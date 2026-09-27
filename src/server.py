
from mcp.server.fastmcp import FastMCP

from src.tools.security import consultar_alertas_seguranca
from src.tools.performance import consultar_metricas


mcp = FastMCP("Network Management MCP")


@mcp.tool()
def alertas_seguranca(nivel: str | None = None):
    """
    Consulta alertas de segurança simulados da rede.

    Args:
        nivel: filtra por nível do alerta:
               alto, medio ou baixo.
               Se omitido, retorna todos.
    """
    return consultar_alertas_seguranca(nivel)


@mcp.tool()
def metricas_rede(equipamento: str | None = None):
    """
    Consulta métricas de desempenho simuladas da rede.

    Args:
        equipamento: nome do equipamento.
                     Se omitido, retorna todos.
    """
    return consultar_metricas(equipamento)


if __name__ == "__main__":
    mcp.run()
