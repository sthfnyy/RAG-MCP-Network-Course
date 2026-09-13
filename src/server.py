from mcp.server.fastmcp import FastMCP

from src.tools.security import consultar_alertas_seguranca

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


if __name__ == "__main__":
    print("Servidor MCP de Gerenciamento de Redes iniciado...")
    mcp.run()