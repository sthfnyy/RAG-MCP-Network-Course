# Laboratorio MCP — dois cenarios

**Aluno:** apenas `metricas_rede`, `alertas_seguranca`, Resource e Prompt, com JSON simulado. Dependencias em `requirements.txt`.

**Professor:** as mesmas funcionalidades e, mediante `MCP_ENABLE_REAL_NETWORK=1`, a Tool extra `rede_local_real`, que le estatisticas reais das interfaces locais usando `psutil`. Dependencias em `requirements-professor.txt`. Nenhuma Tool altera a rede ou realiza varredura.

## Instalar — Windows PowerShell

Na pasta raiz do projeto:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m unittest discover -s tests -v
```

Para a maquina do professor:

```powershell
python -m pip install -r requirements-professor.txt
$env:MCP_ENABLE_REAL_NETWORK = "1"
python -m unittest discover -s tests -v
```

**Nao execute `python -m src.server` num terminal separado quando o Inspector ou Claude iniciara o processo STDIO.**

## Inspector

```powershell
npx -y @modelcontextprotocol/inspector
```

Cadastrar servidor STDIO com `command` = caminho absoluto de `venv\Scripts\python.exe` e `args` = `-m src.server`. Definir raiz do projeto como CWD quando o Inspector oferecer essa opcao. No modo professor, passar `MCP_ENABLE_REAL_NETWORK=1` pelo ambiente que inicia o Inspector ou pelas configuracoes do servidor.

## Testes

Tools: `alertas_seguranca()` (2), `alertas_seguranca(nivel="alto")` (1), `metricas_rede()` (3), `metricas_rede(equipamento="roteador-01")` (1). Resource `network://topologia-simulada`. Prompt `analisar_incidente_rede`. No professor, adicionalmente `rede_local_real(intervalo_segundos=2)`.

## Claude Desktop (professor)

Copie e ajuste o exemplo em `config/claude_desktop_config_EXEMPLO.json`. No Windows, a configuracao de chat costuma estar em `%APPDATA%\Claude\claude_desktop_config.json`. Preencha o executavel Python e `PYTHONPATH` absolutos, depois reinicie o aplicativo. Use `MCP_ENABLE_REAL_NETWORK=1` apenas no computador do professor. A configuracao desse arquivo e da aba Code do Claude Desktop sao diferentes.

**Privacidade:** o modo real pode expor nomes das interfaces e contadores do seu computador a um cliente MCP ou LLM conectado. Evite mostrar nomes privados em tela compartilhada; nao exponha o servidor diretamente na Internet.

## Arquivos

`src/server.py`: registra Tools, Resource e Prompt. `src/tools/`: logica separada de consulta. `src/data/`: datasets ficticios. `tests/`: testes logicos. `config/`: exemplo de configuracao para Claude Desktop.
