"""Servidor MCP: aluno (simulado) e demonstracao do professor (simulado + rede local)."""
import json
import os
from pathlib import Path

from mcp.server.fastmcp import FastMCP
from src.tools.performance import consultar_metricas
from src.tools.security import consultar_alertas_seguranca

mcp = FastMCP("Network Management MCP")
DATA_DIR = Path(__file__).resolve().parent / "data"


@mcp.tool()
def alertas_seguranca(nivel: str | None = None) -> list[dict]:
    """Consulta alertas SIMULADOS; nivel: alto, medio ou baixo. Omitido: todos."""
    return consultar_alertas_seguranca(nivel)



@mcp.tool()
def metricas_rede(equipamento: str | None = None):
    """
    Consulta métricas SIMULADAS de desempenho de equipamentos
    de rede, utilizando os dados de um arquivo JSON.

    Os valores são fictícios e utilizados exclusivamente
    para fins didáticos.

    Campos retornados:
    - equipamento: identificador do equipamento fictício;
    - latencia_ms: latência simulada em milissegundos;
    - vazao_mbps: vazão simulada em megabits por segundo;
    - perda_pacotes_percentual: perda simulada de pacotes.

    IMPORTANTE:
    O campo vazao_mbps NÃO representa necessariamente
    a capacidade máxima do equipamento.

    Args:
        equipamento: nome do equipamento a consultar.
                     Se omitido, retorna todos.
    """
    return consultar_metricas(equipamento)


@mcp.resource("network://topologia-simulada")
def topologia_simulada() -> str:
    """Topologia FICTICIA do laboratorio; nao corresponde a rede do usuario."""
    return (DATA_DIR / "topology.json").read_text(encoding="utf-8")


@mcp.prompt()
def analisar_incidente_rede() -> str:
    """Roteiro de analise de um incidente, distinguindo simulacao de dados reais."""
    return (
        "Investigue os alertas e metricas disponiveis. Identifique a origem de cada "
        "resultado como SIMULADO ou REAL. Compare sintomas, informe horarios quando "
        "existirem e diferencie hipotese de incidente confirmado. Nao afirme que "
        "trafego alto confirma DDoS. Nao execute alteracoes na infraestrutura."
    )


# A Tool real nem sequer e registrada no modo dos estudantes.
if os.getenv("MCP_ENABLE_REAL_NETWORK", "0") == "1":
    from src.tools.real_network import consultar_rede_real

    @mcp.tool()
    def rede_local_real(interface: str | None = None, intervalo_segundos: int = 2) -> dict:
        """Consulta SOMENTE leitura de interfaces e trafego REAL deste computador.

        interface: nome exato opcional; vazio = interfaces ativas.
        intervalo_segundos: 1 a 5 segundos para calcular a taxa aproximada.
        Nao mede latencia da Internet nem perda ponta a ponta.
        """
        return consultar_rede_real(interface, intervalo_segundos)


if __name__ == "__main__":
    # STDOUT reservado exclusivamente ao protocolo MCP.
    mcp.run(transport="stdio")
