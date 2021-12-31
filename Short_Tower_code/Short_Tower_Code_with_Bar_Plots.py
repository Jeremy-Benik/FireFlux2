# -*- coding: utf-8 -*-
"""
Created on Mon Dec 27 09:22:29 2021

@author: Jeremy Benik
"""
# %% Importing necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import glob
from metpy.units import units
import statistics as st
import math
# %% importing the data using glob so I can read all the files at once
path = r'/media/jeremy/Data/Fireflux2/Website_Docs/Short_Tower_Data'
filenames = glob.glob(path + "/*.csv")
# %% making a for loop to iterate through all the files and make plots of them all at once
n = 5 #this is a 5 second average of the data
for filename in filenames:
    df1 = pd.read_csv((filename), parse_dates = ['TIMESTAMP'])
    df = df1.truncate(before= np.where(df1['TIMESTAMP'] == '1/30/2013  15:04:00')[0][3], 
                        after=np.where(df1['TIMESTAMP'] == '1/30/2013  15:34:00')[0][3])
    time = df['TIMESTAMP']
    u = df['u']
    v = df['v']
    w = df['w']
    t = df['t']
    time2 = np.arange(0, len(time)) / 60
    fig, ax = plt.subplots(4, 1, figsize = (15, 10))
    plt.suptitle(f"Short tower plots for the {filename[-20]} Tower", fontsize = 18, fontweight = 'bold')
    ax[0].plot(time2, u, 'blue', label = 'U wind')
    ax[0].plot(time2, u.rolling(window = n).mean(), 'black', label = 'Avg. U winds', linestyle = '-')
    ax[0].legend(prop={'size': 6})
    ax[0].set_title(f"U wind for the {filename[-20]} Tower", fontsize = 16, fontweight = 'bold')
    ax[0].set_xlim(0, 30)
    ax[0].set_xlabel('Time (Minutes)', fontsize = 16, fontweight = 'bold')
    ax[0].set_ylabel('U wind (m/s)', fontsize = 16, fontweight = 'bold')
    ax[1].plot(time2, v, 'green', label = 'V wind')
    ax[1].plot(time2, v.rolling(window = n).mean(), 'black', label = 'Avg. V winds', linestyle = '-')
    ax[1].legend(prop={'size': 6})
    ax[1].set_title(f"V wind for the {filename[-20]} Tower", fontsize = 16, fontweight = 'bold')
    ax[1].set_xlim(0, 30)
    ax[1].set_xlabel('Time (Minutes)', fontsize = 16, fontweight = 'bold')
    ax[1].set_ylabel('V wind (m/s)', fontsize = 16, fontweight = 'bold')
    ax[2].plot(time2, w, 'red', label = 'W wind')
    ax[2].plot(time2, w.rolling(window = n).mean(), 'black', label = 'Avg. W winds', linestyle = '-')
    ax[2].legend(prop={'size': 6})
    ax[2].set_title(f"W wind for the {filename[-20]} Tower", fontsize = 16, fontweight = 'bold')
    ax[2].set_xlim(0, 30)
    ax[2].set_xlabel('Time (Minutes)', fontsize = 16, fontweight = 'bold')
    ax[2].set_ylabel('W wind (m/s)', fontsize = 16, fontweight = 'bold')
    ax[3].plot(time2, t, 'green', label = 'Temperature$^\circ$C')
    ax[3].plot(time2, t.rolling(window = n).mean(), 'black', label = 'Avg. Temperature', linestyle = '-')
    ax[3].legend(prop={'size': 6})
    ax[3].set_title(f"Temperature for the {filename[-20]} Tower", fontsize = 16, fontweight = 'bold')
    ax[3].set_xlim(0, 30)
    ax[3].set_xlabel('Time (Minutes)', fontsize = 16, fontweight = 'bold')
    ax[3].set_ylabel('Temperature$^\circ$C', fontsize = 16, fontweight = 'bold')
    plt.tight_layout()
    plt.show()
    # %%
    df1 = pd.read_csv((filename), parse_dates = ['TIMESTAMP'])
    df4 = df1.truncate(before= np.where(df1['TIMESTAMP'] == '1/30/2013  15:00:00')[0][3], 
                        after=np.where(df1['TIMESTAMP'] == '1/30/2013  15:04:00')[0][3])
    df8 = df1.truncate(before= np.where(df1['TIMESTAMP'] == '1/30/2013  15:00:00')[0][3], 
                        after=np.where(df1['TIMESTAMP'] == '1/30/2013  15:08:00')[0][3])
    df10 = df1.truncate(before= np.where(df1['TIMESTAMP'] == '1/30/2013  15:04:00')[0][3], 
                        after=np.where(df1['TIMESTAMP'] == '1/30/2013  15:14:00')[0][3])
    df15 = df1.truncate(before= np.where(df1['TIMESTAMP'] == '1/30/2013  15:04:00')[0][3], 
                        after=np.where(df1['TIMESTAMP'] == '1/30/2013  15:19:00')[0][3])
    u4 = df4['u']
    v4 = df4['v']
    w4 = df4['w']
    
    u4  = st.mean(u4)
    v4  = st.mean(v4)
    w4  = st.mean(w4)
    
    u8 = df8['u']
    v8 = df8['v']
    w8 = df8['w']
    
    u8  = st.mean(u8)
    v8  = st.mean(v8)
    w8  = st.mean(w8)
    
    u10 = df10['u']
    v10 = df10['v']
    w10 = df10['w']
    
    u10  = st.mean(u10)
    v10  = st.mean(v10)
    w10  = st.mean(w10)
    
    u15 = df15['u']
    v15 = df15['v']
    w15 = df15['w']
    
    u15  = st.mean(u15)
    v15  = st.mean(v15)
    w15  = st.mean(w15)
    
    w_4 = np.sqrt((u4 ** 2) + (v4 ** 2))
    w_8 = np.sqrt((u8 ** 2) + (v8 ** 2))
    w_10 = np.sqrt((u10 ** 2) + (v10 ** 2))
    w_15 = np.sqrt((u15 ** 2) + (v15 ** 2))
    
    name_8 = 'Wind Speed 20m 8min avg', 'Wind Speed 10m 8min avg', 'Wind Speed 6m 8min avg'
    name_10 = 'Wind Speed 20m 10min avg', 'Wind Speed 10m 10min avg', 'Wind Speed 6m 10min avg'
    name_15 = 'Wind Speed 20m 15min avg', 'Wind Speed 10m 15min avg', 'Wind Speed 6m 15min avg'

    height_name_20 = ['20m 15min avg', '20m 10min avg', '20m 8min avg']
    height_name_10 = ['10m 15min avg', '10m 10min avg', '10m 8min avg']
    height_name_6 = ['6m 15min avg', '6m 10min avg', '6m 8min avg']
    fig, ax = plt.subplots(1, 1, figsize = (20, 12))

    height = ['20m 15min avg', '20m 10min avg', '20m 8min avg', '10m 15min avg', '10m 10min avg', '10m 8min avg', 
              '6m 15min av]g', '6m 10min avg', '6m 8min avg']
    x_pos_20 = [0, 1, 2, 3]
    x_pos_10 = [5, 6, 7, 8]
    x_pos_6 = [10, 11, 12, 13]
    x_pos = [0, 1, 2, 3, 5, 6, 7, 8, 10, 11, 12, 13]
    h_pos = [1.5, 6.5, 11.5]
    width1 = [1,1,1]


    ax.barh('4 minute Average', w_4, color = 'yellow')
    ax.barh('8 minute Average', w_8, color = 'green')
    ax.barh('10 minute Average', w_10, color = 'blue')
    ax.barh('15 Minute Average', w_15, color = 'red')
    ax.set_xlabel('Wind Speed (m/s)', fontsize = 16, fontweight = 'bold')
    ax.set_ylabel('Time Averaged (Minutes)', fontsize = 16, fontweight = 'bold')
    ax.set_title(f'Wind Speeds For {filename[-20]} Tower Averaged at 4 Min, 8min, 10min, and 15min', fontsize = 16, fontweight = 'bold')
    ax.legend(['4 minute Average', '8 minute Average', '10 minute Average', '15 minute Average'])
    plt.tight_layout()
    plt.grid(True, axis = 'x')
    plt.show()
    print(f'FILE {filename[-20]}')
    print(u15, v15, w15, '|', u10, v10, w10, '|', u8, v8, w8, '|', u4, v4, w4)
    print()
    print(w_15,"\n",w_10,"\n",w_8,"\n",w_4)
    print('NEW LINE')
    
    
    