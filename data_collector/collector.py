import yfinance as yf
import pandas as pd
import os

def collect_data(tickers, p, i):

    for tick in tickers:
        print(f"Collecting {tick} data...")    
        ticker = yf.Ticker(tick)
        df = ticker.history(period = p , interval = i)

        new_df = df.drop(['Dividends', 'Stock Splits'], axis = 1)
        new_df = new_df.reset_index()
        new_df['Date'] = pd.to_datetime(new_df['Date'])
        new_df['Date'] = new_df['Date'].dt.strftime('%d/%m/%Y - %H:%M')
        new_df['Volume'] = new_df['Volume'].apply(lambda x: f'{x:_d}')
        # new_df['Volume'] = f"{new_df['Volume']:_d}"
        # print(new_df.info())
        print(new_df.head(5).to_string())

collect_data('PETR4.SA', '1y', '1d')