''' This program takes all the temperature data from the towers and from the wrfout file and compares them. This comparison is done to better see if the ROS was accurate or not'''
# -*- coding: utf-8 -*-
"""
Created on Mon March 28 11:39:54 2022

@author: Jeremy Benik
"""
# %% Importing libraries
import netCDF4 as nc
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import xarray as xr
import wrf
# %% Reading in the data and truncating it to the correct size
#main tower data
main_tower1 = pd.read_csv('/home/jbenik/FireFlux2/Codes_and_Data/Data/Main_Tower_Data/Proc_FF2_10HzMTdespiked_rotated.csv', parse_dates=['TIMESTAMP'], skiprows = (0, 2, 3))

main_tower = main_tower1.truncate(before= np.where(main_tower1['TIMESTAMP'] == '1/30/2013  15:04:00')[0][0], 
                    after=np.where(main_tower1['TIMESTAMP'] == '1/30/2013  15:14:00')[0][0])

#short tower data
df_w1 = pd.read_csv('/home/jbenik/FireFlux2/Codes_and_Data/Data/Short_Tower_Data/Proc_FF2_1HzSTWdespikedrotated.csv')

df_w = df_w1.truncate(before= np.where(df_w1['TIMESTAMP'] == '1/30/2013 15:04')[0][0], 
                    after=np.where(df_w1['TIMESTAMP'] == '1/30/2013 15:14')[0][0])

df_e1 = pd.read_csv('/home/jbenik/FireFlux2/Codes_and_Data/Data/Short_Tower_Data/Proc_FF2_1HzSTEdespikedrotated.csv')

df_e = df_e1.truncate(before= np.where(df_e1['TIMESTAMP'] == '1/30/2013 15:04')[0][0], 
                    after=np.where(df_e1['TIMESTAMP'] == '1/30/2013 15:14')[0][0])

df_s1 = pd.read_csv('/home/jbenik/FireFlux2/Codes_and_Data/Data/Short_Tower_Data/Proc_FF2_1HzSTSdespikedrotated.csv')

df_s = df_s1.truncate(before= np.where(df_s1['TIMESTAMP'] == '1/30/2013 15:04')[0][0], 
                    after=np.where(df_s1['TIMESTAMP'] == '1/30/2013 15:14')[0][0])
#wrfout file
print("Reading in the wrfout file")
wrfout = nc.Dataset('/home/jbenik/FireFlux2/Codes_and_Data/Data/wrf_files/wrfout_d01_2013-01-30_15:00:00', 'r')

# %% defining variables (I just need timestamp and T for this code)
print("Getting the variables from the main tower data")
time_main_tower = main_tower['TIMESTAMP']
time2 = np.arange(240, 840.1, .1)

print('20 meter variables')
ts20 = main_tower['Ts_20m']

print('10 meter variables')
ts10 = main_tower['Ts_10m']

print('6 meter variable')
ts6 = main_tower['Ts_6m']

#west tower
print("Reading variables from west tower")
time_short_tower_w = df_w['TIMESTAMP']
tw = df_w['t']
#east tower
print("Reading in variables from east tower")
time_short_tower_e = df_e['TIMESTAMP']
te = df_e['t']
#south tower
print("reading in variables from south tower")
time_short_tower_s = df_s['TIMESTAMP']
ts = df_s['t']

#wrfout temperature
print("reading in temperature from wrfout")
T_wrfout = wrf.getvar(wrfout, "temp", None, units = 'K')
T_wrfout -= 273.15 #converting it to celcius

#height for interpolating
print('reading in height from wrfout')
ht = wrf.getvar(wrfout, "z", units="m", msl = False)

# %% locations of the towers
# main tower
y_main = 190
x_main = 93

# East tower
y_east = 158
x_east = 117

# West tower
y_west = 151
x_west = 94

# South tower
y_south = 119
x_south = 115

# %% interpolating levels

print("Interpolating T at 20 meters")
T_h_20 = wrf.interplevel(T_wrfout, ht, 20)[240:841, y_main, x_main]
# 10 meters
print("Interpolating T at 10 meters")
T_h_10 = wrf.interplevel(T_wrfout, ht, 10)[240:841, y_main, x_main]
# 5.77 meters
print('Interpolating T at 5.77 meters')
T_h_577 = wrf.interplevel(T_wrfout, ht, 5.77)[240:841, y_main, x_main]

#west tower
print('Interpolating T for the west tower at 5.33 meters')
Tw_h_533 = wrf.interplevel(T_wrfout, ht, 5.33)[240:841, y_west, x_west]
#south tower
print('Interpolating T for the south tower at 5.33 meters')
Ts_h_533 = wrf.interplevel(T_wrfout, ht, 5.33)[240:841, y_south, x_south]
#east tower
print('Interpolating T for the east tower at 5.28 meters')
Te_h_528 = wrf.interplevel(T_wrfout, ht, 5.28)[240:841, y_east, x_east]
# %% Creating the figure and plotting them all
n = 10
fig, ax = plt.subplots(2, 3, figsize = (12, 12))
# Plotting T from the main tower at 20 meters
ax[0, 0].plot(np.array(wrfout.variables['XTIME'][240:841]) * 60, T_h_20, color = 'red', label = '20m wrfout T')
ax[0, 0].plot(time2, ts20, color = 'blue', label = '20 meter Main tower T')
ax[0, 0].plot(time2, ts20.rolling(window = n).mean(), color = 'black', label = 'Main Tower Rolling Average')
ax[0, 0].set_title('20 meter temperature')
ax[0, 0].set_xlabel('Time (seconds)')
ax[0, 0].set_ylabel('Temperature (C)')
# Plotting T from the main tower at 10 meters
ax[0, 1].plot(np.array(wrfout.variables['XTIME'][240:841]) * 60, T_h_10, color = 'red', label = '10m wrfout T')
ax[0, 1].plot(time2, ts10, color = 'blue', label = '10 meter Main tower T')
ax[0, 1].plot(time2, ts10.rolling(window = n).mean(), color = 'black', label = 'Main Tower Rolling Average')
ax[0, 1].set_title('10 meter temperature')
ax[0, 1].set_xlabel('Time (seconds)')
ax[0, 1].set_ylabel('Temperature (C)')
# Plotting T from the main tower at 5.77 meters
ax[0, 2].plot(np.array(wrfout.variables['XTIME'][240:841]) * 60, T_h_577, color = 'red', label = '5.77m wrfout T')
ax[0, 2].plot(time2, ts6, color = 'blue', label = '5.77 meter Main tower T')
ax[0, 2].plot(time2, ts6.rolling(window = n).mean(), color = 'black', label = 'Main Tower Rolling Average')
ax[0, 2].set_title('5.77 meter temperature')
ax[0, 2].set_xlabel('Time (seconds)')
ax[0, 2].set_ylabel('Temperature (C)')
n = 5 #creating a 5 second average of the data
# Plotting T from the East tower
ax[1, 0].plot(np.arange(240, 841), te, color = 'blue', label = 'East Tower Temp (\N{DEGREE SIGN}C)') #plotting the wind speed from South tower
ax[1, 0].plot(np.arange(240, 841), te.rolling(window = n).mean(), color = 'black', label = 'East Tower Rolling Average') #plotting the rolling average from the South tower wind speed
ax[1, 0].plot(np.array(wrfout.variables['XTIME'][240:841]) * 60, Te_h_528, color = 'red', label = 'wrfout file Temperature (\N{DEGREE SIGN}C)') #plotting the wind speed from the wrfout file
ax[1, 0].set_xlabel('Time', fontsize = 10)
ax[1, 0].set_ylabel('Temperature (\N{DEGREE SIGN}C)', fontsize = 10)
ax[1, 0].set_title('East Tower Temperature (\N{DEGREE SIGN}C) vs. wrfout', fontsize = 10)

# Plotting T from the West tower
ax[1, 1].plot(np.arange(240, 841), tw, color = 'blue', label = 'West Tower Temp (\N{DEGREE SIGN}C)') #plotting the wind speed from west tower
ax[1, 1].plot(np.arange(240, 841), tw.rolling(window = n).mean(), color = 'black', label = 'West Tower Rolling Average') #plotting the rolling average from the west tower wind speed
ax[1, 1].plot(np.array(wrfout.variables['XTIME'][240:841] * 60), Tw_h_533, color = 'red', label = 'wrfout file Temperature') #plotting the wind speed from the wrfout file
ax[1, 1].set_xlabel('Time', fontsize = 10)
ax[1, 1].set_ylabel('Temperature (\N{DEGREE SIGN}C)', fontsize = 10)
ax[1, 1].set_title('West Tower Temperature (\N{DEGREE SIGN}C) vs. wrfout', fontsize = 10)

# Plotting T from the South tower
ax[1, 2].plot(np.arange(240, 841), ts, color = 'blue', label = 'South Tower Temp (\N{DEGREE SIGN}C)') #plotting the wind speed from South tower
ax[1, 2].plot(np.arange(240, 841), ts.rolling(window = n).mean(), color = 'black', label = 'South Tower Rolling Average') #plotting the rolling average from the South tower wind speed
ax[1, 2].plot(np.array(wrfout.variables['XTIME'][240:841]) * 60, Ts_h_533, color = 'red', label = 'wrfout file Temperature') #plotting the wind speed from the wrfout file
ax[1, 2].set_xlabel('Time', fontsize = 10)
ax[1, 2].set_ylabel('Temperature (\N{DEGREE SIGN}C)', fontsize = 10)
ax[1, 2].set_title('South Tower Temperature (\N{DEGREE SIGN}C) vs. wrfout', fontsize = 10)

# Adding gridlines 
ax[0, 0].grid()
ax[0, 1].grid()
ax[0, 2].grid()
ax[1, 0].grid()
ax[1, 1].grid()
ax[1, 2].grid()

plt.tight_layout()
plt.savefig('/home/jbenik/FireFlux2/Codes_and_Data/Data/wrf_files/images/temperature_plot_ideal.png')
plt.show()