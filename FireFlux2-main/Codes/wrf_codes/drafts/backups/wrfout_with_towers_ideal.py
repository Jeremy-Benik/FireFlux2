'''The purpose of this code is to plot the wrfout file compared to the tower data. the wrfout used in this case was from the modified input sounding run
and the towers were found using the google earth file and finding the closest point to them.'''
# -*- coding: utf-8 -*-
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
                    after=np.where(main_tower1['TIMESTAMP'] == '1/30/2013  15:06:00')[0][0])
# Wrfout file 
print(" Reading in the wrfout file from the ideal case")
wrfout = nc.Dataset('/home/jbenik/FireFlux2/Codes_and_Data/Data/wrf_files/wrfout_d01_2013-01-30_15:00:00', 'r')
wrfout_xr = xr.open_dataset('/home/jbenik/FireFlux2/Codes_and_Data/Data/wrf_files/wrfout_d01_2013-01-30_15:00:00')

# %% Getting the variables from the files
# Main tower variables
print("Getting the variables from the main tower data")
time_main_tower = main_tower['TIMESTAMP']
time2 = np.arange(240, 360.01, .1)

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
print("W wind is done, now I am getting Temperature")
T_wrfout = wrf.getvar(wrfout, "temp", None, units = 'K')
T_wrfout -= 273.15 #converting it to celcius
print("Now I am getting height")
ht = wrf.getvar(wrfout, "z", units="m", msl = False)
# %% Interpolating the variables to specific heights

# 20 meters
print("Interpolating heights")
print("Interpolating U at 20 meters")
U_h_20 = wrf.interplevel(u_wrfout, ht, 20)[240:360, y_main, x_main]
print("Interpolating V at 20 meters")
V_h_20 = wrf.interplevel(v_wrfout, ht, 20)[240:360, y_main, x_main]
print("Calculating Wind Speed")
ws_h_20 = np.sqrt((U_h_20 ** 2) + (V_h_20 ** 2))
print("Interpolating W at 20 meters")
W_h_20 = wrf.interplevel(w_wrfout, ht, 20)[240:360, y_main, x_main]
print("Interpolating T at 20 meters")
T_h_20 = wrf.interplevel(T_wrfout, ht, 20)[240:360, y_main, x_main]

# 10 meters
print("Interpolating U at 10 meters")
U_h_10 = wrf.interplevel(u_wrfout, ht, 10)[240:360, y_main, x_main]
V_h_10 = wrf.interplevel(v_wrfout, ht, 10)[240:360, y_main, x_main]
ws_h_10 = np.sqrt((U_h_10 ** 2) + (V_h_10 ** 2))
W_h_10 = wrf.interplevel(w_wrfout, ht, 10)[240:360, y_main, x_main]
T_h_10 = wrf.interplevel(T_wrfout, ht, 10)[240:360, y_main, x_main]

# 5.77 meters
U_h_577 = wrf.interplevel(u_wrfout, ht, 5.77)[240:360, y_main, x_main]
V_h_577 = wrf.interplevel(v_wrfout, ht, 5.77)[240:360, y_main, x_main]
ws_h_577 = np.sqrt((U_h_577 ** 2) + (V_h_577 ** 2))
W_h_577 = wrf.interplevel(w_wrfout, ht, 5.77)[240:360, y_main, x_main]
T_h_577 = wrf.interplevel(T_wrfout, ht, 5.77)[240:360, y_main, x_main]
# %% Making the plots
#defining n which is the number of intervals for the rolling average
n = 10
#I chose 10 here since the data is taken at 10Hz, so this way I can see what it is like every second

print("Plotting")
fig, ax  = plt.subplots(3, 3, figsize = (20, 20))
plt.suptitle("Wind Speeds and Temperature at the Main tower comapred to the wrfout file")

# 20 meters
ax[0, 0].plot(np.array(wrfout.variables['XTIME'][240:360]) * 60, ws_h_20, label = 'wrfout file Wind Speed (m/s)', color = 'red')
#ax[0, 0].plot(np.array(wrfout.variables['XTIME'][:]), ws_h_20.rolling(window = n).mean(), label = 'Average Winds', color = 'black')
ax[0, 0].plot(time2, ws_20, color = 'blue', label = 'Main Tower Data (20 meters)')
ax[0, 0].plot(time2, ws_20.rolling(window = n).mean(), color = 'black', label = '20m Rolling Average Winds')
ax[0, 0].set_xlabel('Time (seconds)', fontsize = 10, )
ax[0, 0].set_ylabel('Wind Speed (m/s)', fontsize = 10, )
ax[0, 0].set_xlim(220, 350)
ax[0, 0].set_title("Wind Speed at 20 Meters", fontsize = 12, )
ax[0, 0].legend()

ax[0, 1].plot(np.array(wrfout.variables['XTIME'][240:360]) * 60, ws_h_10, label = 'wrfout file', color = 'red')
ax[0, 1].plot(time2, ws_10, color = 'blue', label = 'Main Tower Data (10 meters)')
ax[0, 1].plot(time2, ws_10.rolling(window = n).mean(), color = 'black', label = '20m Rolling Average Winds')
#ax[0, 1].plot(np.array(wrfout.variables['XTIME'][:]), ws_h_10.rolling(window = n).mean(), label = 'wrfout file', color = 'black')
ax[0, 1].set_title("Wind Speed at 10 Meters", fontsize = 10)
ax[0, 1].set_xlabel('Time (seconds)', fontsize = 10)
ax[0, 1].set_ylabel('Wind Speed (m/s)', fontsize = 10)
ax[0, 1].set_xlim(220, 350)
ax[0, 1].legend()


ax[0, 2].plot(time2, ws_6, color = 'blue', label = 'Main Tower Data (5.77 meters)')
ax[0, 2].plot(time2, ws_6.rolling(window = n).mean(), color = 'black', label = 'Main Tower Data (5.77 meters)')
ax[0, 2].plot(np.array(wrfout.variables['XTIME'][240:360]) * 60, ws_h_577, label = 'wrfout file', color = 'red')
#ax[0, 2].plot(np.array(wrfout.variables['XTIME'][:]), ws_h_577.rolling(window = n).mean(), label = 'wrfout file', color = 'black')
ax[0, 2].set_xlabel('Time (seconds)', fontsize = 10)
ax[0, 2].set_ylabel('Wind Speed (m/s)', fontsize = 10)
ax[0, 2].set_xlim(220, 350)
ax[0, 2].set_title("Wind Speed at 5.77 Meters", fontsize = 10)
ax[0, 2].legend()


ax[1, 0].plot(time2, ts20, color = 'blue', label = 'Main tower Data (Temperature at 20 meters)')
ax[1, 0].plot(time2, ts20.rolling(window = n).mean(), color = 'black', label = 'Main tower Data (Temperature at 20 meters)')
ax[1, 0].plot(np.array(wrfout.variables['XTIME'][240:360]) * 60, T_h_20, color = 'red', label = 'wrfout file')
#ax[1, 0].plot(np.array(wrfout.variables['XTIME'][:]), T_h_20.rolling(window = n).mean(), color = 'black', label = 'wrfout file')
ax[1, 0].set_xlabel('Time (seconds)', fontsize = 10)
ax[1, 0].set_ylabel('Temperature (C)', fontsize = 10)
ax[1, 0].set_title("Temperature at 20 Meters", fontsize = 10)
ax[1, 0].set_xlim(220, 350)
ax[1, 0].legend()

ax[1, 1].plot(time2, ts10, color = 'blue', label = 'Main tower Data (Temperature at 10 meters)')
ax[1, 1].plot(time2, ts10.rolling(window = n).mean(), color = 'black', label = 'Main tower Data (Temperature at 10 meters)')
ax[1, 1].plot(np.array(wrfout.variables['XTIME'][240:360]) * 60, T_h_10, color = 'red', label = 'wrfout file')
#ax[1, 1].plot(np.array(wrfout.variables['XTIME'][:]), T_h_10.rolling(window = n).mean(), color = 'black', label = 'wrfout file')
ax[1, 1].set_xlabel('Time (seconds)', fontsize = 10)
ax[1, 1].set_ylabel('Temperature (C)', fontsize = 10)
ax[1, 1].set_title("Temperature at 10 Meters", fontsize = 10)
ax[1, 1].set_xlim(220, 350)
ax[1, 1].legend()

ax[1, 2].plot(time2, ts6, color = 'blue', label = 'Main tower Data (Temperature at 5.77 meters)')
ax[1, 2].plot(time2, ts6.rolling(window = n).mean(), color = 'black', label = 'Main tower Data (Temperature at 5.77 meters)')
ax[1, 2].plot(np.array(wrfout.variables['XTIME'][240:360]) * 60, T_h_577, color = 'red', label = 'wrfout file')
#ax[1, 2].plot(np.array(wrfout.variables['XTIME'][:]), T_h_577.rolling(window = n).mean(), color = 'black', label = 'wrfout file')
ax[1, 2].set_xlabel('Time (seconds)', fontsize = 10, )
ax[1, 2].set_ylabel('Temperature (C)', fontsize = 10, )
ax[1, 2].set_title("Temperature at 5.77 Meters", fontsize = 10)
ax[1, 2].set_xlim(220, 350)
ax[1, 2].legend()


ax[2, 0].plot(time2, uz20, color = 'blue', label = 'Main tower Data (W wind 20 meters)')
ax[2, 0].plot(time2, uz20.rolling(window = n).mean(), color = 'black', label = 'Main tower Data (W wind 20 meters)')
ax[2, 0].plot(np.array(wrfout.variables['XTIME'][240:360]) * 60, W_h_20, color = 'red', label = 'wrfout file')
#ax[2, 0].plot(np.array(wrfout.variables['XTIME'][:]), W_h_20.rolling(window = n).mean(), color = 'black', label = 'wrfout file')
ax[2, 0].set_xlabel('Time (seconds)', fontsize = 10)
ax[2, 0].set_ylabel('Wind Speed (m/s)', fontsize = 10)
ax[2, 0].set_title("W Wind Speed at 20 Meters", fontsize = 10)
ax[2, 0].set_xlim(220, 350)
ax[2, 0].legend()

ax[2, 1].plot(time2, uz10, color = 'blue', label = 'Main tower Data (W wind 10 meters)')
ax[2, 1].plot(time2, uz10.rolling(window = n).mean(), color = 'black', label = 'Main tower Data (W wind 10 meters)')
ax[2, 1].plot(np.array(wrfout.variables['XTIME'][240:360]) * 60, W_h_10, color = 'red', label = 'wrfout file')
#ax[2, 1].plot(np.array(wrfout.variables['XTIME'][:]), W_h_10.rolling(window = n).mean(), color = 'black', label = 'wrfout file')
ax[2, 1].set_xlabel('Time (seconds)', fontsize = 10)
ax[2, 1].set_ylabel('Wind Speed (m/s)', fontsize = 10)
ax[2, 1].set_title("W Wind Speed at 10 Meters", fontsize = 10)
ax[2, 1].set_xlim(220, 350)
ax[2, 1].legend()
ax[2, 1].grid()



ax[2, 2].plot(time2, uz6, color = 'blue', label = 'Main tower Data (W wind 5.77 meters)')
ax[2, 2].plot(time2, uz6.rolling(window = n).mean(), color = 'black', label = 'Main tower Data (W wind 5.77 meters)')
ax[2, 2].plot(np.array(wrfout.variables['XTIME'][240:360]) * 60, W_h_577, color = 'red', label = 'wrfout file')
#ax[2, 2].plot(np.array(wrfout.variables['XTIME'][:]), W_h_577.rolling(window = n).mean(), color = 'black', label = 'wrfout file')
ax[2, 2].set_xlabel('Time (seconds)', fontsize = 10)
ax[2, 2].set_ylabel('Wind Speed (m/s)', fontsize = 10)
ax[2, 2].set_title("W Wind Speed at 5.77 Meters", fontsize = 10)
ax[2, 2].set_xlim(220, 350)
ax[2, 2].legend()


ax[0, 0].grid()
ax[0, 1].grid()
ax[0, 2].grid()
ax[1, 0].grid()
ax[1, 1].grid()
ax[1, 2].grid()
ax[2, 0].grid()
ax[2, 1].grid()
ax[2, 2].grid()

plt.tight_layout()
plt.savefig('/home/jbenik/FireFlux2/Codes_and_Data/Data/wrf_files/images/wrfout_main_tower_ideal.png')
plt.show()
plt.pause(0.0001)
plt.close()
# %% Short towers
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
uw = df_w['u']
vw = df_w['v']
ww = df_w['w']
tw = df_w['t']
wsw = np.sqrt((uw ** 2) + (vw ** 2))
#east tower
print("Reading in variables from east tower")
time_short_tower_e = df_e['TIMESTAMP']
ue = df_e['u']
ve = df_e['v']
we = df_e['w']
te = df_e['t']
wse = np.sqrt((ue ** 2) + (ve ** 2))
#south tower
print("reading in variables from south tower")
time_short_tower_s = df_s['TIMESTAMP']
us = df_s['u']
vs = df_s['v']
ws = df_s['w']
ts = df_s['t']
wss = np.sqrt((us ** 2) + (vs ** 2))

# Interpolating the vars to heights and defining the location of them
#west tower is at 5.33m
#east tower is at 5.28 meters
#south tower is at 5.33m
# %% Getting locations of the towers then assigning variables to them

#west tower
print('Interpolating west tower at 5.33 meters')
Uw_h_533 = wrf.interplevel(u_wrfout, ht, 5.33)[240:841, y_west, x_west]
Vw_h_533 = wrf.interplevel(v_wrfout, ht, 5.33)[240:841, y_west, x_west]
wsw_h_33 = np.sqrt((Uw_h_533 ** 2) + (Vw_h_533 ** 2))
Ww_h_533 = wrf.interplevel(w_wrfout, ht, 5.33)[240:841, y_west, x_west]
Tw_h_533 = wrf.interplevel(T_wrfout, ht, 5.33)[240:841, y_west, x_west]

#east tower
print('Interpolating the east tower at 5.28 meters')
Ue_h_528 = wrf.interplevel(u_wrfout, ht, 5.28)[240:841, y_east, x_east]
Ve_h_528 = wrf.interplevel(v_wrfout, ht, 5.28)[240:841, y_east, x_east]
wse_h_528 = np.sqrt((Ue_h_528 ** 2) + (Ve_h_528 ** 2))
We_h_528 = wrf.interplevel(w_wrfout, ht, 5.28)[240:841, y_east, x_east]
Te_h_528 = wrf.interplevel(T_wrfout, ht, 5.28)[240:841, y_east, x_east]


#south tower
print('interpolating the south tower at 5.33 meters')
Us_h_533 = wrf.interplevel(u_wrfout, ht, 5.33)[240:841, y_south, x_south]
Vs_h_533 = wrf.interplevel(v_wrfout, ht, 5.33)[240:841, y_south, x_south]
wss_h_533 = np.sqrt((Us_h_533 ** 2) + (Vs_h_533 ** 2))
Ws_h_533 = wrf.interplevel(w_wrfout, ht, 5.33)[240:841, y_south, x_south]
Ts_h_533 = wrf.interplevel(T_wrfout, ht, 5.33)[240:841, y_south, x_south]

# %% Creating a plot for the short towers
print("Creating the plot")
fig, ax = plt.subplots(3, 3, figsize = (12, 12))
# Plotting the west tower first
#wind speed
ax[0, 0].plot(np.arange(240, 841), wsw, color = 'blue', label = 'West Tower Wind Speed (m/s)') #plotting the wind speed from west tower
ax[0, 0].plot(np.arange(240, 841), wsw.rolling(window = n).mean(), color = 'black', label = 'Rolling Average') #plotting the rolling average from the west tower wind speed
ax[0, 0].plot(np.array(wrfout.variables['XTIME'][240:841]) * 60, Ws_h_533, color = 'red', label = 'wrfout file Wind Speed (m/s)') #plotting the wind speed from the wrfout file
ax[0, 0].set_xlabel('Time', fontsize = 10)
ax[0, 0].set_ylabel('Wind Speed (m/s)', fontsize = 10)
ax[0, 0].set_title('West Tower Wind Speed vs. wrfout', fontsize = 10)
# w wind
ax[0, 1].plot(np.arange(240, 841), ww, color = 'blue', label = 'West Tower W Wind Speed (m/s)') #plotting the wind speed from west tower
ax[0, 1].plot(np.arange(240, 841), ww.rolling(window = n).mean(), color = 'black', label = 'West Tower Rolling Average') #plotting the rolling average from the west tower wind speed
ax[0, 1].plot(np.array(wrfout.variables['XTIME'][240:841]) * 60, Ww_h_533, color = 'red', label = 'wrfout file W Wind (m/s)') #plotting the wind speed from the wrfout file
ax[0, 1].set_xlabel('Time', fontsize = 10)
ax[0, 1].set_ylabel('Wind Speed (m/s)', fontsize = 10)
ax[0, 1].set_title('West Tower W Wind vs. wrfout', fontsize = 10)
#temperature
ax[0, 2].plot(np.arange(240, 841), tw, color = 'blue', label = 'West Tower Temp (\N{DEGREE SIGN}C)') #plotting the wind speed from west tower
ax[0, 2].plot(np.arange(240, 841), tw.rolling(window = n).mean(), color = 'black', label = 'West Tower Rolling Average') #plotting the rolling average from the west tower wind speed
ax[0, 2].plot(np.array(wrfout.variables['XTIME'][240:841] * 60), Tw_h_533, color = 'red', label = 'wrfout file Temperature') #plotting the wind speed from the wrfout file
ax[0, 2].set_xlabel('Time', fontsize = 10)
ax[0, 2].set_ylabel('Temperature (\N{DEGREE SIGN}C)', fontsize = 10)
ax[0, 2].set_title('West Tower Temperature (\N{DEGREE SIGN}C) vs. wrfout', fontsize = 10)

# Plotting the South Tower
#wind speed
ax[1, 0].plot(np.arange(240, 841), wss, color = 'blue', label = 'South Tower Wind Speed (m/s)') #plotting the wind speed from South tower
ax[1, 0].plot(np.arange(240, 841), wss.rolling(window = n).mean(), color = 'black', label = 'South Tower Rolling Average') #plotting the rolling average from the South tower wind speed
ax[1, 0].plot(np.array(wrfout.variables['XTIME'][240:841]) * 60, wss_h_533, color = 'red', label = 'wrfout file Wind Speed (m/s)') #plotting the wind speed from the wrfout file
ax[1, 0].set_xlabel('Time', fontsize = 10)
ax[1, 0].set_ylabel('Wind Speed (m/s)', fontsize = 10)
ax[1, 0].set_title('South Tower Wind Speed vs. wrfout', fontsize = 10)
# w wind
ax[1, 1].plot(np.arange(240, 841), ws, color = 'blue', label = 'South Tower W Wind Speed (m/s)') #plotting the wind speed from South tower
ax[1, 1].plot(np.arange(240, 841), ws.rolling(window = n).mean(), color = 'black', label = 'South Tower Rolling Average') #plotting the rolling average from the South tower wind speed
ax[1, 1].plot(np.array(wrfout.variables['XTIME'][240:841]) * 60, Ws_h_533, color = 'red', label = 'wrfout file W Wind (m/s)') #plotting the wind speed from the wrfout file
ax[1, 1].set_xlabel('Time', fontsize = 10)
ax[1, 1].set_ylabel('Wind Speed (m/s)', fontsize = 10)
ax[1, 1].set_title('South Tower W Wind vs. wrfout', fontsize = 10)
#temperature
ax[1, 2].plot(np.arange(240, 841), ts, color = 'blue', label = 'South Tower Temp (\N{DEGREE SIGN}C)') #plotting the wind speed from South tower
ax[1, 2].plot(np.arange(240, 841), ts.rolling(window = n).mean(), color = 'black', label = 'South Tower Rolling Average') #plotting the rolling average from the South tower wind speed
ax[1, 2].plot(np.array(wrfout.variables['XTIME'][240:841]) * 60, Ts_h_533, color = 'red', label = 'wrfout file Temperature') #plotting the wind speed from the wrfout file
ax[1, 2].set_xlabel('Time', fontsize = 10)
ax[1, 2].set_ylabel('Wind Speed (m/s)', fontsize = 10)
ax[1, 2].set_title('South Tower Temperature (\N{DEGREE SIGN}C) vs. wrfout', fontsize = 10)

# Plotting the East Tower
#wind speed
ax[2, 0].plot(np.arange(240, 841), wse, color = 'blue', label = 'East Tower Wind Speed (m/s)') #plotting the wind speed from South tower
ax[2, 0].plot(np.arange(240, 841), wse.rolling(window = n).mean(), color = 'black', label = 'East Tower Rolling Average') #plotting the rolling average from the South tower wind speed
ax[2, 0].plot(np.array(wrfout.variables['XTIME'][240:841]) * 60, wse_h_528, color = 'red', label = 'wrfout file Wind Speed (m/s)') #plotting the wind speed from the wrfout file
ax[2, 0].set_xlabel('Time', fontsize = 10)
ax[2, 0].set_ylabel('Wind Speed (m/s)', fontsize = 10)
ax[2, 0].set_title('East Tower Wind Speed vs. wrfout', fontsize = 10)
# w wind
ax[2, 1].plot(np.arange(240, 841), we, color = 'blue', label = 'East Tower W Wind Speed (m/s)') #plotting the wind speed from South tower
ax[2, 1].plot(np.arange(240, 841), we.rolling(window = n).mean(), color = 'black', label = 'East Tower Rolling Average') #plotting the rolling average from the South tower wind speed
ax[2, 1].plot(np.array(wrfout.variables['XTIME'][240:841]) * 60, We_h_528, color = 'red', label = 'wrfout file W Wind (m/s)') #plotting the wind speed from the wrfout file
ax[2, 1].set_xlabel('Time', fontsize = 10)
ax[2, 1].set_ylabel('Wind Speed (m/s)', fontsize = 10)
ax[2, 1].set_title('East Tower W Wind vs. wrfout', fontsize = 10)
#temperature
ax[2, 2].plot(np.arange(240, 841), te, color = 'blue', label = 'East Tower Temp (\N{DEGREE SIGN}C)') #plotting the wind speed from South tower
ax[2, 2].plot(np.arange(240, 841), te.rolling(window = n).mean(), color = 'black', label = 'East Tower Rolling Average') #plotting the rolling average from the South tower wind speed
ax[2, 2].plot(np.array(wrfout.variables['XTIME'][240:841]) * 60, Te_h_528, color = 'red', label = 'wrfout file Temperature (\N{DEGREE SIGN}C)') #plotting the wind speed from the wrfout file
ax[2, 2].set_xlabel('Time', fontsize = 10)
ax[2, 2].set_ylabel('Temperature (\N{DEGREE SIGN}C)', fontsize = 10)
ax[2, 2].set_title('East Tower Temperature (\N{DEGREE SIGN}C) vs. wrfout', fontsize = 10)


ax[0, 0].grid()
ax[0, 1].grid()
ax[0, 2].grid()
ax[1, 0].grid()
ax[1, 1].grid()
ax[1, 2].grid()
ax[2, 0].grid()
ax[2, 1].grid()
ax[2, 2].grid()


plt.tight_layout()
plt.savefig('/home/jbenik/FireFlux2/Codes_and_Data/Data/wrf_files/images/wrfout_short_towers2_ideal.png')
plt.show()
plt.pause(0.0001)
plt.close()

