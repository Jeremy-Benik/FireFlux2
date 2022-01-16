#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  1 12:35:19 2022

@author: Jeremy Benik
"""

import pandas as pd #importing pandas so I can use it to read in the file
import matplotlib.pyplot as plt #importing matplotlib to create the plot
import numpy as np #importing numpy as I need it for calculating the square root to get wind speeds and np.where

df1 = pd.read_csv('/media/jeremy/Data/Fireflux2/Website_Docs/Main_Tower_Data/Proc_FF2_10HzMTdespiked_rotated.csv', 
                  parse_dates=['TIMESTAMP'], skiprows = (0, 2, 3)) #setting df1 to the dataframe, change this to your path
#and you will also likely need to change the parse_dates to your dates and skiprows to whatever rows you want to skip

#what this does is it takes the file and cuts it down to what I want it to be. So in this case I'm using it 
#to cut down my data to 4 minutes before the fire start, and I set this to df.
#The indexing at the end is to get the index to where that time occurs. 
df = df1.truncate(before= np.where(df1['TIMESTAMP'] == '1/30/2013  15:00:00')[0][80], 
                    after=np.where(df1['TIMESTAMP'] == '1/30/2013  15:04:00')[0][80])

#Reasding in the variables
time = df['TIMESTAMP'][1::40] #defining time and the indexing is to start at the first element and skip every 20th element
#Since there are a lot of data points, plotting them looks terrible so by plotting every 20th data point, it looks much better
ux20 = df['Ux_20m'][1::40]
uy20 = df['Uy_20m'][1::40]
uz20 = df['Uz_20m'][1::40]
ts20 = df['Ts_20m'][1::40]
ux10 = df['Ux_10m'][1::40]
uy10 = df['Uy_10m'][1::40]
uz10 = df['Uz_10m'][1::40]
ts10 = df['Ts_10m'][1::40]
ux6 = df['Ux_6m'][1::40]
uy6 = df['Uy_6m'][1::40]
uz6 = df['Uz_6m'][1::40]
ts6 = df['Ts_6m'][1::40]
n = 5 #This is set to 2 since I'm iterating every 20th number, and there are 10 measurements per second, so to 
#accurately get the time, I need to mulitply is by two to get the actual seconds of the data. 
#time = np.array(time)

fig, ax = plt.subplots(figsize = (15, 10)) #creating the plot, can be used to make subplots if needed

uv20 = np.sqrt(ux20**2 + uy20**2) #calculating the wind speed for the 20m high tower
uv10 = np.sqrt(ux10**2 + uy10**2) #calculating the wind speed for the 10m high tower
uv6 = np.sqrt(ux6**2 + uy6**2) #calculating the wind speed for the 6m high tower

#This is where the magic starts to happen, here are the inputs: X (time), Y (height on tower), U wind, V wind, color
ax.quiver(range(0, n * len(time), n), 20, ux20, -uy20, color = 'blue')
#Here I used the x component of the wind, then -y to point the values towards the tower, and colored it to look nice. 

ax.quiver(range(0, n * len(time), n), 10, ux10, -uy10, color = 'red')


ax.quiver(range(0, n * len(time), n), 6, ux6, -uy6, color = 'green')
height = ['20 meters AGL', '10 meters AGL', '6 meters AGL']
ax.legend(height)
#plt.colorbar(ux20, orientation = 'horizontal')

# there's gonna be a lot of arrows. Use a subset. Maybe every minute to see what's going on. I could even do an average across some time period.
ax.set_ylim([0, 25])
ax.set_xlim([0, n * len(time)])
ax.set_xlabel('Time (Seconds)', fontsize = 18, fontweight = 'bold')
ax.set_ylabel('Height (m)', fontsize = 18, fontweight = 'bold')
ax.set_title('Wind Vectors From Main Tower At Different Levels Taken 4 Minutes Before Ignition', fontsize = 22, fontweight = 'bold' )
# In this plot, we assume the winds are blowing towards the tower.
plt.tight_layout()
plt.show()

# %% 4 min before and 4 min after (8 min total)
df1 = pd.read_csv('/media/jeremy/Data/Fireflux2/Website_Docs/Main_Tower_Data/Proc_FF2_10HzMTdespiked_rotated.csv', 
                  parse_dates=['TIMESTAMP'], skiprows = (0, 2, 3)) #setting df1 to the dataframe, change this to your path
#and you will also likely need to change the parse_dates to your dates and skiprows to whatever rows you want to skip

#what this does is it takes the file and cuts it down to what I want it to be. So in this case I'm using it 
#to cut down my data to 4 minutes before the fire start, and I set this to df.
#The indexing at the end is to get the index to where that time occurs. 
df = df1.truncate(before= np.where(df1['TIMESTAMP'] == '1/30/2013  15:00:00')[0][80], 
                    after=np.where(df1['TIMESTAMP'] == '1/30/2013  15:08:00')[0][80])

#Reasding in the variables
time = df['TIMESTAMP'][1::60] #defining time and the indexing is to start at the first element and skip every 20th element
#Since there are a lot of data points, plotting them looks terrible so by plotting every 20th data point, it looks much better
ux20 = df['Ux_20m'][1::60]
uy20 = df['Uy_20m'][1::60]
uz20 = df['Uz_20m'][1::60]
ts20 = df['Ts_20m'][1::60]
ux10 = df['Ux_10m'][1::60]
uy10 = df['Uy_10m'][1::60]
uz10 = df['Uz_10m'][1::60]
ts10 = df['Ts_10m'][1::60]
ux6 = df['Ux_6m'][1::60]
uy6 = df['Uy_6m'][1::60]
uz6 = df['Uz_6m'][1::60]
ts6 = df['Ts_6m'][1::60]
n = 6 #This is set to 2 since I'm iterating every 20th number, and there are 10 measurements per second, so to 
#accurately get the time, I need to mulitply is by two to get the actual seconds of the data. 
#time = np.array(time)

fig, ax = plt.subplots(figsize = (15, 10)) #creating the plot, can be used to make subplots if needed

uv20 = np.sqrt(ux20**2 + uy20**2) #calculating the wind speed for the 20m high tower
uv10 = np.sqrt(ux10**2 + uy10**2) #calculating the wind speed for the 10m high tower
uv6 = np.sqrt(ux6**2 + uy6**2) #calculating the wind speed for the 6m high tower

#This is where the magic starts to happen, here are the inputs: X (time), Y (height on tower), U wind, V wind, color
ax.quiver(range(0, n * len(time), n), 20, ux20, -uy20, color = 'blue')
#Here I used the x component of the wind, then -y to point the values towards the tower, and colored it to look nice. 

ax.quiver(range(0, n * len(time), n), 10, ux10, -uy10, color = 'red')


ax.quiver(range(0, n * len(time), n), 6, ux6, -uy6, color = 'green')
height = ['20 meters AGL', '10 meters AGL', '6 meters AGL']
ax.legend(height)
#plt.colorbar(ux20, orientation = 'horizontal')

# there's gonna be a lot of arrows. Use a subset. Maybe every minute to see what's going on. I could even do an average across some time period.
ax.set_ylim([0, 25])
ax.set_xlim([0, n * len(time)])
ax.set_xlabel('Time (Seconds)', fontsize = 18, fontweight = 'bold')
ax.set_ylabel('Height (m)', fontsize = 18, fontweight = 'bold')
ax.set_title('Wind Vectors From Main Tower At Different Levels Taken 4 Min Before and 4min After Ignition', fontsize = 22, fontweight = 'bold' )
# In this plot, we assume the winds are blowing towards the tower.
plt.tight_layout()
plt.show()

# %% 10 minutes after ignition

df1 = pd.read_csv('/media/jeremy/Data/Fireflux2/Website_Docs/Main_Tower_Data/Proc_FF2_10HzMTdespiked_rotated.csv', 
                  parse_dates=['TIMESTAMP'], skiprows = (0, 2, 3)) #setting df1 to the dataframe, change this to your path
#and you will also likely need to change the parse_dates to your dates and skiprows to whatever rows you want to skip

#what this does is it takes the file and cuts it down to what I want it to be. So in this case I'm using it 
#to cut down my data to 4 minutes before the fire start, and I set this to df.
#The indexing at the end is to get the index to where that time occurs. 
df = df1.truncate(before= np.where(df1['TIMESTAMP'] == '1/30/2013  15:04:00')[0][80], 
                    after=np.where(df1['TIMESTAMP'] == '1/30/2013  15:14:00')[0][80])

#Reasding in the variables
time = df['TIMESTAMP'][1::80] #defining time and the indexing is to start at the first element and skip every 20th element
#Since there are a lot of data points, plotting them looks terrible so by plotting every 20th data point, it looks much better
ux20 = df['Ux_20m'][1::80]
uy20 = df['Uy_20m'][1::80]
uz20 = df['Uz_20m'][1::80]
ts20 = df['Ts_20m'][1::80]
ux10 = df['Ux_10m'][1::80]
uy10 = df['Uy_10m'][1::80]
uz10 = df['Uz_10m'][1::80]
ts10 = df['Ts_10m'][1::80]
ux6 = df['Ux_6m'][1::80]
uy6 = df['Uy_6m'][1::80]
uz6 = df['Uz_6m'][1::80]
ts6 = df['Ts_6m'][1::80]
n = 8 #This is set to 2 since I'm iterating every 20th number, and there are 10 measurements per second, so to 
#accurately get the time, I need to mulitply is by two to get the actual seconds of the data. 
#time = np.array(time)

fig, ax = plt.subplots(figsize = (15, 10)) #creating the plot, can be used to make subplots if needed

uv20 = np.sqrt(ux20**2 + uy20**2) #calculating the wind speed for the 20m high tower
uv10 = np.sqrt(ux10**2 + uy10**2) #calculating the wind speed for the 10m high tower
uv6 = np.sqrt(ux6**2 + uy6**2) #calculating the wind speed for the 6m high tower

#This is where the magic starts to happen, here are the inputs: X (time), Y (height on tower), U wind, V wind, color
ax.quiver(range(0, n * len(time), n), 20, ux20, -uy20, color = 'blue')
#Here I used the x component of the wind, then -y to point the values towards the tower, and colored it to look nice. 

ax.quiver(range(0, n * len(time), n), 10, ux10, -uy10, color = 'red')


ax.quiver(range(0, n * len(time), n), 6, ux6, -uy6, color = 'green')
height = ['20 meters AGL', '10 meters AGL', '6 meters AGL']
ax.legend(height)
#plt.colorbar(ux20, orientation = 'horizontal')

# there's gonna be a lot of arrows. Use a subset. Maybe every minute to see what's going on. I could even do an average across some time period.
ax.set_ylim([0, 25])
ax.set_xlim([0, n * len(time)])
ax.set_xlabel('Time (Seconds)', fontsize = 18, fontweight = 'bold')
ax.set_ylabel('Height (m)', fontsize = 18, fontweight = 'bold')
ax.set_title('Wind Vectors From Main Tower At Different Levels Taken 10 Minutes After Ignition', fontsize = 22, fontweight = 'bold' )
# In this plot, we assume the winds are blowing towards the tower.
plt.tight_layout()
plt.show()
# %% 15 minutes after ignition
df1 = pd.read_csv('/media/jeremy/Data/Fireflux2/Website_Docs/Main_Tower_Data/Proc_FF2_10HzMTdespiked_rotated.csv', 
                  parse_dates=['TIMESTAMP'], skiprows = (0, 2, 3)) #setting df1 to the dataframe, change this to your path
#and you will also likely need to change the parse_dates to your dates and skiprows to whatever rows you want to skip

#what this does is it takes the file and cuts it down to what I want it to be. So in this case I'm using it 
#to cut down my data to 4 minutes before the fire start, and I set this to df.
#The indexing at the end is to get the index to where that time occurs. 
df = df1.truncate(before= np.where(df1['TIMESTAMP'] == '1/30/2013  15:04:00')[0][80], 
                    after=np.where(df1['TIMESTAMP'] == '1/30/2013  15:19:00')[0][80])

#Reasding in the variables
time = df['TIMESTAMP'][1::100] #defining time and the indexing is to start at the first element and skip every 20th element
#Since there are a lot of data points, plotting them looks terrible so by plotting every 20th data point, it looks much better
ux20 = df['Ux_20m'][1::100]
uy20 = df['Uy_20m'][1::100]
uz20 = df['Uz_20m'][1::100]
ts20 = df['Ts_20m'][1::100]
ux10 = df['Ux_10m'][1::100]
uy10 = df['Uy_10m'][1::100]
uz10 = df['Uz_10m'][1::100]
ts10 = df['Ts_10m'][1::100]
ux6 = df['Ux_6m'][1::100]
uy6 = df['Uy_6m'][1::100]
uz6 = df['Uz_6m'][1::100]
ts6 = df['Ts_6m'][1::100]
n = 10 #This is set to 3 since I'm iterating every 30th number, and there are 10 measurements per second, so to 
#accurately get the time, I need to mulitply is by three to get the actual seconds of the data. 
#All the other plots skipped the 20th element, but since there are so many points here I used 3 to make the graph legible
#time = np.array(time)

fig, ax = plt.subplots(figsize = (15, 10)) #creating the plot, can be used to make subplots if needed

uv20 = np.sqrt(ux20**2 + uy20**2) #calculating the wind speed for the 20m high tower
uv10 = np.sqrt(ux10**2 + uy10**2) #calculating the wind speed for the 10m high tower
uv6 = np.sqrt(ux6**2 + uy6**2) #calculating the wind speed for the 6m high tower

#This is where the magic starts to happen, here are the inputs: X (time), Y (height on tower), U wind, V wind, color
ax.quiver(range(0, n * len(time), n), 20, ux20, -uy20, color = 'blue')
#Here I used the x component of the wind, then -y to point the values towards the tower, and colored it to look nice. 

ax.quiver(range(0, n * len(time), n), 10, ux10, -uy10, color = 'red')


ax.quiver(range(0, n * len(time), n), 6, ux6, -uy6, color = 'green')
height = ['20 meters AGL', '10 meters AGL', '6 meters AGL']
ax.legend(height)
#plt.colorbar(ux20, orientation = 'horizontal')

# there's gonna be a lot of arrows. Use a subset. Maybe every minute to see what's going on. I could even do an average across some time period.
ax.set_ylim([0, 25])
ax.set_xlim([0, n * len(time)])
ax.set_xlabel('Time (Seconds)', fontsize = 18, fontweight = 'bold')
ax.set_ylabel('Height (m)', fontsize = 18, fontweight = 'bold')
ax.set_title('Wind Vectors From Main Tower At Different Levels Taken 15 Minutes After Ignition', fontsize = 22, fontweight = 'bold' )
# In this plot, we assume the winds are blowing towards the tower.
plt.tight_layout()
plt.show() 
