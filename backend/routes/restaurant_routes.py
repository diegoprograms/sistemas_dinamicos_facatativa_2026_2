import base64
import binascii

from fastapi import APIRouter, HTTPException
from backend.services.restaurant_storage import import_file, list_records, save_rows

router = APIRouter(prefix='/restaurants', tags=['restaurants'])


@router.get('/records')
def records():
    return list_records()


@router.post('/records')
def create_record(record: dict):
    try:
        return save_rows([record])
    except ValueError as exc:
        raise HTTPException(status_code=422, detail=str(exc)) from exc


@router.post('/imports')
def upload_file(submission: dict):
    try:
        encoded = submission.get('contenido_base64', '')
        if not isinstance(encoded, str) or len(encoded) > 7 * 1024 * 1024:
            raise ValueError('Archivo demasiado grande o contenido inválido.')
        name = submission.get('nombre', '')
        if not isinstance(name, str):
            raise ValueError('Nombre de archivo inválido.')
        content = base64.b64decode(encoded, validate=True)
        return import_file(name, content)
    except (ValueError, binascii.Error) as exc:
        raise HTTPException(status_code=422, detail=str(exc)) from exc
