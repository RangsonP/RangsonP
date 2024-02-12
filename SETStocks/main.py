import time
import pandas as pd
import yfinance as yf

Stocks = 'BANPU.BK'

data = yf.Ticker(Stocks).history(period='1y', interval='1d')

print(data['Close'])

