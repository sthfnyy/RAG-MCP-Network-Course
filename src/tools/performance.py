import json
from pathlib import Path


def consultar_metricas(equipamento: str | None = None):
    """
    Retorna métricas de desempenho simuladas.

    Args:
        equipamento: filtra as métricas por equipamento.
    """

    arquivo = (
        Path(__file__)
        .parent
        .parent
        / "data"
        / "metrics.json"
    )

    with open(arquivo, "r", encoding="utf-8") as f:
        metricas = json.load(f)

    if equipamento is None:
        return metricas

    return [
        metrica
        for metrica in metricas
        if metrica["equipamento"].lower() == equipamento.lower()
    ]