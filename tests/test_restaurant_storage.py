import csv
import io
import os
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from backend.services.restaurant_storage import COLUMNS, import_file, list_records, save_rows


class RestaurantStorageTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        env = patch.dict(os.environ, RESTAURANT_STORAGE_DIR=self.temp.name)
        env.start()
        self.addCleanup(env.stop)
        self.row = dict(zip(COLUMNS, ['R01', '2026-10-01', '2026-10-07',
                        'Papa', 'Entera', 500, 'g', 'Desconocida', 'pesado']))

    def test_persistence_and_duplicate_between_sources(self):
        self.assertEqual(save_rows([self.row])['guardados'], 1)
        # Each call opens and closes its own database connection.
        self.assertEqual(list_records()[0]['cantidad_kg'], .5)
        content = io.StringIO()
        writer = csv.DictWriter(content, fieldnames=COLUMNS)
        writer.writeheader()
        writer.writerow(self.row)
        original = content.getvalue().encode()
        result = import_file('../../entrega.csv', original)
        self.assertEqual(result['duplicados'], 1)
        self.assertEqual(len(list_records()), 1)
        self.assertEqual((Path(self.temp.name) / 'originales' / result['archivo']).read_bytes(), original)

    def test_excel_round_trip(self):
        import pandas as pd
        stream = io.BytesIO()
        pd.DataFrame([self.row]).to_excel(stream, index=False)
        result = import_file('entrega.xlsx', stream.getvalue())
        self.assertEqual(result['guardados'], 1)
        self.assertEqual(list_records()[0]['producto'], 'papa')
        self.assertEqual(import_file('entrega.xlsx', stream.getvalue())['duplicados'], 1)

    def test_invalid_batch_is_not_partially_saved(self):
        with self.assertRaises(ValueError):
            save_rows([self.row, dict(self.row, cantidad='nan')])
        self.assertEqual(list_records(), [])

    def test_dates_units_and_empty_fields(self):
        for changes in ({'fin': '2026-09-01'}, {'unidad': 'bulto'},
                        {'producto': ' '}, {'cantidad': -1}, {'inicio': 'ayer'}):
            with self.subTest(changes=changes), self.assertRaises(ValueError):
                save_rows([dict(self.row, **changes)])

    def test_invalid_import_leaves_no_archive(self):
        with self.assertRaises(ValueError):
            import_file('entrega.csv', b'otra_columna\nvalor\n')
        self.assertFalse((Path(self.temp.name) / 'originales').exists())


if __name__ == '__main__':
    unittest.main()
