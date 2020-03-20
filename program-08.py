#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Due March 27, 2020
Created on Thu Mar 19 17:11:40 2020
by Hannah Walcek
Assignment 08 - Time Series Analysis With Pandas

Script that produces daily and monthly plots from Wabash River discharge data from 
March 17, 2015 through March 24, 2016
"""
#import modules
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas import Series

#loading data
wr = pd.read_table('WabashRiver_DailyDischarge_20150317-20160324.txt', 
                   skiprows=26, header=None, sep = r"\s*")
#add headers for columns
wr.columns = ['agency code', 'site number', 'date', 'time', 'zone', 
              'discharge', 'other']

#convert data in to time series starting at 2015-03-17 in 15 minute increments
dates = pd.date_range(start='2015-03-17', periods=wr.shape[0], freq='15min')
wr = wr.values
WR = Series(wr[:,5], index=dates)
WR = WR.astype(np.int) #make sure data is int

#create a plot of daily average stream flow
WR_daily = WR.resample("D").mean()
WR_daily.plot()
plt.title('Daily Average Stream Flow')
plt.ylabel('Discharge (cubic feet per second)')
plt.xlabel('Time')
plt.savefig('Daily_Average_Streamflow.pdf')
plt.close()

#identify top ten values
top = WR_daily.sort_values(ascending=False)[:10]
ax = top.plot(style='ro')
WR_daily.plot(ax=ax)
plt.title('Daily Average Stream Flow with Top 10 Values')
plt.ylabel('Discharge (cubic feet per second)')
plt.xlabel('Time')
plt.savefig('High_Points.pdf')
plt.close()

#greate a plot of monthly average streamflow
WR_monthly = WR.resample("M").mean()
WR_monthly.plot()
plt.title('Monthly Average Stream Flow')
plt.ylabel('Discharge (cubic feet per second)')
plt.xlabel('Time')
plt.savefig('Monthly_Average_Streamflow.pdf')
plt.close()