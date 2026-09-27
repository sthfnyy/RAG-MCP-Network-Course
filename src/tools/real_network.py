from datetime import datetime, timezone
import time
import psutil


def consultar_rede_real(interface: str | None = None, intervalo_segundos: int = 2) -> dict:
    if not isinstance(intervalo_segundos, int) or not 1 <= intervalo_segundos <= 5:
        raise ValueError("intervalo_segundos deve ser inteiro entre 1 e 5")

    status = psutil.net_if_stats()
    antes = psutil.net_io_counters(pernic=True)
    tempo_inicio = time.monotonic()
    time.sleep(intervalo_segundos)
    depois = psutil.net_io_counters(pernic=True)
    duracao = max(time.monotonic() - tempo_inicio, 0.001)

    if interface:
        if interface not in depois:
            raise ValueError(
                f"Interface nao encontrada: {interface!r}. "
                f"Disponiveis: {', '.join(sorted(depois))}"
            )
        nomes = [interface]
    else:
        nomes = [nome for nome in depois if status.get(nome) and status[nome].isup]

    interfaces = []
    for nome in sorted(nomes):
        atual, inicial = depois[nome], antes.get(nome)
        if inicial is None:
            continue
        tx = max(0, atual.bytes_sent - inicial.bytes_sent)
        rx = max(0, atual.bytes_recv - inicial.bytes_recv)
        interfaces.append({
            "nome": nome,
            "ativa": bool(status.get(nome) and status[nome].isup),
            "bytes_enviados_total": atual.bytes_sent,
            "bytes_recebidos_total": atual.bytes_recv,
            "tx_mbps_aproximado": round(tx * 8 / duracao / 1_000_000, 4),
            "rx_mbps_aproximado": round(rx * 8 / duracao / 1_000_000, 4),
        })

    return {
        "origem": "REAL: contadores do computador que executa o servidor",
        "coletado_em_utc": datetime.now(timezone.utc).isoformat(),
        "intervalo_medido_segundos": round(duracao, 2),
        "interfaces": interfaces,
        "observacao": "Nao e latencia de Internet, perda ponta a ponta nem detector de DDoS."
    }
