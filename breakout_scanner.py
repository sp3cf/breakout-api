import yfinance as yf
import pandas as pd
import ta

def is_potential_breakout(df):
    if df.shape[0] < 100:
        return False
    rsi = ta.momentum.RSIIndicator(df['Close']).rsi()
    volume_avg = df['Volume'].rolling(20).mean()
    close = df['Close'].iloc[-1]

    near_high = close >= 0.98 * df['High'].max()
    rsi_ok = rsi.iloc[-1] < 70
    volume_spike = df['Volume'].iloc[-1] > 1.5 * volume_avg.iloc[-1]
    
    return near_high and rsi_ok and volume_spike

def find_breakout_candidates(tickers):
    breakout_stocks = []
    for ticker in tickers:
        try:
            df = yf.download(ticker, period='6mo', interval='1d')
            if is_potential_breakout(df):
                breakout_stocks.append(ticker)
        except:
            continue
    return breakout_stocks
