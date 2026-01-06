import os

class Config:
    # --- MODO DE OPERAÇÃO ---
    # Se estiver "true" no Render, vira True no Python. Se não tiver nada, assume False (Real).
    TEST_MODE = os.getenv("TEST_MODE", "False").lower() == "true"

    # --- CREDENCIAIS ---
    API_KEY = os.getenv("BINANCE_API_KEY", "SUA_KEY_LOCAL")
    SECRET_KEY = os.getenv("BINANCE_SECRET_KEY", "SUA_SECRET_LOCAL")
    
    TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "SEU_TOKEN")
    TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID", "SEU_CHAT_ID")

    # --- CONFIGURAÇÕES GERAIS ---
    PAIRS = [
        {'symbol': 'SOL/USDT'}, {'symbol': 'RENDER/USDT'}, {'symbol': 'AVAX/USDT'}, 
        {'symbol': 'NEAR/USDT'}, {'symbol': 'FET/USDT'}, {'symbol': 'ETH/USDT'},
        {'symbol': 'BNB/USDT'}, {'symbol': 'DOGE/USDT'}, {'symbol': 'LINK/USDT'},
        {'symbol': 'ADA/USDT'}, {'symbol': 'XRP/USDT'}, {'symbol': 'DOT/USDT'},
        {'symbol': 'UNI/USDT'}, {'symbol': 'LTC/USDT'}, {'symbol': 'ATOM/USDT'},
        {'symbol': 'INJ/USDT'}, {'symbol': 'OP/USDT'}, {'symbol': 'ARB/USDT'},
        {'symbol': 'PEPE/USDT'}, {'symbol': 'SUI/USDT'}
    ]
    TIMEFRAME = '1m'
    
    SANDBOX_MODE = TEST_MODE
    
    # SEGURANÇA ALTCOIN
    MIN_24H_VOLUME = 10000000 # Mínimo 10 Milhões de dólares de volume
    RSI_OVERSOLD = 33          # Aumentamos de 30 para 35 para dar mais chances de entrada
    
    # --- GERENCIAMENTO DE RISCO ---
    TRADE_AMOUNT = 25.0      # Aumentado para $25 por slot
    MAX_OPEN_TRADES = 2      # Continua 2 slots (Total investido: $50)
    
    # --- SAÍDA E LUCRO ---
    TAKE_PROFIT = 0.021      # 2.1% (Alvo base)
    STOP_LOSS = 0.04         # 4% (Mantivemos o stop de segurança)

    # --- TRAILING STOP (O Deixa Correr) ---
    USE_TRAILING_STOP = True
    TRAILING_ACTIVATION = 0.021   # Ativa o rastreio quando bater 2.1% de lucro
    TRAILING_CALLBACK = 0.003     # Vende se cair 0.3% do topo atingido
    
    # --- FILTROS DE TENDÊNCIA ---
    USE_EMA_FILTER = True         # Se True, só compra acima da EMA
    EMA_PERIOD = 200              # Tendência de longo prazo
    LIMIT_CANDLES = 300           # Aumentamos para garantir cálculo preciso da EMA 200
    
    BTC_CRASH_LIMIT = -3.0     # Deixamos o BTC "respirar" mais antes de travar o bot
    ZOMBIE_TIMEOUT = 3600      # 1 horas em segundos

    # --- FILTROS DE QUALIDADE ---
    MIN_VOLUME_24H = 1000000.0  # (1 Milhão USD) Só opera moedas com alta liquidez