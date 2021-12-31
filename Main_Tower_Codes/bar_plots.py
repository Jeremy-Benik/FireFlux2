#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 28 10:57:24 2021

@author: jeremy
"""
# %% Importing libraries
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import metpy.calc
from metpy.units import units
import statistics as st
import math
# %% Reading in the data using pandas, this is for 8 minutes in total ( 4 before, 4 after)
df1 = pd.read_csv('/media/jeremy/Data/Fireflux2/Website_Docs/Main_Tower_Data/Proc_FF2_10HzMTdespiked_rotated.csv', parse_dates=['TIMESTAMP'], skiprows = (0, 2, 3))
#this reads in the dataframe and parses the dates. I also skip unecessary rows. This csv is modified by removing the record column and 
#moving the other columns over
# Calculating the time for 4 minutes before the fire start so I can average them all
df = df1.truncate(before= np.where(df1['TIMESTAMP'] == '1/30/2013  15:00:00')[0][80], 
                    after=np.where(df1['TIMESTAMP'] == '1/30/2013  15:08:00')[0][80])

time = df['TIMESTAMP']
ux20 = df['Ux_20m'].values * units('m/s')
uy20 = df['Uy_20m'].values * units('m/s')
uz20 = df['Uz_20m'].values * units('m/s')
ts20 = df['Ts_20m']
ux10 = df['Ux_10m'].values * units('m/s')
uy10 = df['Uy_10m'].values * units('m/s')
uz10 = df['Uz_10m'].values * units('m/s')
ts10 = df['Ts_10m']
ux6 = df['Ux_6m'].values * units('m/s')
uy6 = df['Uy_6m'].values * units('m/s')
uz6 = df['Uz_6m'].values * units('m/s')
ts6 = df['Ts_6m']
ux201 = st.mean(ux20)
uy201 = st.mean(uy20)
uz201 = st.mean(uz20)

ux101 = st.mean(ux10)
uy101 = st.mean(uy10)
uz101 = st.mean(uz10)

ux61 = st.mean(ux6)
uy61 = st.mean(uy6)
uz61 = st.mean(uz6)

dir_201 = math.degrees(math.atan(ux201/uy201)) + 360
dir_101 = math.degrees(math.atan(ux101/uy101)) + 360
dir_61 = math.degrees(math.atan(ux61/uy61)) + 360

# %% Timestamp 2 10 minutes after fire started
df1 = pd.read_csv('/media/jeremy/Data/Fireflux2/Website_Docs/Main_Tower_Data/Proc_FF2_10HzMTdespiked_rotated.csv', parse_dates=['TIMESTAMP'], skiprows = (0, 2, 3))
#this reads in the dataframe and parses the dates. I also skip unecessary rows. This csv is modified by removing the record column and 
#moving the other columns over
# Calculating the time for 4 minutes before the fire start so I can average them all
df = df1.truncate(before= np.where(df1['TIMESTAMP'] == '1/30/2013  15:04:00')[0][80], 
                    after=np.where(df1['TIMESTAMP'] == '1/30/2013  15:14:00')[0][80])
time = df['TIMESTAMP']
ux20 = df['Ux_20m'].values * units('m/s')
uy20 = df['Uy_20m'].values * units('m/s')
uz20 = df['Uz_20m'].values * units('m/s')
ts20 = df['Ts_20m']
ux10 = df['Ux_10m'].values * units('m/s')
uy10 = df['Uy_10m'].values * units('m/s')
uz10 = df['Uz_10m'].values * units('m/s')
ts10 = df['Ts_10m']
ux6 = df['Ux_6m'].values * units('m/s')
uy6 = df['Uy_6m'].values * units('m/s')
uz6 = df['Uz_6m'].values * units('m/s')
ts6 = df['Ts_6m']
ux202 = st.mean(ux20)
uy202 = st.mean(uy20)
uz202 = st.mean(uz20)

ux102 = st.mean(ux10)
uy102 = st.mean(uy10)
uz102 = st.mean(uz10)

ux62 = st.mean(ux6)
uy62 = st.mean(uy6)
uz62 = st.mean(uz6)

dir_202 = math.degrees(math.atan(ux201/uy201)) + 360
dir_102 = math.degrees(math.atan(ux101/uy101)) + 360
dir_62 = math.degrees(math.atan(ux61/uy61)) + 360

# %% Timestamp 3 15 minutes after fire started
df1 = pd.read_csv('/media/jeremy/Data/Fireflux2/Website_Docs/Main_Tower_Data/Proc_FF2_10HzMTdespiked_rotated.csv', parse_dates=['TIMESTAMP'], skiprows = (0, 2, 3))
#this reads in the dataframe and parses the dates. I also skip unecessary rows. This csv is modified by removing the record column and 
#moving the other columns over
# Calculating the time for 4 minutes before the fire start so I can average them all
df = df1.truncate(before= np.where(df1['TIMESTAMP'] == '1/30/2013  15:04:00')[0][80], 
                    after=np.where(df1['TIMESTAMP'] == '1/30/2013  15:19:00')[0][80])
time = df['TIMESTAMP']
ux20 = df['Ux_20m'].values * units('m/s')
uy20 = df['Uy_20m'].values * units('m/s')
uz20 = df['Uz_20m'].values * units('m/s')
ts20 = df['Ts_20m']
ux10 = df['Ux_10m'].values * units('m/s')
uy10 = df['Uy_10m'].values * units('m/s')
uz10 = df['Uz_10m'].values * units('m/s')
ts10 = df['Ts_10m']
ux6 = df['Ux_6m'].values * units('m/s')
uy6 = df['Uy_6m'].values * units('m/s')
uz6 = df['Uz_6m'].values * units('m/s')
ts6 = df['Ts_6m']
ux203 = st.mean(ux20)
uy203 = st.mean(uy20)
uz203 = st.mean(uz20)

ux103 = st.mean(ux10)
uy103 = st.mean(uy10)
uz103 = st.mean(uz10)

ux63 = st.mean(ux6)
uy63 = st.mean(uy6)
uz63 = st.mean(uz6)

dir_203 = math.degrees(math.atan(ux201/uy201)) + 360
dir_103 = math.degrees(math.atan(ux101/uy101)) + 360
dir_63 = math.degrees(math.atan(ux61/uy61)) + 360


# %%
x = ['ux201', 'uy201', 'uz201', 'ux102', 'uy102', 'uz102', 'ux63', 'uy63', 'uz63']
colors = {'ux201': 'blue', 'uy201' : 'red', 'uz201' : 'darkgreen', 'ux102': 'purple', 'uy102' : 'coral', 'uz102' : 'yellow', 
          'ux63': 'fuchsia', 'uy63' : 'limegreen', 'uz63' : 'maroon'}
labels = list(colors.keys())
handles = [plt.Rectangle((0,0),1,1, color=colors[label]) for label in labels]
y = [round(ux201, 2), round(uy201, 2), round(uz201, 2), round(ux102, 2), round(uy102, 2), round(uz102, 2)
     , round(ux63, 2), round(uy63, 2), round(uz63, 2)]


fig, ax = plt.subplots(1, 2, figsize = (12, 15))
plt.suptitle('winds for 4 minutes before and 4 minutes after with direction', fontsize = 18, fontweight = 'bold')
ax[0].bar(x, y, color = ['blue', 'red', 'darkgreen', 'purple', 'coral', 'yellow', 'fuchsia', 'limegreen', 'maroon'])
ax[0].set_xlabel('Wind Variables', fontsize = 18, fontweight = 'bold')
ax[0].set_ylabel('Averaged Speed (m/s)', fontsize = 18, fontweight = 'bold')
ax[0].grid()
ax[0].set_title('Averaged Winds', fontsize = 18, fontweight = 'bold')
ax[0].legend(handles, labels)

names = ['direction 20m', 'direction 10m', 'direction 6m']
colors = {'direction_20m' : 'red', 'direction_10m' : 'blue', 'direction_6m' : 'green'}
direction = [dir_20, dir_10, dir_6]
labels = list(colors.keys())
handles = [plt.Rectangle((0,0),1,1, color=colors[label]) for label in labels]
ax[1].bar(names, direction, color = ['red', 'blue', 'green'])
ax[1].set_ylabel('Direction (Degrees)', fontsize = 18, fontweight = 'bold')
ax[1].set_xlabel('Levels (20m, 10m, 6m)', fontsize = 18, fontweight = 'bold')
ax[1].grid()
ax[1].set_ylim(0, 360)
ax[1].set_title('Direction', fontsize = 18, fontweight = 'bold')
ax[1].legend(handles, labels)
plt.tight_layout()
plt.show()
# %% Reading in the data using pandas, this is for 8 minutes in total ( 4 before, 4 after)
df1 = pd.read_csv('/media/jeremy/Data/Fireflux2/Website_Docs/Main_Tower_Data/Proc_FF2_10HzMTdespiked_rotated.csv', parse_dates=['TIMESTAMP'], skiprows = (0, 2, 3))
#this reads in the dataframe and parses the dates. I also skip unecessary rows. This csv is modified by removing the record column and 
#moving the other columns over
# Calculating the time for 4 minutes before the fire start so I can average them all
df = df1.truncate(before= np.where(df1['TIMESTAMP'] == '1/30/2013  15:04:00')[0][80], 
                    after=np.where(df1['TIMESTAMP'] == '1/30/2013  15:14:00')[0][80])
time = df['TIMESTAMP']
ux20 = df['Ux_20m'].values * units('m/s')
uy20 = df['Uy_20m'].values * units('m/s')
uz20 = df['Uz_20m'].values * units('m/s')
ts20 = df['Ts_20m']
ux10 = df['Ux_10m'].values * units('m/s')
uy10 = df['Uy_10m'].values * units('m/s')
uz10 = df['Uz_10m'].values * units('m/s')
ts10 = df['Ts_10m']
ux6 = df['Ux_6m'].values * units('m/s')
uy6 = df['Uy_6m'].values * units('m/s')
uz6 = df['Uz_6m'].values * units('m/s')
ts6 = df['Ts_6m']
ux20 = st.mean(ux20)
uy20 = st.mean(uy20)
uz20 = st.mean(uz20)

ux10 = st.mean(ux10)
uy10 = st.mean(uy10)
uz10 = st.mean(uz10)

ux6 = st.mean(ux6)
uy6 = st.mean(uy6)
uz6 = st.mean(uz6)

dir_20 = math.degrees(math.atan(ux20/uy20)) + 360
dir_10 = math.degrees(math.atan(ux10/uy10)) + 360
dir_6 = math.degrees(math.atan(ux6/uy6)) + 360
# %%
x = ['ux20', 'uy20', 'uz20', 'ux10', 'uy10', 'uz10', 'ux6', 'uy6', 'uz6']
colors = {'ux20': 'blue', 'uy20' : 'red', 'uz20' : 'darkgreen', 'ux10': 'purple', 'uy10' : 'coral', 'uz10' : 'yellow', 
          'ux6': 'fuchsia', 'uy6' : 'limegreen', 'uz6' : 'maroon'}
labels = list(colors.keys())
handles = [plt.Rectangle((0,0),1,1, color=colors[label]) for label in labels]
y = [round(ux20, 2), round(uy20, 2), round(uz20, 2), round(ux10, 2), round(uy10, 2), round(uz10, 2)
     , round(ux6, 2), round(uy6, 2), round(uz6, 2)]


fig, ax = plt.subplots(1, 2, figsize = (12, 15))
plt.suptitle('winds for 10 minutes after with direction', fontsize = 18, fontweight = 'bold')
ax[0].bar(x, y, color = ['blue', 'red', 'darkgreen', 'purple', 'coral', 'yellow', 'fuchsia', 'limegreen', 'maroon'])
ax[0].set_xlabel('Wind Variables', fontsize = 18, fontweight = 'bold')
ax[0].set_ylabel('Averaged Speed (m/s)', fontsize = 18, fontweight = 'bold')
ax[0].grid()
ax[0].set_title('Averaged Winds', fontsize = 18, fontweight = 'bold')
ax[0].legend(handles, labels)

names = ['direction 20m', 'direction 10m', 'direction 6m']
colors = {'direction_20m' : 'red', 'direction_10m' : 'blue', 'direction_6m' : 'green'}
direction = [dir_20, dir_10, dir_6]
labels = list(colors.keys())
handles = [plt.Rectangle((0,0),1,1, color=colors[label]) for label in labels]
ax[1].bar(names, direction, color = ['red', 'blue', 'green'])
ax[1].set_ylabel('Direction (Degrees)', fontsize = 18, fontweight = 'bold')
ax[1].set_xlabel('Levels (20m, 10m, 6m)', fontsize = 18, fontweight = 'bold')
ax[1].grid()
ax[1].set_ylim(0, 360)
ax[1].set_title('Direction', fontsize = 18, fontweight = 'bold')
ax[1].legend(handles, labels)
plt.tight_layout()
plt.show()
# %% Reading in the data using pandas, this is for 8 minutes in total ( 4 before, 4 after)
df1 = pd.read_csv('/media/jeremy/Data/Fireflux2/Website_Docs/Main_Tower_Data/Proc_FF2_10HzMTdespiked_rotated.csv', parse_dates=['TIMESTAMP'], skiprows = (0, 2, 3))
#this reads in the dataframe and parses the dates. I also skip unecessary rows. This csv is modified by removing the record column and 
#moving the other columns over
# Calculating the time for 4 minutes before the fire start so I can average them all
df = df1.truncate(before= np.where(df1['TIMESTAMP'] == '1/30/2013  15:04:00')[0][80], 
                    after=np.where(df1['TIMESTAMP'] == '1/30/2013  15:19:00')[0][80])
time = df['TIMESTAMP']
ux20 = df['Ux_20m'].values * units('m/s')
uy20 = df['Uy_20m'].values * units('m/s')
uz20 = df['Uz_20m'].values * units('m/s')
ts20 = df['Ts_20m']
ux10 = df['Ux_10m'].values * units('m/s')
uy10 = df['Uy_10m'].values * units('m/s')
uz10 = df['Uz_10m'].values * units('m/s')
ts10 = df['Ts_10m']
ux6 = df['Ux_6m'].values * units('m/s')
uy6 = df['Uy_6m'].values * units('m/s')
uz6 = df['Uz_6m'].values * units('m/s')
ts6 = df['Ts_6m']
ux20 = st.mean(ux20)
uy20 = st.mean(uy20)
uz20 = st.mean(uz20)

ux10 = st.mean(ux10)
uy10 = st.mean(uy10)
uz10 = st.mean(uz10)

ux6 = st.mean(ux6)
uy6 = st.mean(uy6)
uz6 = st.mean(uz6)

dir_20 = math.degrees(math.atan(ux20/uy20)) + 360
dir_10 = math.degrees(math.atan(ux10/uy10)) + 360
dir_6 = math.degrees(math.atan(ux6/uy6)) + 360
# %%
x = ['ux20', 'uy20', 'uz20', 'ux10', 'uy10', 'uz10', 'ux6', 'uy6', 'uz6']
colors = {'ux20': 'blue', 'uy20' : 'red', 'uz20' : 'darkgreen', 'ux10': 'purple', 'uy10' : 'coral', 'uz10' : 'yellow', 
          'ux6': 'fuchsia', 'uy6' : 'limegreen', 'uz6' : 'maroon'}
labels = list(colors.keys())
handles = [plt.Rectangle((0,0),1,1, color=colors[label]) for label in labels]
y = [round(ux20, 2), round(uy20, 2), round(uz20, 2), round(ux10, 2), round(uy10, 2), round(uz10, 2)
     , round(ux6, 2), round(uy6, 2), round(uz6, 2)]


fig, ax = plt.subplots(1, 2, figsize = (12, 15))
plt.suptitle('winds for 15 minutes after with direction', fontsize = 18, fontweight = 'bold')
ax[0].bar(x, y, color = ['blue', 'red', 'darkgreen', 'purple', 'coral', 'yellow', 'fuchsia', 'limegreen', 'maroon'])
ax[0].set_xlabel('Wind Variables', fontsize = 18, fontweight = 'bold')
ax[0].set_ylabel('Averaged Speed (m/s)', fontsize = 18, fontweight = 'bold')
ax[0].grid()
ax[0].set_title('Averaged Winds', fontsize = 18, fontweight = 'bold')
ax[0].legend(handles, labels)

names = ['direction 20m', 'direction 10m', 'direction 6m']
colors = {'direction_20m' : 'red', 'direction_10m' : 'blue', 'direction_6m' : 'green'}
direction = [dir_20, dir_10, dir_6]
labels = list(colors.keys())
handles = [plt.Rectangle((0,0),1,1, color=colors[label]) for label in labels]
ax[1].bar(names, direction, color = ['red', 'blue', 'green'])
ax[1].set_ylabel('Direction (Degrees)', fontsize = 18, fontweight = 'bold')
ax[1].set_xlabel('Levels (20m, 10m, 6m)', fontsize = 18, fontweight = 'bold')
ax[1].grid()
ax[1].set_ylim(0, 360)
ax[1].set_title('Direction', fontsize = 18, fontweight = 'bold')
ax[1].legend(handles, labels)
plt.tight_layout()
plt.show()

