from mcp.server.fastmcp import FastMCP

from src.tools.security import consultar_alertas_seguranca

mcp = FastMCP(
    "Network Management MCP"
)


@mcp.tool()
def alertas_seguranca():
    """
    Consulta alertas de segurança da rede.
    """

    return consultar_alertas_seguranca()


if __name__ == "__main__":
    print("Servidor MCP de Gerenciamento de Redes iniciado...")
    mcp.run()