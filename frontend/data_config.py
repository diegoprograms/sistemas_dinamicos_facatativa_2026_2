import pandas as pd


TABLES = {
    "Establecimientos": pd.DataFrame([{
        "id_sitio": "SIT001", "nombre": "Restaurante El Campo", "sector": "Centro",
        "tipo_menu": "Ejecutivo", "observaciones": "",
    }]),
    "Observaciones del almuerzo": pd.DataFrame([{
        "id_observacion": "OBS001", "id_sitio": "SIT001", "fecha": "2026-09-01",
        "hora_inicio": "12:00", "hora_fin": "14:00", "clientes_ingresaron": 100,
        "personas_excluidas": 5, "clientes_validos": 95, "dia_especial": "No",
        "observaciones": "",
    }]),
    "Menús": pd.DataFrame([{
        "id_menu": "MEN001", "id_sitio": "SIT001", "fecha": "2026-09-01",
        "tipo_menu": "Ejecutivo", "archivo_foto": "menu_ejemplo.jpg",
        "fuente": "Plataforma de domicilios", "estado_revision": "Pendiente",
    }]),
    "Platos": pd.DataFrame([{
        "id_plato": "PLA001", "id_menu": "MEN001", "nombre_plato": "Ajiaco",
        "descripcion": "Con arroz y aguacate", "precio": 22000, "es_almuerzo": True,
        "es_popular": True, "participacion_estimada": 0.30,
        "fuente_participacion": "Supuesto",
    }]),
    "Ingredientes por plato": pd.DataFrame([{
        "id_ingrediente_plato": "ING001", "id_plato": "PLA001", "producto": "Papa",
        "variedad": "Pastusa", "cantidad_g_por_porcion": 230,
        "cantidad_kg_por_porcion": 0.230, "estado_producto": "Crudo",
        "fuente_receta": "Receta estándar", "nivel_confianza": "Media",
    }]),
    "Abastecimiento": pd.DataFrame([{
        "id_abastecimiento": "ABA001", "id_sitio": "SIT001",
        "categoria_producto": "Verduras", "producto": "Papa",
        "frecuencia_compra": "Semanal", "intervalo_dias": 7, "dias_compra": "Lunes",
        "cantidad_compra_kg": 50.0, "lugar_compra": "Plaza de mercado",
        "fuente_dato": "Estimación", "nivel_confianza": "Baja",
    }]),
}

SCENARIOS = pd.DataFrame([
    {"escenario": "Bajo", "tasa_compra": 0.75, "platos_por_comprador": 0.95, "ajuste_porcion": 0.85},
    {"escenario": "Probable", "tasa_compra": 0.85, "platos_por_comprador": 1.00, "ajuste_porcion": 1.00},
    {"escenario": "Alto", "tasa_compra": 0.95, "platos_por_comprador": 1.05, "ajuste_porcion": 1.15},
])

STUDENT_TABLES = {
    "Establecimientos": [
        "ID_establecimiento", "Grupo", "Zona", "Tipo_establecimiento",
        "Referencia_ubicacion", "Colabora_residuos", "Observaciones",
    ],
    "Conteo_personas": [
        "ID_jornada", "Fecha", "ID_establecimiento", "Grupo", "Zona",
        "Hora_inicio", "Hora_fin", "Personas_ingresan", "Duracion_min", "Observaciones",
    ],
    "Residuos": [
        "ID_jornada", "Fecha", "ID_establecimiento", "Grupo", "Zona", "Tipo_residuo",
        "Masa", "Unidad", "Metodo_medicion", "Periodo_corresponde", "Observaciones",
    ],
}
