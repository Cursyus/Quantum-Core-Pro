# 💎 QuantumCore Pro v51.1 - Cloud & Intelligence Edition

**QuantumCore Pro** é um sistema de trading algorítmico de alta frequência (HFT) desenvolvido para o mercado de Criptomoedas (Binance Spot). Ele opera com uma arquitetura híbrida, permitindo execução visual em Desktop (Windows) ou execução "Headless" em servidores na nuvem (Render/AWS).

![Status](https://img.shields.io/badge/Status-Stable-green) ![Python](https://img.shields.io/badge/Python-3.11+-blue) ![Strategy](https://img.shields.io/badge/Strategy-Mean_Reversion-orange)

## 🚀 Funcionalidades Principais

### 🧠 Inteligência de Mercado
* **Estratégia Híbrida:** RSI (Reversão) + Bollinger Bands + **Filtro de Tendência EMA 200**.
* **Anti-Mico (Liquidez):** Ignora automaticamente moedas com volume < $1 Milhão/24h.
* **Smart Trailing Stop:** Ativa em **2.1%** de lucro e persegue a alta. Vende se cair **0.3%** do topo.
* **Zombie Killer v2:** Detecta trades estagnados por **1 hora** e libera o capital automaticamente.

### 🛡️ Segurança Financeira
* **Circuit Breaker Diário:**
    * 🏆 Meta: Pára de comprar ao atingir **$10.00** de lucro no dia.
    * 🛑 Stop Global: Desliga o bot se o prejuízo atingir **-$5.00**.
* **Gestão de Slots:** Limite estrito de 2 trades simultâneos para evitar sobrexposição.

### 📡 Controle Remoto (Telegram)
* **Notificações em Tempo Real:** Compra, Venda, Zombie Kill e Trailing Stop.
* **Análise Visual:** Envia **Gráficos de Candles** (Print) com indicadores desenhados no momento da operação.
* **Comandos:** `/status`, `/relatorio`, `/ajuda`.

---

## ☁️ Implantação na Nuvem (Render / VPS)

O bot está preparado para rodar 24/7 em serviços como **Render.com**. Ele utiliza Variáveis de Ambiente para segurança.

### 1. Configuração do Serviço
* **Build Command:** `pip install -r requirements.txt`
* **Start Command:** `python server.py`

### 2. Variáveis de Ambiente (Environment Variables)
Adicione estas chaves no painel do seu servidor para conectar o bot:

| Chave (Key) | Valor (Value) | Descrição |
| :--- | :--- | :--- |
| `BINANCE_API_KEY` | `sua_api_key_aqui` | Chave de API da Binance (Spot). |
| `BINANCE_SECRET_KEY` | `sua_secret_key_aqui` | Segredo da API da Binance. |
| `TELEGRAM_BOT_TOKEN` | `123456:ABC-DEF...` | Token do seu bot criado no @BotFather. |
| `TELEGRAM_CHAT_ID` | `123456789` | Seu ID numérico do Telegram (use @userinfobot para descobrir). |
| `TEST_MODE` | `false` | Defina como `true` para usar **Binance Testnet** (Dinheiro Fictício). |

> **⚠️ Atenção:** Se `TEST_MODE` for `true`, as chaves da API devem ser da **Binance Testnet**, não da conta real.

---

## 🖥️ Instalação e Uso Local (Windows)

Para rodar no seu computador com Interface Gráfica e Gráficos em Tempo Real.

1.  **Pré-requisitos:**
    * Miniconda ou Python 3.11+ instalado.
2.  **Instalação:**
    ```bash
    # Crie o ambiente (apenas na primeira vez)
    conda create -n r2 python=3.11
    conda activate r2
    pip install -r requirements.txt
    ```
3.  **Executar:**
    * Clique duas vezes no arquivo `START_BOT.bat`.

---

## 🤖 Comandos do Telegram

* `/start` - Inicia o menu principal.
* `/status` - Mostra lucro do dia, trades ativos e slots ocupados.
* `/relatorio` - Lista os últimos trades realizados e o PnL acumulado.

---

## ⚙️ Configuração Avançada (`core/config.py`)

Se estiver rodando localmente, você pode ajustar a estratégia direto no arquivo:

```python
TRADE_AMOUNT = 25.0       # Valor por operação ($)
TAKE_PROFIT = 0.021       # Alvo de Lucro (2.1%)
STOP_LOSS = 0.04          # Proteção (4%)
TRAILING_CALLBACK = 0.003 # Recuo permitido no Trailing (0.3%)

⚠️ Disclaimer

Este software é uma ferramenta de automação. O mercado de criptomoedas é volátil. O autor não se responsabiliza por perdas financeiras. Use o TEST_MODE para validar sua estratégia antes de operar capital real.

Desenvolvido por Tedyzeta - 2026