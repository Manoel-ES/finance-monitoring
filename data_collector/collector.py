import yfinance as yf
import pandas as pd
import os
import cleaner

def collect_data(tickers, p, i):
    if not os.path.exists('data'):
        os.makedirs('data')

    for tick in tickers:
        try:
            print(f"Collecting {tick} data...")    
            ticker = yf.Ticker(tick)
            df = ticker.history(period = p , interval = i, raise_errors = True)
            if df.empty:
                print(f"Empty data to {tick}")
                continue

            cleaned_df = cleaner.clean_data(df)

            filepath = os.path.join('data', f'{tick}.csv')
            cleaned_df.to_csv(filepath, index = False)

        except Exception as e:
            err_msg = str(e)
            if 'possibly delisted' in err_msg:
                print(f'Error collecting tick: {tick} is delisted')
            else:
                print(f'GENERIC ERROR COLLECTING {tick}')

    print('Completed')


collect_data(['PETR4.SA', 'AAPL'], '1y', '1d')