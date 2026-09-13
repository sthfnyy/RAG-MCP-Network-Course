import json
from pathlib import Path


def consultar_alertas_seguranca(nivel: str | None = None):
    """
    Retorna alertas de segurança simulados.

    Args:
        nivel: filtra os alertas por nível.
    """

    arquivo = (
        Path(__file__)
        .parent
        .parent
        / "data"
        / "alerts.json"
    )

    with open(arquivo, "r", encoding="utf-8") as f:
        alertas = json.load(f)

    if nivel is None:
        return alertas

    return [
        alerta
        for alerta in alertas
        if alerta["nivel"].lower() == nivel.lower()
    ]