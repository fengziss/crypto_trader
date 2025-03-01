import pandas as pd
import requests

def fetch_okx_data(symbol='BTC-USDT', timeframe='1H'):
    url = "https://www.okx.com/api/v5/market/history-candles"
    params = {
        'instId': symbol,
        'bar': timeframe,
        'limit': 1000
    }
    response = requests.get(url, params=params)
    data = response.json()['data']
    df = pd.DataFrame(data, columns=['timestamp', 'open', 'high', 'low', 'close', 'vol'])
    df['timestamp'] = pd.to_datetime(df['timestamp'].astype(int), unit='ms')
    df.set_index('timestamp', inplace=True)
    df = df.astype(float)
    return df