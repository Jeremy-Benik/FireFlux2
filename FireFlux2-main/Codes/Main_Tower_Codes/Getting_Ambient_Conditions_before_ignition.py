'''This code creates a plot of all the variables in the file for 4 minutes before the ignition and 30 minutes after the ignition.
this code also averages the time over 5 seconds (black line) to see what the averages would be like'''

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
# %% This section of the code will read in the dataframe as df1 and it will be truncated based on
#5 minutes before the fire started, and 30 minutes after the fire started
#Since the fire started at 15:04:08, and the data is 10hz, I indexed to the 8th second in the file
df1 = pd.read_csv('/home/jbenik/FireFlux2/Codes_and_Data/Data/Main_Tower_Data/Proc_FF2_10HzMTdespiked_rotated.csv', parse_dates=['TIMESTAMP'], skiprows = (0, 2, 3))
#this reads in the dataframe and parses the dates. I also skip unecessary rows. This csv is modified by removing the record column and 
#moving the other columns over
df = df1.truncate(before= np.where(df1['TIMESTAMP'] == '1/30/2013  15:00:00')[0][0], 
                    after=np.where(df1['TIMESTAMP'] == '1/30/2013  15:09:00')[0][79])
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
fig.suptitle('Conditions From Main Tower 4 Minutes Before Ignition and 5 Minutes After With 5 Second Time Averaging', fontsize=18, fontweight = 'bold')
ax[0, 0].plot(time2, ux20, 'r', label = '20m U Wind')
ax[0, 0].plot(time2, ux20.rolling(window = n).mean(), 'black', label = 'Avg. 20m Winds', linestyle = '-')
ax[0, 0].set_title('U Winds (20m) vs Time (s)', fontsize = 18, fontweight = 'bold')
ax[0, 0].set_ylabel('Speed (m/s)', fontsize = 18, fontweight = 'bold')
ax[0, 0].set_xlabel('Time (seconds)', fontsize = 18, fontweight = 'bold')
ax[0, 0].legend(prop={'size': 6})
ax[1, 0].plot(time2, uy20, 'blue', label = '20m V Wind')
ax[1, 0].plot(time2, uy20.rolling(window = n).mean(), 'black', label = 'Avg. 20m Winds', linestyle = '-')
ax[1, 0].legend(prop={'size': 6})
ax[1, 0].set_xlabel('Time (seconds)', fontsize = 18, fontweight = 'bold')
ax[1, 0].set_ylabel('Speed (m/s)', fontsize = 18, fontweight = 'bold')
ax[1, 0].set_title('V Winds (20m) vs Time (s)', fontsize = 18, fontweight = 'bold')
ax[1, 0].set_xlim(0, len(time2) / 10)
ax[0, 0].set_xlim(0, len(time2) / 10)
ax[2, 0].plot(time2 , uz20, 'purple', label = '20m W Wind')
ax[2, 0].plot(time2, uz20.rolling(window = n).mean(), 'black', label = 'Avg. 20m Winds', linestyle = '-')
ax[2, 0].set_title('W Winds (20m) vs Time (s)', fontsize = 18, fontweight = 'bold')
ax[2, 0].set_ylabel('Speed (m/s)', fontsize = 18, fontweight = 'bold')
ax[2, 0].set_xlabel('Time (seconds)', fontsize = 18, fontweight = 'bold')
ax[2, 0].legend(prop={'size': 6})
ax[2, 0].set_xlim(0, len(time2) / 10)
ax[3, 0].plot(time2, ts20, 'green', label = 'Temperature$^\circ$C 20m')
ax[3, 0].plot(time2, ts20.rolling(window = n).mean(), 'black', label = 'Temperature$^\circ$C 20m', linestyle = '-')
ax[3, 0].set_title('Temperature (20m) vs Time (s)', fontsize = 18, fontweight = 'bold')
ax[3, 0].set_ylabel('Temperature \N{DEGREE SIGN}C', fontsize = 18, fontweight = 'bold')
ax[3, 0].set_xlabel('Time (seconds)', fontsize = 18, fontweight = 'bold')
ax[3, 0].legend(prop={'size': 6})
ax[3, 0].set_xlim(0, len(time2) / 10)
ax[0, 1].plot(time2, ux10, 'red', label = '10m U Wind')
ax[0, 1].plot(time2, ux10.rolling(window = n).mean(), 'black', label = 'Avg. 10m Winds', linestyle = '-')
ax[0, 1].set_title('U Winds (10m) vs Time (s)', fontsize = 18, fontweight = 'bold')
ax[0, 1].set_ylabel('Speed (m/s)', fontsize = 18, fontweight = 'bold')
ax[0, 1].set_xlabel('Time (seconds)', fontsize = 18, fontweight = 'bold')
ax[0, 1].legend(prop={'size': 6})
ax[0, 1].set_xlim(0, len(time2) / 10)
ax[1, 1].plot(time2, uy10, 'blue', label = '10m V Wind')
ax[1, 1].plot(time2, uy10.rolling(window = n).mean(), 'black', label = 'Avg. 10m Winds', linestyle = '-')
ax[1, 1].set_title('V Winds (10m) vs Time (s)', fontsize = 18, fontweight = 'bold')
ax[1, 1].set_ylabel('Speed (m/s)', fontsize = 18, fontweight = 'bold')
ax[1, 1].set_xlabel('Time (seconds)', fontsize = 18, fontweight = 'bold')
ax[1, 1].legend(prop={'size': 6})
ax[1, 1].set_xlim(0, len(time2) / 10)
ax[2, 1].plot(time2, uz10, 'purple', label = '10m W Wind')
ax[2, 1].plot(time2, uz10.rolling(window = n).mean(), 'black', label = 'Avg. 10m Winds', linestyle = '-')
ax[2, 1].set_title('W Winds (10m) vs Time (s)', fontsize = 18, fontweight = 'bold')
ax[2, 1].set_ylabel('Speed (m/s)', fontsize = 18, fontweight = 'bold')
ax[2, 1].set_xlabel('Time (seconds)', fontsize = 18, fontweight = 'bold')
ax[2, 1].legend(prop={'size': 6})
ax[2, 1].set_xlim(0, len(time2) / 10)
ax[3, 1].plot(time2, ts10, 'green', label = 'Temperature$^\circ$C 10m')
ax[3, 1].plot(time2, ts10.rolling(window = n).mean(), 'black', label = 'Avg. 10m Temp.', linestyle = '-')
ax[3, 1].set_title('Temperature (10m) vs Time (s)', fontsize = 18, fontweight = 'bold')
ax[3, 1].set_ylabel('Temperature \N{DEGREE SIGN}C', fontsize = 18, fontweight = 'bold')
ax[3, 1].set_xlabel('Time (seconds)', fontsize = 18, fontweight = 'bold')
ax[3, 1].legend(prop={'size': 6})
ax[3, 1].set_xlim(0, len(time2) / 10)
ax[0, 2].plot(time2, ux6, 'red', label = '5.77m U Wind')
ax[0, 2].plot(time2, ux6.rolling(window = n).mean(), 'black', label = 'Avg. 5.77m Winds', linestyle = '-')
ax[0, 2].set_title('U Winds (5.77m) vs Time (s)', fontsize = 18, fontweight = 'bold')
ax[0, 2].set_ylabel('Speed (m/s)', fontsize = 18, fontweight = 'bold')
ax[0, 2].set_xlabel('Time (seconds)', fontsize = 18, fontweight = 'bold')
ax[0, 2].legend(prop={'size': 6})
ax[0, 2].set_xlim(0, len(time2) / 10)
ax[1, 2].plot(time2, uy6, 'blue', label = '5.77m V Wind')
ax[1, 2].plot(time2, uy6.rolling(window = n).mean(), 'black', label = 'Avg. 5.77m Winds', linestyle = '-')
ax[1, 2].set_title('V Winds (5.77m) vs Time (s)', fontsize = 18, fontweight = 'bold')
ax[1, 2].set_ylabel('Speed (m/s)', fontsize = 18, fontweight = 'bold')
ax[1, 2].set_xlabel('Time (seconds)', fontsize = 18, fontweight = 'bold')
ax[1, 2].legend(prop={'size': 6})
ax[1, 2].set_xlim(0, len(time2) / 10)
ax[2, 2].plot(time2, uz6, 'purple', label = '5.77m W Wind')
ax[2, 2].plot(time2, uz6.rolling(window = n).mean(), 'black', label = 'Avg. 5.77m Winds', linestyle = '-')
ax[2, 2].set_title('W Winds (5.77m) vs Time (s)', fontsize = 18, fontweight = 'bold')
ax[2, 2].set_ylabel('Speed (m/s)', fontsize = 18, fontweight = 'bold')
ax[2, 2].set_xlabel('Time (seconds)', fontsize = 18, fontweight = 'bold')
ax[2, 2].legend(prop={'size': 6})
ax[2, 2].set_xlim(0, len(time2) / 10)
ax[3, 2].plot(time2, ts6, 'green', label = 'Temperature$^\circ$C 5.77m')
ax[3, 2].plot(time2, ts6.rolling(window = n).mean(), 'black', label = 'Avg. 5.77m Temp.', linestyle = '-')
ax[3, 2].set_title('Temperature (5.77m) vs Time (s)', fontsize = 18, fontweight = 'bold')
ax[3, 2].set_ylabel('Temperature \N{DEGREE SIGN}C', fontsize = 18, fontweight = 'bold')
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





















# %%

