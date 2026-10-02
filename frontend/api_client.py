import os

import requests


API_URL = os.environ.get("BACKEND_URL", "http://127.0.0.1:8000").rstrip("/")


def health_check() -> dict:
    response = requests.get(f"{API_URL}/health", timeout=5)
    response.raise_for_status()
    return response.json()

