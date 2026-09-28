import json
from pathlib import Path

DATA_FILE = Path(__file__).resolve().parents[1] / "data" / "metrics.json"


def consultar_metricas(equipamento: str | None = None) -> list[dict]:
    """Consulta exclusivamente o dataset SIMULADO do laboratorio."""
    metricas = json.loads(DATA_FILE.read_text(encoding="utf-8"))
    if not isinstance(metricas, list):
        raise ValueError("metrics.json precisa conter uma lista JSON")
    if equipamento is None or not equipamento.strip():
        return metricas
    nome = equipamento.strip().casefold()
    return [item for item in metricas if item["equipamento"].casefold() == nome]
