from fastapi import APIRouter

from backend.model.system_model import run_preliminary_model


router = APIRouter(prefix="/simulation", tags=["simulation"])


@router.get("/example")
def example_simulation() -> dict:
    return run_preliminary_model(
        consumption_kg=1000.0,
        available_supply_kg=850.0,
        required_water_m3=300.0,
        available_water_m3=240.0,
    )

