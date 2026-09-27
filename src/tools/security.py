import json
from pathlib import Path

DATA_FILE = Path(__file__).resolve().parents[1] / "data" / "alerts.json"
NIVEIS = {"alto", "medio", "baixo"}


def consultar_alertas_seguranca(nivel: str | None = None) -> list[dict]:
    """Consulta exclusivamente os alertas SIMULADOS do laboratorio."""
    alertas = json.loads(DATA_FILE.read_text(encoding="utf-8"))
    if not isinstance(alertas, list):
        raise ValueError("alerts.json precisa conter uma lista JSON")
    if nivel is None or not nivel.strip():
        return alertas
    nivel = nivel.strip().casefold()
    if nivel not in NIVEIS:
        raise ValueError(f"Nivel invalido: {nivel!r}. Use alto, medio ou baixo.")
    return [item for item in alertas if item["nivel"].casefold() == nivel]
