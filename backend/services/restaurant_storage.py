"""Persistent restaurant records and original submissions, independent of the UI."""
import csv
import hashlib
import io
import json
import math
import os
import sqlite3
from datetime import date, datetime, timezone
from pathlib import Path

COLUMNS = ['restaurante', 'inicio', 'fin', 'producto', 'presentacion',
           'cantidad', 'unidad', 'procedencia', 'metodo']


def storage_root():
    return Path(os.environ.get('RESTAURANT_STORAGE_DIR',
                str(Path(__file__).resolve().parents[2] / 'data' / 'private')))


def connect():
    root = storage_root()
    root.mkdir(parents=True, exist_ok=True)
    con = sqlite3.connect(root / 'restaurantes.sqlite', timeout=15)
    con.row_factory = sqlite3.Row
    con.execute('''CREATE TABLE IF NOT EXISTS records (
        id INTEGER PRIMARY KEY, fingerprint TEXT UNIQUE NOT NULL,
        payload TEXT NOT NULL, source TEXT NOT NULL, created_at TEXT NOT NULL)''')
    con.execute('''CREATE TABLE IF NOT EXISTS imports (
        archivo TEXT PRIMARY KEY, nombre_original TEXT NOT NULL, received_at TEXT NOT NULL)''')
    con.commit()
    return con


def validate(row):
    result = {}
    for name in COLUMNS:
        value = row.get(name)
        if value is None or not str(value).strip():
            raise ValueError(f'Falta el campo {name}.')
        result[name] = str(value).strip()
    for name in ('inicio', 'fin'):
        try:
            result[name] = date.fromisoformat(result[name]).isoformat()
        except ValueError:
            raise ValueError(f'{name}: use una fecha AAAA-MM-DD.') from None
    if result['fin'] < result['inicio']:
        raise ValueError('El final del periodo no puede ser anterior al inicio.')
    try:
        quantity = float(result['cantidad'])
    except (TypeError, ValueError):
        raise ValueError('La cantidad debe ser numérica.') from None
    if not math.isfinite(quantity) or quantity < 0:
        raise ValueError('La cantidad debe ser finita y no negativa.')
    result['cantidad'] = quantity
    result['unidad'] = result['unidad'].lower()
    if result['unidad'] not in ('kg', 'g'):
        raise ValueError('Unidad admitida: kg o g. Convierta otras unidades con un peso conocido.')
    result['metodo'] = result['metodo'].lower()
    if result['metodo'] not in ('pesado', 'factura', 'estimado'):
        raise ValueError('Método admitido: pesado, factura o estimado.')
    for key in ('restaurante', 'producto', 'presentacion', 'procedencia'):
        result[key] = result[key].casefold()
    result['cantidad_kg'] = quantity / 1000 if result['unidad'] == 'g' else quantity
    return result


def save_rows(rows, source='formulario'):
    # Validate the entire submission before writing any row.
    clean = []
    for index, row in enumerate(rows, start=2):
        try:
            clean.append(validate(row))
        except (ValueError, AttributeError) as exc:
            raise ValueError(f'Fila {index}: {exc}') from None
    if not clean:
        raise ValueError('La entrega no contiene registros.')
    con = connect()
    added = 0
    try:
        with con:
            for row in clean:
                payload = json.dumps(row, sort_keys=True, ensure_ascii=False)
                fingerprint = hashlib.sha256(payload.encode()).hexdigest()
                cursor = con.execute(
                    'INSERT OR IGNORE INTO records (fingerprint,payload,source,created_at) VALUES (?,?,?,?)',
                    (fingerprint, payload, source, datetime.now(timezone.utc).isoformat()))
                added += cursor.rowcount
    finally:
        con.close()
    return {'guardados': added, 'duplicados': len(clean) - added}


def list_records():
    con = connect()
    try:
        return [dict(json.loads(row['payload']), id=row['id'], origen=row['source'],
                     guardado_en=row['created_at'])
                for row in con.execute('SELECT * FROM records ORDER BY id DESC')]
    finally:
        con.close()


def import_file(name, content):
    suffix = Path(name).suffix.lower()
    if suffix not in ('.csv', '.xlsx'):
        raise ValueError('Solo se admiten archivos CSV o XLSX.')
    if len(content) > 5 * 1024 * 1024:
        raise ValueError('El archivo supera 5 MB.')
    if suffix == '.csv':
        try:
            rows = list(csv.DictReader(io.StringIO(content.decode('utf-8-sig'))))
        except UnicodeDecodeError:
            raise ValueError('El CSV debe estar codificado en UTF-8.') from None
    else:
        import pandas as pd
        try:
            frame = pd.read_excel(io.BytesIO(content), dtype=str, keep_default_na=False)
            for column in ('inicio', 'fin'):
                if column in frame:
                    frame[column] = frame[column].str.replace(' 00:00:00', '', regex=False)
            rows = frame.to_dict('records')
        except Exception as exc:
            raise ValueError('No se pudo leer el Excel. Use la primera hoja con las columnas de la plantilla.') from exc
    if not rows:
        raise ValueError('El archivo no contiene registros.')
    # Validate before archiving; the raw bytes are retained for accepted submissions.
    for index, row in enumerate(rows, start=2):
        try:
            validate(row)
        except ValueError as exc:
            raise ValueError(f'Fila {index}: {exc}') from None
    digest = hashlib.sha256(content).hexdigest()
    archive = storage_root() / 'originales'
    archive.mkdir(parents=True, exist_ok=True)
    path = archive / (digest + suffix)
    path.write_bytes(content)
    result = save_rows(rows, source=path.name)
    con = connect()
    try:
        with con:
            con.execute('INSERT OR IGNORE INTO imports VALUES (?,?,?)',
                        (path.name, Path(name).name, datetime.now(timezone.utc).isoformat()))
    finally:
        con.close()
    return dict(result, archivo=path.name)
