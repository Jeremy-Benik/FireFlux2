'''This file loops through all the anemometer files, truncates the data for 30 min before the fire and 30 minutes after the fire and plots them'''
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 19 11:23:59 2021

@author: Jeremy Benik
"""
''' This code iterates through all the files inside the ff2 anamometers and plots the data from them. The files
include date, wind speed in mph, wind gusts, and wind direction. From there I used a metpy library
to then split the wind into u and v vectors and plotted those. There are 4 graphs per page. If you want to save the plots, uncomment 
the plt.savefig. '''
# %% Importing necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import datetime
import glob
from metpy.units import units
import metpy.calc as mpcalc
# %% Going through one file to see what is inside of it, then will probably iteratre through all files
path = r'../../Data/FF2Anemometers/' #setting the path to my files
#explain what simplification I have done in clickup. 
filenames = glob.glob(path + "/*.csv") #setting the path and saying I want to iterate through my .csv files
# %%
for filename in filenames:
    df1 = pd.read_csv((filename), parse_dates=['Date Time, GMT+00:00'], 
                        encoding = 'unicode_escape', skiprows = (0, 2))
    df = df1[df1['Date Time, GMT+00:00'].between('2013-01-30 14:34:00', '2013-01-30  15:34:00')]
    for _,g in df.groupby('Date Time, GMT+00:00'):
        if len(g) > 1:
            seconds = np.linspace(0, 59, len(g))
            df.loc[g.index, 'Date Time, GMT+00:00'] = [t+datetime.timedelta(seconds=seconds[i]) for i,t in enumerate(g['Date Time, GMT+00:00'])]
    #df = df.groupby('Date Time, GMT+00:00').mean().reset_index()
    date = df['Date Time, GMT+00:00']
    speed = df['Wind Speed, mph'].values * units.mph
    speed *= 0.44704
    gust = df['Gust Speed, mph']
    gust *= 0.44704
    wind_dir = df.iloc[:,4].values * units.degrees
    u, v = mpcalc.wind_components(speed, wind_dir)
    fig, ax = plt.subplots(ncols = 1, nrows = 4, figsize = (18, 10))
    ax[0].plot(date, speed, 'r', label='Wind Speed (kts)')
    ax[0].legend(prop={'size': 10})
    #ax[0].set_xlim(0, len(date))
    ax[0].set_xlabel('Date and Time', fontsize=18, fontweight='bold')
    ax[0].set_ylabel('Wind Speed (kts)', fontsize=18, fontweight='bold')
    ax[0].set_title(f"Wind Speed for File {filename[57:-4][:]}.csv", fontsize=18, fontweight='bold')
    ax[1].plot(date, gust, 'b', label='Wind Gust (kts)')
    ax[1].legend(prop={'size': 10})
    ax[1].set_xlabel('Date and Time', fontsize=18, fontweight='bold')
    ax[1].set_ylabel('Wind Gust (kts)', fontsize=18, fontweight='bold')
    #ax[1].set_xlim(0, len(date))
    ax[1].set_title(f"Wind Gust for File {filename[57:-4][:]}.csv", fontsize=18, fontweight='bold')
    ax[2].plot(date, u, 'green', label = 'U wind')
    ax[2].set_xlabel('Date and Time', fontsize=18, fontweight='bold')
    ax[2].set_ylabel('U Wind (kts)', fontsize=18, fontweight='bold')
    ax[2].set_title(f"U Wind Speed for File {filename[57:-4][:]}.csv", fontsize=18, fontweight='bold')
    #ax[2].set_xlim(0, len(date))
    ax[2].legend()
    ax[3].plot(date, v, '#9A32CD', label = 'V wind')
    ax[3].set_xlabel('Date and Time', fontsize=18, fontweight='bold')
    #ax[3].set_xlim(0, len(date))
    ax[3].set_ylabel('V Wind (kts)', fontsize=18, fontweight='bold')
    ax[3].set_title(f"V Wind Speed for File {filename[57:-4][:]}.csv", fontsize=18, fontweight='bold')
    ax[3].legend()
    plt.tight_layout()
    #plt.savefig(f"D:/Fireflux2/figures/Wind_Profiles/Wind_Images_csv{filename[41:-4][:]}_v2.png")
    plt.show()
    

