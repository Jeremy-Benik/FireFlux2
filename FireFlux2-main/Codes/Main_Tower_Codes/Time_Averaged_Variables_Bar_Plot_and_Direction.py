'''This code takes the average of all data over certain time intervals and plots them at their
respective heights. the other plot is the wind direction compared to the other averages. Averages in this code are: 
4 minutes before and 4 minutes after the fire start (8min), 10 minutes from fire start, and 15 minutes from fire start'''
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 28 18:10:33 2021

@author: jeremy
"""
# %% reading in libraries
import pandas as pd
import matplotlib.pyplot as plt
import statistics as st
import math
# %%reading in date
df8 = pd.read_csv('/media/jeremy/Data/Fireflux2/Website_Docs/Main_Tower_Data/8_min.csv')
df10 = pd.read_csv('/media/jeremy/Data/Fireflux2/Website_Docs/Main_Tower_Data/10_min.csv')
df15 = pd.read_csv('/media/jeremy/Data/Fireflux2/Website_Docs/Main_Tower_Data/15_min.csv')
# %% Defining variables
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
# %% Defining variables for the bar plot
x_20_8 = ['ux_20_8', 'uy_20_8', 'uz_20_8']
x_10_8 = ['ux_10_8', 'uy_10_8', 'uz_10_8']
x_6_8 = ['ux_6_8', 'uy_6_8', 'uz_6_8']

x_20_10 = ['ux_20_10', 'uy_20_10', 'uz_20_10']
x_10_10 = ['ux_10_10', 'uy_10_10', 'uz_10_10']
x_6_10 = ['ux_6_10', 'uy_6_10', 'uz_6_10']

x_20_15 = ['ux_20_15', 'uy_20_15', 'uz_20_15']
x_10_15 = ['ux_10_15', 'uy_10_15', 'uz_10_15']
x_6_15 = ['ux_6_15', 'uy_6_15', 'uz_6_15']

y_20_8 = [ux_20_8, uy_20_8, uz_20_8]
y_10_8 = [ux_10_8, uy_10_8, uz_10_8]
y_6_8 = [ux_6_8, uy_6_8, uz_6_8]

y_20_10 = [ux_20_10, uy_20_10, uz_20_10]
y_10_10 = [ux_10_10, uy_10_10, uz_10_10]
y_6_10 = [ux_6_10, uy_6_10, uz_6_10]

y_20_15 = [ux_20_15, uy_20_15, uz_20_15]
y_10_15 = [ux_10_15, uy_10_15, uz_10_15]
y_6_15 = [ux_6_15, uy_6_15, uz_6_15]

# %% PLotting the directions
height_20 = [dir_20_15, dir_20_10, dir_20_8]
height_10 = [dir_10_15, dir_10_10, dir_10_8]
height_6 = [dir_6_15, dir_6_10, dir_6_8]
units_sold = (('20 Meters',height_20), ('10 Meters', height_10), ('6 Meters', height_6))

height = ['20m 15min avg', '20m 10min avg', '20m 8min avg', '10m 15min avg', '10m 10min avg', '10m 8min avg', 
          '6m 15min av]g', '6m 10min avg', '6m 8min avg']
x_pos_20 = [0, 1, 2]
x_pos_10 = [4, 5, 6]
x_pos_6 = [8, 9, 10]
x_pos = [0, 1, 2, 4, 5, 6, 8, 9, 10]
width1 = [1,1,1]



# %% Making a plot
fig, ax = plt.subplots(1, 2, figsize = (30, 20))

ax[0].bar('ux_20_15',ux_20_15, width = width1)
ax[0].bar('ux_20_10',ux_20_10, width = width1)
ax[0].bar('ux_20_8',ux_20_8, width = width1)
ax[0].bar('uy_20_15', uy_20_15, width = width1)
ax[0].bar('uy_20_10', uy_20_10, width = width1)
ax[0].bar('uy_20_8', uy_20_8, width = width1)

ax[0].bar('ux_10_15',ux_10_15, width = width1)
ax[0].bar('ux_10_10',ux_10_10, width = width1)
ax[0].bar('ux_10_8',ux_10_8, width = width1)
ax[0].bar('uy_10_15', uy_10_15, width = width1)
ax[0].bar('uy_10_10', uy_10_10, width = width1)
ax[0].bar('uy_10_8', uy_10_8, width = width1)

ax[0].bar('ux_6_15',ux_6_15, width = width1)
ax[0].bar('ux_6_10',ux_6_10, width = width1)
ax[0].bar('ux_6_8',ux_6_8, width = width1)
ax[0].bar('uy_6_15', uy_6_15, width = width1)
ax[0].bar('uy_6_10', uy_6_10, width = width1)
ax[0].bar('uy_6_8', uy_6_8, width = width1)

ax[0].set_ylabel('Wind Speed (m/s)', fontsize = 18, fontweight = 'bold')
ax[0].set_xlabel('Wind averaged at varying heights and times', fontsize = 18, fontweight = 'bold')
ax[0].set_title('Averaged wind Speeds at different times and heights for Main Tower', fontsize = 18, fontweight = 'bold')
ax[0].grid()
ax[0].legend(('ux_20_15', 'ux_20_10', 'ux_20_8', 'uy_20_15', 'uy_20_10', 'uy_20_8', 'ux_10_15', 'ux_10_10', 'ux_10_8', 
              'uy_10_15', 'uy_10_10', 'uy_10_8', 'ux_6_15', 'ux_6_10', 'ux_6_8', 'uy_6_15', 'uy_6_10', 'uy_6_8'))
ax[1].bar(x_pos_20, height_20, width = width1, color = ['blue', 'red', 'green'])
ax[1].bar(x_pos_10, height_10, width = width1, color = ['orange', 'purple', 'darkgreen'])
ax[1].bar(x_pos_6, height_6, width = width1, color = ['coral', 'yellow', 'gray'])
ax[1].set_xticks(x_pos, height)
ax[1].set_xlabel('Direction at Height (m) with Different Time Averaging', fontsize = 18, fontweight = 'bold')
ax[1].set_ylabel('Degrees', fontsize = 18, fontweight = 'bold')
ax[1].set_ylim(0, 360)
#plt.grid()
ax[1].set_title('Wind Spped direction At Different Heights Averaged at Different Times', fontsize = 18, fontweight = 'bold')
#ax[1].legend(('20m 15min avg', '20m 10min avg', '20m 8min avg', '10m 15min avg', '10m 10min avg', '10m 8min avg', 
#          '6m 15min avg', '6m 10min avg', '6m 8min avg'))
plt.tight_layout()
plt.show()


