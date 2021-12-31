# -*- coding: utf-8 -*-
"""
Created on Fri Nov 19 11:23:59 2021

@author: Jeremy Benik
"""
# %% Importing necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import datetime
import os
# %% Going through one file to see what is inside of it, then will probably iteratre through all files
df = pd.read_csv('F:/Fireflux2/Website_Docs/FF2Anemometers/14.csv', parse_dates=['Date Time, GMT+00:00'], 
                 encoding = 'unicode_escape', skiprows = (0, 2))
# start of fire is: 1/30/2013  15:04:08
#20 intervals for every minute, so every 3 seconds there is an observation, so I will pick the third one
# %% Assigning variables
# x = np.where(df['Date Time, GMT+00:00'] == '1/30/2013  15:34:00')[0][3]
# y = np.where(df['Date Time, GMT+00:00'] == '1/30/2013  14:34:00')[0][3]
newdf = df[df['Date Time, GMT+00:00'].between('2013-01-30 14:34:00', '2013-01-30  15:34:00')]
#30 minutes before and 30 minutes after
date = newdf['Date Time, GMT+00:00']
speed = newdf['Wind Speed, mph']
speed *= 0.44704
gust = newdf['Gust Speed, mph']
gust *= 0.44704
winddir = newdf['Wind Direction']
# %% #making a plot of the charts
'''First (top chart) chart of wind speed'''

fig, ax = plt.subplots(ncols = 1, nrows = 2, figsize = (15, 10))
fig.suptitle('Anamometer data ', 
             fontsize=18, fontweight = 'bold')
ax[0].plot(range(len(date)), speed, 'r', label = 'Wind Speed, mph')
ax[0].legend(prop={'size': 10})
ax[0].set_xlim(0, len(date))
ax[0].set_xlabel('Time (Seconds)', fontsize = 18, fontweight = 'bold')
ax[0].set_ylabel('Wind Speed m/s', fontsize = 18, fontweight = 'bold')
ax[0].set_title('Wind Speed m/s', fontsize = 18, fontweight = 'bold')
'''Second chart of wind gusts'''
ax[1].plot(range(len(date)), gust, 'b', label = 'Wind Gust, mph')
ax[1].legend(prop={'size': 10})
ax[1].set_xlim(0, len(date))
ax[1].set_xlabel('Time (Seconds)', fontsize = 18, fontweight = 'bold')
ax[1].set_ylabel('Wind Gust m/s', fontsize = 18, fontweight = 'bold')
ax[1].set_title('Wind Gust m/s', fontsize = 18, fontweight = 'bold')
plt.tight_layout()
plt.show()

