from backend.model.system_model import run_preliminary_model


def simulate(**values) -> dict:
    return run_preliminary_model(**values)

