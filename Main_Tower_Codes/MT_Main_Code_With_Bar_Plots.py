# -*- coding: utf-8 -*-
"""
Created on Tue Dec 21 15:39:50 2021

@author: Jeremy Benik
"""
'''This code combines the previous codes into one code, the first section of this code
will truncate the file using the truncate function, which will then be saved into a new variable named
df, using df I will then make plots of the data. The csv file has been modified slightly 
by removing the record column'''
# %% Importing necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import metpy.calc
from metpy.units import units
import statistics as st
import math
# %% This section of the code will read in the dataframe as df1 and it will be truncated based on
#5 minutes before the fire started, and 30 minutes after the fire started
#Since the fire started at 15:04:08, and the data is 10hz, I indexed to the 8th second in the file
df1 = pd.read_csv('/media/jeremy/Data/Fireflux2/Website_Docs/Main_Tower_Data/Proc_FF2_10HzMTdespiked_rotated.csv', parse_dates=['TIMESTAMP'], skiprows = (0, 2, 3))
#this reads in the dataframe and parses the dates. I also skip unecessary rows. This csv is modified by removing the record column and 
#moving the other columns over
df = df1.truncate(before= np.where(df1['TIMESTAMP'] == '1/30/2013  15:00:00')[0][0], 
                    after=np.where(df1['TIMESTAMP'] == '1/30/2013  15:34:00')[0][79])
#this truncates the dataframe down to the time at which we want (start time and 30 minutes after the ignition point)
#By using the timestamp to navigate and truncate the data, this can be used with multiple files assuming the same time format
#this finds where the timestamp equals that time, then indexes to the specific number of it. the [79] is the 8th second of 15:34:00
#Now df is the main dataframe that can be used to start plotting
# %% Defining variables to make life easier
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
# %% Finding where the fire start is, then adding a line there to indicate it. Not sure if this is necessary
#but I think it may make the graphs look nice. I'll use the other code first to not mess with this one much. 
# %% This graph is all the data over the 35 minute time interval, and the black lines are the averaged time
#over 5 seconds. To change the average time, change the value of n to something else
#keep in mind that this is 10hz
n = 50
time2 = np.arange(0, len(time)) / 10
fig, ax = plt.subplots(4, 3, figsize = (20, 10))
fig.suptitle('35 minutes of data from 15:00 CST, to start of fire at 15:04, then 30 minutes of data after that', fontsize=18, fontweight = 'bold')
ax[0, 0].plot(time2, ux20, 'r', label = 'ux20m winds')
ax[0, 0].plot(time2, ux20.rolling(window = n).mean(), 'black', label = 'Avg. ux20m winds', linestyle = '-')
ax[0, 0].set_title('ux20 winds vs time(s)', fontsize = 18, fontweight = 'bold')
ax[0, 0].set_ylabel('Speed (m/s)', fontsize = 18, fontweight = 'bold')
ax[0, 0].set_xlabel('Time (seconds)', fontsize = 18, fontweight = 'bold')
ax[0, 0].legend(prop={'size': 6})
ax[1, 0].plot(time2, uy20, 'blue', label = 'uy20m winds')
ax[1, 0].plot(time2, uy20.rolling(window = n).mean(), 'black', label = 'Avg. uy20m winds', linestyle = '-')
ax[1, 0].legend(prop={'size': 6})
ax[1, 0].set_xlabel('Time (seconds)', fontsize = 18, fontweight = 'bold')
ax[1, 0].set_ylabel('Speed (m/s)', fontsize = 18, fontweight = 'bold')
ax[1, 0].set_title('uy20 winds vs time (s)', fontsize = 18, fontweight = 'bold')
ax[1, 0].set_xlim(0, len(time2) / 10)
ax[0, 0].set_xlim(0, len(time2) / 10)
ax[2, 0].plot(time2 , uz20, 'purple', label = 'uz20m winds')
ax[2, 0].plot(time2, uz20.rolling(window = n).mean(), 'black', label = 'Avg. uz20m winds', linestyle = '-')
ax[2, 0].set_title('uz20 winds vs time(s)', fontsize = 18, fontweight = 'bold')
ax[2, 0].set_ylabel('Speed (m/s)', fontsize = 18, fontweight = 'bold')
ax[2, 0].set_xlabel('Time (seconds)', fontsize = 18, fontweight = 'bold')
ax[2, 0].legend(prop={'size': 6})
ax[2, 0].set_xlim(0, len(time2) / 10)
ax[3, 0].plot(time2, ts20, 'green', label = 'Temperature$^\circ$C 20m')
ax[3, 0].plot(time2, ts20.rolling(window = n).mean(), 'black', label = 'Temperature$^\circ$C 20m', linestyle = '-')
ax[3, 0].set_title('ts20 winds vs time(s)', fontsize = 18, fontweight = 'bold')
ax[3, 0].set_ylabel('Temperature C', fontsize = 18, fontweight = 'bold')
ax[3, 0].set_xlabel('Time (seconds)', fontsize = 18, fontweight = 'bold')
ax[3, 0].legend(prop={'size': 6})
ax[3, 0].set_xlim(0, len(time2) / 10)
ax[0, 1].plot(time2, ux10, 'red', label = 'ux10 winds')
ax[0, 1].plot(time2, ux10.rolling(window = n).mean(), 'black', label = 'Avg. ux10 winds', linestyle = '-')
ax[0, 1].set_title('ux10 winds vs time(s)', fontsize = 18, fontweight = 'bold')
ax[0, 1].set_ylabel('Speed (m/s)', fontsize = 18, fontweight = 'bold')
ax[0, 1].set_xlabel('Time (seconds)', fontsize = 18, fontweight = 'bold')
ax[0, 1].legend(prop={'size': 6})
ax[0, 1].set_xlim(0, len(time2) / 10)
ax[1, 1].plot(time2, uy10, 'blue', label = 'uy10m winds')
ax[1, 1].plot(time2, uy10.rolling(window = n).mean(), 'black', label = 'Avg. uy10 winds', linestyle = '-')
ax[1, 1].set_title('uy10 winds vs time(s)', fontsize = 18, fontweight = 'bold')
ax[1, 1].set_ylabel('Speed (m/s)', fontsize = 18, fontweight = 'bold')
ax[1, 1].set_xlabel('Time (seconds)', fontsize = 18, fontweight = 'bold')
ax[1, 1].legend(prop={'size': 6})
ax[1, 1].set_xlim(0, len(time2) / 10)
ax[2, 1].plot(time2, uz10, 'purple', label = 'uz10m winds')
ax[2, 1].plot(time2, uz10.rolling(window = n).mean(), 'black', label = 'Avg. uz10 winds', linestyle = '-')
ax[2, 1].set_title('uz10 winds vs time(s)', fontsize = 18, fontweight = 'bold')
ax[2, 1].set_ylabel('Speed (m/s)', fontsize = 18, fontweight = 'bold')
ax[2, 1].set_xlabel('Time (seconds)', fontsize = 18, fontweight = 'bold')
ax[2, 1].legend(prop={'size': 6})
ax[2, 1].set_xlim(0, len(time2) / 10)
ax[3, 1].plot(time2, ts10, 'green', label = 'Temperature$^\circ$C 10m')
ax[3, 1].plot(time2, ts10.rolling(window = n).mean(), 'black', label = 'Avg. ts10 winds', linestyle = '-')
ax[3, 1].set_title('ts10 winds vs time(s)', fontsize = 18, fontweight = 'bold')
ax[3, 1].set_ylabel('Temperature C', fontsize = 18, fontweight = 'bold')
ax[3, 1].set_xlabel('Time (seconds)', fontsize = 18, fontweight = 'bold')
ax[3, 1].legend(prop={'size': 6})
ax[3, 1].set_xlim(0, len(time2) / 10)
ax[0, 2].plot(time2, ux6, 'red', label = 'ux6m winds')
ax[0, 2].plot(time2, ux6.rolling(window = n).mean(), 'black', label = 'ux6m winds', linestyle = '-')
ax[0, 2].set_title('ux6 winds vs time(s)', fontsize = 18, fontweight = 'bold')
ax[0, 2].set_ylabel('Speed (m/s)', fontsize = 18, fontweight = 'bold')
ax[0, 2].set_xlabel('Time (seconds)', fontsize = 18, fontweight = 'bold')
ax[0, 2].legend(prop={'size': 6})
ax[0, 2].set_xlim(0, len(time2) / 10)
ax[1, 2].plot(time2, uy6, 'blue', label = 'uy6m winds')
ax[1, 2].plot(time2, uy6.rolling(window = n).mean(), 'black', label = 'uy6m winds', linestyle = '-')
ax[1, 2].set_title('uy6 winds vs time(s)', fontsize = 18, fontweight = 'bold')
ax[1, 2].set_ylabel('Speed (m/s)', fontsize = 18, fontweight = 'bold')
ax[1, 2].set_xlabel('Time (seconds)', fontsize = 18, fontweight = 'bold')
ax[1, 2].legend(prop={'size': 6})
ax[1, 2].set_xlim(0, len(time2) / 10)
ax[2, 2].plot(time2, uz6, 'purple', label = 'uz6m winds')
ax[2, 2].plot(time2, uz6.rolling(window = n).mean(), 'black', label = 'uz6m winds', linestyle = '-')
ax[2, 2].set_title('uz6 winds vs time(s)', fontsize = 18, fontweight = 'bold')
ax[2, 2].set_ylabel('Speed (m/s)', fontsize = 18, fontweight = 'bold')
ax[2, 2].set_xlabel('Time (seconds)', fontsize = 18, fontweight = 'bold')
ax[2, 2].legend(prop={'size': 6})
ax[2, 2].set_xlim(0, len(time2) / 10)
ax[3, 2].plot(time2, ts6, 'green', label = 'Temperature$^\circ$C 6m')
ax[3, 2].plot(time2, ts6.rolling(window = n).mean(), 'black', label = 'ts6m winds', linestyle = '-')
ax[3, 2].set_title('ts6 winds vs time(s)', fontsize = 18, fontweight = 'bold')
ax[3, 2].set_ylabel('Temperature C', fontsize = 18, fontweight = 'bold')
ax[3, 2].set_xlabel('Time (seconds)', fontsize = 18, fontweight = 'bold')
ax[3, 2].legend(prop={'size': 6})
ax[3, 2].set_xlim(0, len(time2) / 10)
ax[0, 0].grid()
ax[1, 0].grid()
ax[2, 0].grid()
ax[3, 0].grid()
ax[0, 1].grid()
ax[1, 1].grid()
ax[2, 1].grid()
ax[3, 1].grid()
ax[0, 2].grid()
ax[1, 2].grid()
ax[2, 2].grid()
ax[3, 2].grid()
plt.tight_layout()
plt.show()
# %% Bar plots
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


















