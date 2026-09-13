from mcp.server.fastmcp import FastMCP

from src.tools.security import consultar_alertas_seguranca
from src.tools.performance import consultar_metricas


mcp = FastMCP(
    "Network Management MCP"
)


@mcp.tool()
def alertas_seguranca(nivel: str | None = None):
    """
    Consulta alertas de segurança da rede.

    Args:
        nivel: nível do alerta. Pode ser alto, medio ou baixo.
    """

    return consultar_alertas_seguranca(nivel)


@mcp.tool()
def metricas_rede(equipamento: str | None = None):
    """
    Consulta métricas de desempenho da rede.

    Args:
        equipamento: nome do equipamento.
    """

    return consultar_metricas(equipamento)


if __name__ == "__main__":
    print("Servidor MCP de Gerenciamento de Redes iniciado...")
    mcp.run()