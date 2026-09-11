def consultar_alertas_seguranca():
    """
    Retorna alertas de segurança simulados.
    """

    return [
        {
            "tipo": "trafego_anormal",
            "nivel": "alto",
            "descricao": "Volume de tráfego acima do padrão detectado"
        }
    ]