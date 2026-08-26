from fastapi import APIRouter


router = APIRouter(prefix="/data", tags=["data"])


@router.get("/required")
def required_data() -> dict:
    return {
        "consumption": ["fecha", "producto", "cantidad_kg"],
        "climate": ["fecha", "precipitacion_mm", "temperatura_c"],
        "water": ["fecha", "fuente", "disponible_m3", "utilizada_m3"],
        "production": ["cultivo", "area_ha", "produccion_kg"],
        "supply": ["fecha", "producto", "oferta_local_kg", "oferta_externa_kg"],
    }

