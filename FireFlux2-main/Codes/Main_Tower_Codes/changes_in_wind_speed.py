''' This program plots the wind speeds at the main tower compared to the wrfout file'''
# The info below are the indices for the towers on the burn plot
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
# %% Reading in the files
mod_wrfout = 'main_tower_winds_wrfout_no_fire_atms_new_vars.pkl'
out_path = 'main_tower_winds_wrfout.pkl' #To change the file, change this name
# %%
with open(out_path, 'rb') as f:
    results = pickle.load(f)
    locals().update(results)
# %%
with open(mod_wrfout, 'rb') as t:
    results_mod = pickle.load(t)
    locals().update(results_mod)
# %% Making a new plot of just the wrfout to see what it looks like
n = 10
#I chose 10 here since the data is taken at 10Hz, so this way I can see what it is like every second

wrfout = nc.Dataset('/home/jbenik/FireFlux2/Codes_and_Data/Data/wrf_files/wrfout_files/wrfout_d01_2013-01-30_15:00:00', 'r')
time = wrfout.variables['XTIME'][:]
time2 = np.arange(240, 420.01, .1)

print("Plotting")
fig, ax  = plt.subplots(2, 3, figsize = (15, 10))
plt.suptitle("Wind Speeds at the Main tower from wrfout file", fontsize = 15, fontweight = 'bold')
fig.patch.set_facecolor('white')
# 20 meters
ax[0, 0].plot(wrfout_time, ws_h_20, label = 'wrfout file', color = 'red')
#ax[0, 0].plot(np.array(wrfout.variables['XTIME'][:]), ws_h_20.rolling(window = n).mean(), label = 'Average Winds', color = 'black')
ax[0, 0].set_xlabel('Time (Minutes)', fontsize = 12)
ax[0, 0].set_ylabel('Wind Speed (m/s)', fontsize = 12)
#ax[0, 0].set_xlim(230, 420)
ax[0, 0].set_title("Wind Speed at 20 Meters", fontsize = 15, fontweight = 'bold')
ax[0, 0].legend()

ax[0, 1].plot(wrfout_time, ws_h_10, label = 'wrfout file', color = 'red')
#ax[0, 1].plot(np.array(wrfout.variables['XTIME'][:]), ws_h_10.rolling(window = n).mean(), label = 'wrfout file', color = 'black')
ax[0, 1].set_title("Wind Speed at 10 Meters", fontsize = 15, fontweight = 'bold')
ax[0, 1].set_xlabel('Time (Minutes)', fontsize = 12)
ax[0, 1].set_ylabel('Wind Speed (m/s)', fontsize = 12)
#ax[0, 1].set_xlim(230, 420)
ax[0, 1].legend()


ax[0, 2].plot(wrfout_time, ws_h_577, label = 'wrfout file', color = 'red')
#ax[0, 2].plot(np.array(wrfout.variables['XTIME'][:]), ws_h_577.rolling(window = n).mean(), label = 'wrfout file', color = 'black')
ax[0, 2].set_xlabel('Time (Minutes)', fontsize = 12)
ax[0, 2].set_ylabel('Wind Speed (m/s)', fontsize = 12)
#ax[0, 2].set_xlim(230, 420)
ax[0, 2].set_title("Wind Speed at 5.77 Meters", fontsize = 15, fontweight = 'bold')
ax[0, 2].legend()


ax[1, 0].plot(wrfout_time, W_h_20, color = 'red', label = 'wrfout file')
#ax[2, 0].plot(np.array(wrfout.variables['XTIME'][:]), W_h_20.rolling(window = n).mean(), color = 'black', label = 'wrfout file')
ax[1, 0].set_xlabel('Time (Minutes)', fontsize = 12)
ax[1, 0].set_ylabel('Wind Speed (m/s)', fontsize = 12)
ax[1, 0].set_title("W Wind Speed at 20 Meters", fontsize = 15, fontweight = 'bold')
#ax[1, 0].set_xlim(230, 420)
ax[1, 0].legend()

ax[1, 1].plot(wrfout_time, W_h_10, color = 'red', label = 'wrfout file')
#ax[2, 1].plot(np.array(wrfout.variables['XTIME'][:]), W_h_10.rolling(window = n).mean(), color = 'black', label = 'wrfout file')
ax[1, 1].set_xlabel('Time (Minutes)', fontsize = 12)
ax[1, 1].set_ylabel('Wind Speed (m/s)', fontsize = 12)
ax[1, 1].set_title("W Wind Speed at 10 Meters", fontsize = 15, fontweight = 'bold')
#ax[1, 1].set_xlim(230, 420)
ax[1, 1].legend()


ax[1, 2].plot(wrfout_time, W_h_577, color = 'red', label = 'wrfout file')
#ax[2, 2].plot(np.array(wrfout.variables['XTIME'][:]), W_h_577.rolling(window = n).mean(), color = 'black', label = 'wrfout file')
ax[1, 2].set_xlabel('Time (Minutes)', fontsize = 12)
ax[1, 2].set_ylabel('Wind Speed (m/s)', fontsize = 12)
ax[1, 2].set_title("W Wind Speed at 5.77 Meters", fontsize = 15, fontweight = 'bold')
#ax[1, 2].set_xlim(230, 420)
ax[1, 2].legend()


ax[0, 0].grid()
ax[0, 1].grid()
ax[0, 2].grid()
ax[1, 0].grid()
ax[1, 1].grid()
ax[1, 2].grid()

plt.tight_layout()
#plt.savefig('/home/jbenik/FireFlux2/Codes_and_Data/Data/images/wrfout_Main_tower_wind_ideal_new_backfire.png')
plt.show()
plt.pause(0.0001)
plt.close()
# %%


# %% Making the plots
#defining n which is the number of intervals for the rolling average
n = 10
#I chose 10 here since the data is taken at 10Hz, so this way I can see what it is like every second
wrfout_time = wrfout_time[240:420] * 60
print("Plotting")
fig, ax  = plt.subplots(2, 3, figsize = (15, 10))
plt.suptitle("Wind Speeds at the Main tower comapred to the wrfout file", fontsize = 15, fontweight = 'bold')
fig.patch.set_facecolor('white')
# 20 meters
ax[0, 0].plot(wrfout_time, ws_h_20[240:420], label = 'wrfout file', color = 'red')
#ax[0, 0].plot(np.array(wrfout.variables['XTIME'][:]), ws_h_20.rolling(window = n).mean(), label = 'Average Winds', color = 'black')
ax[0, 0].plot(time2, ws_20, color = 'blue', label = 'Main Tower Data')
ax[0, 0].plot(time2, ws_20.rolling(window = n).mean(), color = 'black', label = 'Rolling Average', linestyle = '--')
ax[0, 0].set_xlabel('Time (seconds)', fontsize = 12)
ax[0, 0].set_ylabel('Wind Speed (m/s)', fontsize = 12)
ax[0, 0].set_xlim(230, 420)
ax[0, 0].set_title("Wind Speed at 20 Meters", fontsize = 15, fontweight = 'bold')
ax[0, 0].legend()

ax[0, 1].plot(wrfout_time, ws_h_10[240:420], label = 'wrfout file', color = 'red')
ax[0, 1].plot(time2, ws_10, color = 'blue', label = 'Main Tower Data')
ax[0, 1].plot(time2, ws_10.rolling(window = n).mean(), color = 'black', label = 'Rolling Average', linestyle = '--')
#ax[0, 1].plot(np.array(wrfout.variables['XTIME'][:]), ws_h_10.rolling(window = n).mean(), label = 'wrfout file', color = 'black')
ax[0, 1].set_title("Wind Speed at 10 Meters", fontsize = 15, fontweight = 'bold')
ax[0, 1].set_xlabel('Time (seconds)', fontsize = 12)
ax[0, 1].set_ylabel('Wind Speed (m/s)', fontsize = 12)
ax[0, 1].set_xlim(230, 420)
ax[0, 1].legend()


ax[0, 2].plot(time2, ws_6, color = 'blue', label = 'Main Tower Data')
ax[0, 2].plot(time2, ws_6.rolling(window = n).mean(), color = 'black', label = 'Rolling Average', linestyle = '--')
ax[0, 2].plot(wrfout_time, ws_h_577[240:420], label = 'wrfout file', color = 'red')
#ax[0, 2].plot(np.array(wrfout.variables['XTIME'][:]), ws_h_577.rolling(window = n).mean(), label = 'wrfout file', color = 'black')
ax[0, 2].set_xlabel('Time (seconds)', fontsize = 12)
ax[0, 2].set_ylabel('Wind Speed (m/s)', fontsize = 12)