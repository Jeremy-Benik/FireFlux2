''' This program plots the wind speeds at the main tower compared to the wrfout file'''

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
# %% Assigning tower coords
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
print("Main tower data")
main_tower1 = pd.read_csv('/home/jbenik/FireFlux2/Codes_and_Data/Data/Main_Tower_Data/Proc_FF2_10HzMTdespiked_rotated.csv', parse_dates=['TIMESTAMP'], skiprows = (0, 2, 3))

main_tower = main_tower1.truncate(before= np.where(main_tower1['TIMESTAMP'] == '1/30/2013  15:04:00')[0][0], 
                    after=np.where(main_tower1['TIMESTAMP'] == '1/30/2013  15:07:00')[0][0])
# Wrfout file 
print(" Reading in the wrfout file from the ideal case")
wrfout = nc.Dataset('/home/jbenik/FireFlux2/Codes_and_Data/Data/wrf_files/wrfout_files/wrfout_d01_2013-01-30_15:00:00', 'r')
wrfout_xr = xr.open_dataset('/home/jbenik/FireFlux2/Codes_and_Data/Data/wrf_files/wrfout_files/wrfout_d01_2013-01-30_15:00:00')

# %% Getting the variables from the files
# Main tower variables
print("Getting the variables from the main tower data")
time_main_tower = main_tower['TIMESTAMP']
time2 = np.arange(240, 420.01, .1)

print('20 meter variables')
ux20 = main_tower['Ux_20m']
uy20 = main_tower['Uy_20m']
ws_20 = np.sqrt((ux20 ** 2) + (uy20 ** 2))
uz20 = main_tower['Uz_20m']
ts20 = main_tower['Ts_20m']

print('10 meter variables')
ux10 = main_tower['Ux_10m']
uy10 = main_tower['Uy_10m']
ws_10 = np.sqrt((ux10 ** 2) + (uy10 ** 2))
uz10 = main_tower['Uz_10m']
ts10 = main_tower['Ts_10m']

print('5.77 meter variable')
ux6 = main_tower['Ux_6m']
uy6 = main_tower['Uy_6m']
ws_6 = np.sqrt((ux6 ** 2) + (uy6 ** 2))
uz6 = main_tower['Uz_6m']
ts6 = main_tower['Ts_6m']
# %% Variables from the wrfout file
# To get the variables from thw wrfout file, I am using the wrf library to get them so they won't be staggered in the grid
time = wrfout.variables['XTIME'][:]
print("I am getting the u variable from the wrfout file")
u_wrfout = wrf.getvar(wrfout, "ua", None, units = "m/s")
print("U wind is done, now I am getting the V wind")
v_wrfout = wrf.getvar(wrfout, "va", None, units = "m/s")
print("V wind is done, now I am getting the W wind")
w_wrfout = wrf.getvar(wrfout, "wa", None, units = "m/s")
print("Now I am getting height")
ht = wrf.getvar(wrfout, "z", units="m", msl = False)
# %% Interpolating the variables to specific heights

# 20 meters
print("Interpolating heights")
print("Interpolating U at 20 meters")
U_h_20 = wrf.interplevel(u_wrfout, ht, 20)[240:420, y_main, x_main]
print("Interpolating V at 20 meters")
V_h_20 = wrf.interplevel(v_wrfout, ht, 20)[240:420, y_main, x_main]
print("Calculating Wind Speed")
ws_h_20 = np.sqrt((U_h_20 ** 2) + (V_h_20 ** 2))
print("Interpolating W at 20 meters")
W_h_20 = wrf.interplevel(w_wrfout, ht, 20)[240:420, y_main, x_main]

# 10 meters
print("Interpolating U at 10 meters")
U_h_10 = wrf.interplevel(u_wrfout, ht, 10)[240:420, y_main, x_main]
V_h_10 = wrf.interplevel(v_wrfout, ht, 10)[240:420, y_main, x_main]
ws_h_10 = np.sqrt((U_h_10 ** 2) + (V_h_10 ** 2))
W_h_10 = wrf.interplevel(w_wrfout, ht, 10)[240:420, y_main, x_main]

# 5.77 meters
print('Interpolating U at 5.77 meters')
U_h_577 = wrf.interplevel(u_wrfout, ht, 5.77)[240:420, y_main, x_main]
V_h_577 = wrf.interplevel(v_wrfout, ht, 5.77)[240:420, y_main, x_main]
ws_h_577 = np.sqrt((U_h_577 ** 2) + (V_h_577 ** 2))
W_h_577 = wrf.interplevel(w_wrfout, ht, 5.77)[240:420, y_main, x_main]
# %% Making the plots
#defining n which is the number of intervals for the rolling average
n = 10
#I chose 10 here since the data is taken at 10Hz, so this way I can see what it is like every second

print("Plotting")
fig, ax  = plt.subplots(2, 3, figsize = (15, 10))
plt.suptitle("Wind Speeds at the Main tower comapred to the wrfout file", fontsize = 15, fontweight = 'bold')
fig.patch.set_facecolor('white')
# 20 meters
ax[0, 0].plot(np.array(wrfout.variables['XTIME'][240:420]) * 60, ws_h_20, label = 'wrfout file', color = 'red')
#ax[0, 0].plot(np.array(wrfout.variables['XTIME'][:]), ws_h_20.rolling(window = n).mean(), label = 'Average Winds', color = 'black')
ax[0, 0].plot(time2, ws_20, color = 'blue', label = 'Main Tower Data')
ax[0, 0].plot(time2, ws_20.rolling(window = n).mean(), color = 'black', label = 'Rolling Average', linestyle = '--')
ax[0, 0].set_xlabel('Time (seconds)', fontsize = 12)
ax[0, 0].set_ylabel('Wind Speed (m/s)', fontsize = 12)
ax[0, 0].set_xlim(230, 420)
ax[0, 0].set_title("Wind Speed at 20 Meters", fontsize = 15, fontweight = 'bold')
ax[0, 0].legend()

ax[0, 1].plot(np.array(wrfout.variables['XTIME'][240:420]) * 60, ws_h_10, label = 'wrfout file', color = 'red')
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
ax[0, 2].plot(np.array(wrfout.variables['XTIME'][240:420]) * 60, ws_h_577, label = 'wrfout file', color = 'red')
#ax[0, 2].plot(np.array(wrfout.variables['XTIME'][:]), ws_h_577.rolling(window = n).mean(), label = 'wrfout file', color = 'black')
ax[0, 2].set_xlabel('Time (seconds)', fontsize = 12)
ax[0, 2].set_ylabel('Wind Speed (m/s)', fontsize = 12)
ax[0, 2].set_xlim(230, 420)
ax[0, 2].set_title("Wind Speed at 5.77 Meters", fontsize = 15, fontweight = 'bold')
ax[0, 2].legend()


ax[1, 0].plot(time2, uz20, color = 'blue', label = 'Main tower Data')
ax[1, 0].plot(time2, uz20.rolling(window = n).mean(), color = 'black', label = 'Rolling Average', linestyle = '--')
ax[1, 0].plot(np.array(wrfout.variables['XTIME'][240:420]) * 60, W_h_20, color = 'red', label = 'wrfout file')
#ax[2, 0].plot(np.array(wrfout.variables['XTIME'][:]), W_h_20.rolling(window = n).mean(), color = 'black', label = 'wrfout file')
ax[1, 0].set_xlabel('Time (seconds)', fontsize = 12)
ax[1, 0].set_ylabel('Wind Speed (m/s)', fontsize = 12)
ax[1, 0].set_title("W Wind Speed at 20 Meters", fontsize = 15, fontweight = 'bold')
ax[1, 0].set_xlim(230, 420)
ax[1, 0].legend()

ax[1, 1].plot(time2, uz10, color = 'blue', label = 'Main tower Data')
ax[1, 1].plot(time2, uz10.rolling(window = n).mean(), color = 'black', label = 'Rolling Average', linestyle = '--')
ax[1, 1].plot(np.array(wrfout.variables['XTIME'][240:420]) * 60, W_h_10, color = 'red', label = 'wrfout file')
#ax[2, 1].plot(np.array(wrfout.variables['XTIME'][:]), W_h_10.rolling(window = n).mean(), color = 'black', label = 'wrfout file')
ax[1, 1].set_xlabel('Time (seconds)', fontsize = 12)
ax[1, 1].set_ylabel('Wind Speed (m/s)', fontsize = 12)
ax[1, 1].set_title("W Wind Speed at 10 Meters", fontsize = 15, fontweight = 'bold')
ax[1, 1].set_xlim(230, 420)
ax[1, 1].legend()


ax[1, 2].plot(time2, uz6, color = 'blue', label = 'Main tower Data')
ax[1, 2].plot(time2, uz6.rolling(window = n).mean(), color = 'black', label = 'Rolling Average', linestyle = '--')
ax[1, 2].plot(np.array(wrfout.variables['XTIME'][240:420]) * 60, W_h_577, color = 'red', label = 'wrfout file')
#ax[2, 2].plot(np.array(wrfout.variables['XTIME'][:]), W_h_577.rolling(window = n).mean(), color = 'black', label = 'wrfout file')
ax[1, 2].set_xlabel('Time (seconds)', fontsize = 12)
ax[1, 2].set_ylabel('Wind Speed (m/s)', fontsize = 12)
ax[1, 2].set_title("W Wind Speed at 5.77 Meters", fontsize = 15, fontweight = 'bold')
ax[1, 2].set_xlim(230, 420)
ax[1, 2].legend()


ax[0, 0].grid()
ax[0, 1].grid()
ax[0, 2].grid()
ax[1, 0].grid()
ax[1, 1].grid()
ax[1, 2].grid()

plt.tight_layout()
#plt.savefig('/home/jbenik/FireFlux2/Codes_and_Data/Data/wrf_files/images/wrfout_main_tower_winds_ideal.png')
plt.show()
plt.pause(0.0001)
plt.close()
# %%
