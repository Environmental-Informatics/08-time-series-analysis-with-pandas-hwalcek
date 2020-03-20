#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Due March 27, 2020
Created on Thu Mar 19 15:43:52 2020
by Hannah Walcek
Assignment 08 - Time Series Analysis With Pandas

Script that produces various plots from monthly arctic oscillation (AO) and 
north atlantic oscillation (NAO)
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas import Series, DataFrame

#loading data
ao = np.loadtxt('monthly.ao.index.b50.current.ascii')
#head and tail shows us that the start date is 1950-01 most current date is from 2020-02
dates = pd.date_range(start='1950-01', end='2020-02', freq='M')
#other way of writing without specifying the end
dates = pd.date_range(start='1950-01', periods=ao.shape[0], freq='M')
dates

AO = Series(ao[:,2], index=dates)

#plot total time series
AO.plot()
plt.savefig('DailyAtlanticOscillation.png')
plt.close()
#plot smaller portion
AO['1980':'1990'].plot()
plt.close()
#plot even smaller portion
AO['1980-05':'1981-03'].plot()
plt.close()

#individual value
AO[120]

#individual by index
AO['1960-01']

#one year
AO['1960']

#where values are greater than 0
AO[AO >0]

#loading new data and creating series same way as for AO
nao = np.loadtxt('norm.nao.monthly.b5001.current.ascii')
dates_nao = pd.date_range('1950-01', periods=nao.shape[0], freq='M')
NAO = Series(nao[:,2], index=dates_nao)

NAO.index

#create data frame that will contain both AO and NAO data - different lengths are fine
#this will not work
aonao = DataFrame({'AO':AO, 'NAO':NAO})

#plot data
aonao.plot(subplots=True)
plt.close()

#look at first rows of aonao
aonao.tail()

#add column to data frame
aonao['Diff'] = aonao['AO'] - aonao['NAO']
aonao.head()

#deleting said column
del aonao['Diff']
aonao.head()

import datetime
aonao.loc[(aonao.AO > 0) & (aonao.NAO < 0) 
        & (aonao.index > datetime.datetime(1980,1,1)) 
        & (aonao.index < datetime.datetime(1989,1,1)),
        'NAO'].plot(kind='barh')
plt.close()

#let's do some statistics
aonao.mean()
aonao.max()
aonao.min()
#mean row-wise
aonao.mean(1)

#gets most statistical information
aonao.describe()

#annual ('A') mean
AO_mm = AO.resample("A").mean()
AO_mm.plot(style='g--')
plt.close()

#median
AO_mm = AO.resample("A").median()
AO_mm.plot()
plt.savefig('AnnualMedianValues.png')
plt.close()

#rolling mean
aonao.rolling(window=12, center=False).mean().plot(style='-g')
plt.savefig('RollingMean.png')
plt.close()







