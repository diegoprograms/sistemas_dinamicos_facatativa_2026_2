from fastapi import FastAPI

from backend.routes.data_routes import router as data_router
from backend.routes.simulation_routes import router as simulation_router


app = FastAPI(
    title="Sistema dinámico hídrico-alimentario",
    version="0.1.0",
)

app.include_router(data_router)
app.include_router(simulation_router)


@app.get("/health")
def health() -> dict:
    return {"status": "ok", "message": "Backend funcionando correctamente"}

