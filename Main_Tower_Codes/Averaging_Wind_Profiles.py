# -*- coding: utf-8 -*-
"""
Created on Wed Dec 22 16:23:42 2021

@author: Rubix
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


df1 = pd.read_csv('/media/jeremy/Data/Fireflux2/Website_Docs/Main_Tower_Data/Proc_FF2_10HzMTdespiked_rotated.csv', parse_dates=['TIMESTAMP'], skiprows = (0, 2, 3))
#this reads in the dataframe and parses the dates. I also skip unecessary rows. This csv is modified by removing the record column and 
#moving the other columns over
df = df1.truncate(before= np.where(df1['TIMESTAMP'] == '1/30/2013  15:04:00')[0][80], 
                    after=np.where(df1['TIMESTAMP'] == '1/30/2013  15:14:00')[0][80])

time = df['TIMESTAMP']
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


n = 50 #5 second averaging
time2 = np.arange(0, len(time)) / 10
fig, ax = plt.subplots(4, 3, figsize = (20, 10))

ax[0, 0].plot(time2, ux20.rolling(window = n).mean(), 'black', label = 'Avg. ux20m winds', linestyle = '-')
