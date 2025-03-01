import talib
import numpy as np

def HMA(close, period=7):
    wma_half = talib.WMA(close, period//2)
    wma_full = talib.WMA(close, period)
    hma_series = 2 * wma_half - wma_full
    return talib.WMA(hma_series, int(np.sqrt(period)))

def generate_signals(df):
    df['hma7'] = HMA(df['close'], 7)
    df['ema9'] = talib.EMA(df['close'], 9)
    df['tema80'] = talib.TEMA(df['close'], 80)
    
    signals = []
    in_long = False
    in_short = False
    
    for idx, row in df.iterrows():
        # 做多条件
        if (row['hma7'] > row['ema9']) and not in_long:
            signals.append(('BUY', row['close'], idx))
            in_long = True
        # 平多条件
        elif (row['hma7'] < row['ema9']) and (row['close'] < row['hma7']) and in_long:
            signals.append(('CLOSE_LONG', row['close'], idx))
            in_long = False
        # 做空条件
        elif (row['hma7'] < row['tema80']) and not in_short:
            signals.append(('SELL', row['close'], idx))
            in_short = True
        # 平空条件
        elif (row['hma7'] > row['ema9']) and in_short:
            signals.append(('CLOSE_SHORT', row['close'], idx))
            in_short = False
    return signals