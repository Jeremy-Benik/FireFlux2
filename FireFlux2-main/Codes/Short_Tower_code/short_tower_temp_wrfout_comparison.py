''' This code plots the temperatures of the short towers compared to the wrfout file to see how they compare'''
#This information below are the indices for the towers
"""
Created on Sat March 5 11:36:54 2022

@author: Jeremy Benik
"""
'''Here are the results of this code for quick access if needed
None of these are staggered, these are just using the regular grid

Main tower
y for main tower is at: 190
x for main tower is: 93

East tower
y for east tower is at: 158
x for east tower is: 117

West tower
y for west tower is at: 151
West_west for west tower is: 94

South tower
y for south tower is at: 119
West_south for south tower is: 115

Fire mesh coordinates

Main tower
y for main tower is at: 1908
x for main tower is: 937

East tower
y for east tower is at: 1581
x for east tower is: 1173

West tower
y for west tower is at: 1511
West_west for west tower is: 943

South tower
y for south tower is at: 1199
West_south for south tower is: 1155 '''
# %% Importing libraries
print("importing libraries")
import pandas as pd
import netCDF4 as nc
import xarray as xr
import matplotlib.pyplot as plt
import numpy as np
import wrf
import statistics as st
import glob
import pickle
import os.path as osp
out_path = 'short_tower_temp_wrfout_with_time_1.pkl' #To change the file, change this name
if not osp.exists(out_path):
    # %% Assigning tower coords
    print("Getting indicies of the towers")
    #These values can be found in the code titled finding_towers_ideal.py. 
    # these values are not on the subgrid
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

    # Now these are the subgrid coords

    # Main tower
    y_main_sub = 1908
    x_main_sub = 937

    # East tower
    y_east_sub = 1581
    x_east_sub = 1173

    # West tower
    y_west_sub = 1511
    x_west_sub = 943

    # South tower
    y_south_sub = 1199
    x_south_sub = 1155
    # %% Reading in the data
    print("Reading in the data")
    # Wrfout file 
    print(" Reading in the wrfout file from the ideal case")
    wrfout = nc.Dataset('/home/jbenik/FireFlux2/Codes_and_Data/Data/wrf_files/wrfout_files/wrfout_d01_2013-01-30_15:00:00', 'r')

    # %% Variables from the wrfout file
    # To get the variables from thw wrfout file, I am using the wrf library to get them so they won't be staggered in the grid
    print('Reading in Time')
    time = wrfout.variables['XTIME'][:]
    print('Reading in Temp from the wrfout')
    T_wrfout = wrf.getvar(wrfout, "temp", None, units = 'K')
    T_wrfout -= 273.15 #converting it to celcius
    print("Now I am getting height")
    ht = wrf.getvar(wrfout, "z", units="m", msl = False)
    # %% Interpolating the variables to specific heights
    # %% Short towers
    print("Getting the short tower data")
    n = 5 #this is a 5 second average of the data
    df_w1 = pd.read_csv('/home/jbenik/FireFlux2/Codes_and_Data/Data/Short_Tower_Data/Proc_FF2_1HzSTWdespikedrotated.csv')

    df_w = df_w1.truncate(before= np.where(df_w1['TIMESTAMP'] == '1/30/2013 15:04')[0][0], 
                        after=np.where(df_w1['TIMESTAMP'] == '1/30/2013 15:14')[0][0])

    df_e1 = pd.read_csv('/home/jbenik/FireFlux2/Codes_and_Data/Data/Short_Tower_Data/Proc_FF2_1HzSTEdespikedrotated.csv')

    df_e = df_e1.truncate(before= np.where(df_e1['TIMESTAMP'] == '1/30/2013 15:04')[0][0], 
                        after=np.where(df_e1['TIMESTAMP'] == '1/30/2013 15:14')[0][0])

    df_s1 = pd.read_csv('/home/jbenik/FireFlux2/Codes_and_Data/Data/Short_Tower_Data/Proc_FF2_1HzSTSdespikedrotated.csv')

    df_s = df_s1.truncate(before= np.where(df_s1['TIMESTAMP'] == '1/30/2013 15:04')[0][0], 
                        after=np.where(df_s1['TIMESTAMP'] == '1/30/2013 15:14')[0][0])

    # defining vars
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

    # %% Getting locations of the towers then assigning variables to them
    #west tower
    print('Interpolating west tower at 5.33 meters')
    Tw_h_533 = wrf.interplevel(T_wrfout, ht, 5.33)[y_west, x_west]

    #east tower
    print('Interpolating the east tower at 5.28 meters')
    Te_h_528 = wrf.interplevel(T_wrfout, ht, 5.28)[y_east, x_east]


    #south tower
    print('interpolating the south tower at 5.33 meters')
    Ts_h_533 = wrf.interplevel(T_wrfout, ht, 5.33)[y_south, x_south]
    
    wrfout_time = wrfout.variables['XTIME'][:]
    results = {'Tw_h_533':Tw_h_533, 'Ts_h_533':Ts_h_533, 'Te_h_528':Te_h_528, 'wrfout_time':wrfout_time}

    with open(out_path, 'wb') as f:
        pickle.dump(results, f)
else:
    with open(out_path, 'rb') as f:
        results = pickle.load(f)
    locals().update(results)

# %% Creating a plot for the short towers
print("Creating the plot")
fig, ax = plt.subplots(1, 3, figsize = (15, 10))
plt.suptitle('Short Tower Temperature (\N{DEGREE SIGN}C) vs. wrfout file', fontsize = 15, fontweight = 'bold')
# Plotting the west tower first
#temperature
ax[0].plot(np.arange(240, 841), tw, color = 'green', label = 'West Tower') #plotting the wind speed from west tower
ax[0].plot(np.arange(240, 841), tw.rolling(window = n).mean(), color = 'black', label = 'Rolling Average') #plotting the rolling average from the west tower wind speed
ax[0].plot(np.array(wrfout.variables['XTIME'][240:841] * 60), Tw_h_533, color = 'red', label = 'wrfout file') #plotting the wind speed from the wrfout file
ax[0].set_xlabel('Time (Seconds)', fontsize = 12, fontweight = 'bold')
ax[0].set_ylabel('Temperature (\N{DEGREE SIGN}C)', fontsize = 12, fontweight = 'bold')
ax[0].set_title('West Tower Temperature (\N{DEGREE SIGN}C) vs. wrfout', fontsize = 13, fontweight = 'bold')
ax[0].legend()
# Plotting the South Tower
#temperature
ax[1].plot(np.arange(240, 841), ts, color = 'green', label = 'South Tower') #plotting the wind speed from South tower
ax[1].plot(np.arange(240, 841), ts.rolling(window = n).mean(), color = 'black', label = 'Rolling Average') #plotting the rolling average from the South tower wind speed
ax[1].plot(np.array(wrfout.variables['XTIME'][240:841]) * 60, Ts_h_533, color = 'red', label = 'wrfout file') #plotting the wind speed from the wrfout file
ax[1].set_xlabel('Time (Seconds)', fontsize = 12, fontweight = 'bold')
ax[1].set_ylabel('Temperature (\N{DEGREE SIGN}C)', fontsize = 12, fontweight = 'bold')
ax[1].set_title('South Tower Temperature (\N{DEGREE SIGN}C) vs. wrfout', fontsize = 13, fontweight = 'bold')
ax[1].legend()
# Plotting the East Tower
#temperature
ax[2].plot(np.arange(240, 841), te, color = 'green', label = 'East Tower') #plotting the wind speed from South tower
ax[2].plot(np.arange(240, 841), te.rolling(window = n).mean(), color = 'black', label = 'Rolling Average') #plotting the rolling average from the South tower wind speed
ax[2].plot(np.array(wrfout.variables['XTIME'][240:841]) * 60, Te_h_528, color = 'red', label = 'wrfout file') #plotting the wind speed from the wrfout file
ax[2].set_xlabel('Time (Seconds)', fontsize = 12, fontweight = 'bold')
ax[2].set_ylabel('Temperature (\N{DEGREE SIGN}C)', fontsize = 12, fontweight = 'bold')
ax[2].set_title('East Tower Temperature (\N{DEGREE SIGN}C) vs. wrfout', fontsize = 13, fontweight = 'bold')
ax[2].legend()

ax[0].grid()
ax[1].grid()
ax[2].grid()
plt.tight_layout()
#plt.savefig('/home/jbenik/FireFlux2/Codes_and_Data/Data/images/wrfout_short_towers2_temp_ideal_cheyenne_run_3.png')
plt.show()
plt.close()

# %%
