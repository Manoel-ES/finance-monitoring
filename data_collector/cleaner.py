import os
import pandas as pd

def clean_data(df):

    # new_df = pd.read_csv(tick)
    new_df = df.drop(['Dividends', 'Stock Splits'], axis = 1)
    new_df = new_df.reset_index()

    new_df['Date']  = pd.to_datetime(new_df['Date'])
    new_df['Date']  = new_df['Date'].dt.strftime('%d/%m/%Y - %H:%M')
    new_df['Open']  = pd.to_numeric(new_df['Open'], errors = 'coerce')
    new_df['High']  = pd.to_numeric(new_df['High'], errors = 'coerce')
    new_df['Low']   = pd.to_numeric(new_df['Low'], errors = 'coerce')
    new_df['Close'] = pd.to_numeric(new_df['Close'], errors = 'coerce')
    # new_df['Volume']= pd.to_numeric(df['Volume'], errors='coerce')

    new_df = new_df.dropna()
    
    return new_df