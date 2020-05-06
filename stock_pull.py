# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 21:44:48 2020

@author: Gregoireg
"""
#%%

import yfinance as yf
import matplotlib.pyplot as plt
from datetime import timedelta

ticker = "YRI.TO"
data = yf.download(tickers= ticker, period="5d", interval="15m")
data = data.reset_index()

time = []
price = data['Open']

print(price)
val = data['Close'][-1:]
print(val)
price = price.append(val, ignore_index=True)
print(price)

#print(time+timedelta(minutes=15))
plt.plot(price)