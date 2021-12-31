# -*- coding: utf-8 -*-
"""
Created on Wed Dec 22 10:34:40 2021

@author: Jeremy Benik
"""
# "%m/%d/%Y, %H:%M:%S"
import pandas as pd
import numpy as np
import statistics as st
import matplotlib.pyplot as plt
import datetime 
df = pd.read_csv('F:/Fireflux2/Website_Docs/data_for_messing_with.csv')
# %% Defining variables to make life easier
time = pd.to_datetime(df['TIMESTAMP'])
# time = df['TIMESTAMP']
ux20 = df['Ux_20m']
uy20 = df['Uy_20m']
uz20 = df['Uz_20m']
ts20 = df['Ts_20m']
ux10 = df['Ux_10m']
uy10 = df['Uy_10m']
uz10 = df['Uz_10m']
ts10 = df['Ts_10m']
ux6 = df['Ux_6m']
uy6 = df['Uy_6m']
uz6 = df['Uz_6m']
ts6 = df['Ts_6m']
# %% This graph is all the data over the 35 minute time interval, and the black lines are the averaged time
#over 5 seconds. To change the average time, change the value of n to something else
#keep in mind that this is 10hz
y = np.where(time == '1/30/2013  15:04:00')[0][80]
n = 50
time2 = np.arange(0, len(time)) / 10
fig = plt.figure(figsize = (12, 12))
plt.title('Plots of variables without an average')
plt.plot(time2, ux20, 'r', label = 'ux20m winds')
plt.vlines(np.where(time == '1/30/2013  15:04:00')[0][80] / 10, min(ux20), max(ux20), color='blue')
plt.plot(time2, ux20.rolling(window = n).mean(), 'black', label = 'A')
