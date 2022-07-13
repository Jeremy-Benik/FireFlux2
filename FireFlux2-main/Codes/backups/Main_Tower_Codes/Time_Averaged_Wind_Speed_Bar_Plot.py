'''This code creates a bar plot of the time averaged variables in the Main Tower Data, and plots them versus other time averaged variables
to see which time average would result in a more representative time average for the wind for the experiment.'''
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 30 09:52:51 2021

@author: jeremy
"""

# %% reading in libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statistics as st
import math
# %%reading in date
df4 = pd.read_csv('/media/jeremy/Data/Fireflux2/Website_Docs/Main_Tower_Data/4_min.csv')
df8 = pd.read_csv('/media/jeremy/Data/Fireflux2/Website_Docs/Main_Tower_Data/8_min.csv')
df10 = pd.read_csv('/media/jeremy/Data/Fireflux2/Website_Docs/Main_Tower_Data/10_min.csv')
df15 = pd.read_csv('/media/jeremy/Data/Fireflux2/Website_Docs/Main_Tower_Data/15_min.csv')
# %% Defining variables
#These are all the 4 minute file
ux_20_4 = df4['Ux_20m']
uy_20_4 = df4['Uy_20m']
uz_20_4 = df4['Uz_20m']

ux_10_4 = df4['Ux_10m']
uy_10_4 = df4['Uy_10m']
uz_10_4 = df4['Uz_10m']

ux_6_4 = df4['Ux_6m']
uy_6_4 = df4['Uy_6m']
uz_6_4 = df4['Uz_6m']

#These are all the 8 minute file
ux_20_8 = df8['Ux_20m']
uy_20_8 = df8['Uy_20m']
uz_20_8 = df8['Uz_20m']

ux_10_8 = df8['Ux_10m']
uy_10_8 = df8['Uy_10m']
uz_10_8 = df8['Uz_10m']

ux_6_8 = df8['Ux_6m']
uy_6_8 = df8['Uy_6m']
uz_6_8 = df8['Uz_6m']

#These are all the 10 minute file
ux_20_10 = df10['Ux_20m']
uy_20_10 = df10['Uy_20m']
uz_20_10 = df10['Uz_20m']

ux_10_10 = df10['Ux_10m']
uy_10_10 = df10['Uy_10m']
uz_10_10 = df10['Uz_10m']


ux_6_10 = df10['Ux_6m']
uy_6_10 = df10['Uy_6m']
uz_6_10 = df10['Uz_6m']
#These are all the 15 minute file
ux_20_15 = df15['Ux_20m']
uy_20_15 = df15['Uy_20m']
uz_20_15 = df15['Uz_20m']

ux_10_15 = df15['Ux_10m']
uy_10_15 = df15['Uy_10m']
uz_10_15 = df15['Uz_10m']

ux_6_15 = df15['Ux_6m']
uy_6_15 = df15['Uy_6m']
uz_6_15 = df15['Uz_6m']
# %% Averaging all them out
#These are for the 4 minute file
ux_20_4  = st.mean(ux_20_4)
uy_20_4  = st.mean(uy_20_4)
uz_20_4  = st.mean(uz_20_4)

ux_10_4  = st.mean(ux_10_4)
uy_10_4  = st.mean(uy_10_4)
uz_10_4  = st.mean(uz_10_4)

ux_6_4  = st.mean(ux_6_4)
uy_6_4  = st.mean(uy_6_4)
uz_6_4  = st.mean(uz_6_4)
#These are for the 8 minute file
ux_20_8  = st.mean(ux_20_8)
uy_20_8  = st.mean(uy_20_8)
uz_20_8  = st.mean(uz_20_8)

ux_10_8  = st.mean(ux_10_8)
uy_10_8  = st.mean(uy_10_8)
uz_10_8  = st.mean(uz_10_8)

ux_6_8  = st.mean(ux_6_8)
uy_6_8  = st.mean(uy_6_8)
uz_6_8  = st.mean(uz_6_8)

dir_20_8 = math.degrees(math.atan(uy_20_8/ux_20_8)) + 360
dir_10_8 = math.degrees(math.atan(uy_10_8/ux_10_8)) + 360
dir_6_8 = math.degrees(math.atan(uy_6_8/ux_6_8)) + 360
#these are the 10 minute file
ux_20_10  = st.mean(ux_20_10)
uy_20_10  = st.mean(uy_20_10)
uz_20_10  = st.mean(uz_20_10)

ux_10_10  = st.mean(ux_10_10)
uy_10_10  = st.mean(uy_10_10)
uz_10_10  = st.mean(uz_10_10)

ux_6_10  = st.mean(ux_6_10)
uy_6_10  = st.mean(uy_6_10)
uz_6_10  = st.mean(uz_6_10)

dir_20_10 = math.degrees(math.atan(uy_20_10/ux_20_10)) + 360
dir_10_10 = math.degrees(math.atan(uy_10_10/ux_10_10)) + 360
dir_6_10 = math.degrees(math.atan(uy_6_10/ux_6_10)) + 360
#these are the 15 minute file
ux_20_15  = st.mean(ux_20_15)
uy_20_15  = st.mean(uy_20_15)
uz_20_15  = st.mean(uz_20_15)

ux_10_15  = st.mean(ux_10_15)
uy_10_15  = st.mean(uy_10_15)
uz_10_15  = st.mean(uz_10_15)

ux_6_15  = st.mean(ux_6_15)
uy_6_15  = st.mean(uy_6_15)
uz_6_15  = st.mean(uz_6_15)

dir_20_15 = math.degrees(math.atan(uy_20_15/ux_20_15)) + 360
dir_10_15 = math.degrees(math.atan(uy_10_15/ux_10_15)) + 360
dir_6_15 = math.degrees(math.atan(uy_6_15/ux_6_15)) + 360
# %% Calculatg wind speeds
w_20_4 = np.sqrt((ux_20_4 ** 2) + (uy_20_4 ** 2)) #wind speed at 20 meters 8 min average
w_10_4 = np.sqrt((ux_10_4 ** 2) + (uy_10_4 ** 2)) #wind speed at 10 meters 8 min average
w_6_4 = np.sqrt((ux_6_4 ** 2) + (uy_6_4 ** 2)) #wind speed at 6 meters 8 min average


w_20_8 = np.sqrt((ux_20_8 ** 2) + (uy_20_8 ** 2)) #wind speed at 20 meters 8 min average
w_10_8 = np.sqrt((ux_10_8 ** 2) + (uy_10_8 ** 2)) #wind speed at 10 meters 8 min average
w_6_8 = np.sqrt((ux_6_8 ** 2) + (uy_6_8 ** 2)) #wind speed at 6 meters 8 min average


w_20_10 = np.sqrt((ux_20_10 ** 2) + (uy_20_10 ** 2)) #wind speed at 20 meters 8 min average
w_10_10 = np.sqrt((ux_10_10 ** 2) + (uy_10_10 ** 2)) #wind speed at 10 meters 8 min average
w_6_10 = np.sqrt((ux_6_10 ** 2) + (uy_6_10 ** 2)) #wind speed at 6 meters 8 min average


w_20_15 = np.sqrt((ux_20_15 ** 2) + (uy_20_15 ** 2)) #wind speed at 20 meters 8 min average
w_10_15 = np.sqrt((ux_10_15 ** 2) + (uy_10_15 ** 2)) #wind speed at 10 meters 8 min average
w_6_15 = np.sqrt((ux_6_15 ** 2) + (uy_6_15 ** 2)) #wind speed at 6 meters 8 min average


w_8 = [w_20_8, w_10_8, w_6_8]
w_10 = [w_20_10, w_10_10, w_6_10]
w_15 = [w_20_15, w_10_15, w_6_15]

height_20 = [w_20_15, w_20_10, w_20_8, w_20_4]
height_10 = [w_10_15, w_10_10, w_10_8, w_10_4]
height_6 = [w_6_15, w_6_10, w_6_8, w_6_4]
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

# %%
ax.barh(x_pos_6, height_20, height = 1, color = ['red', 'blue', 'green', 'yellow'])
x = ax.barh(x_pos_20, height_6, height = 1, color = ['red', 'blue', 'green', 'yellow'])
ax.barh(x_pos_10, height_10, height = 1, color = ['red', 'blue', 'green', 'yellow'])

ax.set_xlabel('Wind Speed (m/s)', fontsize = 18, fontweight = 'bold')
ax.set_ylabel('Height (m)', fontsize = 18, fontweight = 'bold')
#ax.set_yticks(x_pos, height)
ax.set_yticks(h_pos, ['6 Meters', '10 Meters', '20 Meters'])
leg = [name_8, name_10, name_15]
ax.set_title('Wind speeds at Certain Heights on the Main Tower Averaged Over 15min, 10min, 8 min, and 4 minutes', fontsize = 18, fontweight = 'bold')
ax.legend(x, ['15 Minute Average', '10 Minute Average', '8 Minute Average', '4 Minutes'])
#ax.grid()
plt.tight_layout()
plt.grid(True, axis = 'x')
plt.show()









