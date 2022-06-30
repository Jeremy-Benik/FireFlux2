# -*- coding: utf-8 -*-
"""
Created on Sat March 5 11:36:54 2022

@author: Jeremy Benik
"""
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
# %% Reading in data
# Main Tower Data
print("Reading in the data")
# Wrfout file 
#This file is from a run that didn't complete, I tried to get the one off ember but it wasn't working when I wrote this code. 
print("wrfout file")
wrfout = nc.Dataset('/home/jbenik/FireFlux2/Codes_and_Data/Data/wrf_files/wrfout_d01_2013-01-30_15:00:00', 'r')
wrfout_xr = xr.open_dataset('/home/jbenik/FireFlux2/Codes_and_Data/Data/wrf_files/wrfout_d01_2013-01-30_15:00:00')

wrfin = nc.Dataset('/home/jbenik/FireFlux2/Codes_and_Data/Data/wrf_files/wrfin_d01_real', 'r')

# %% getting the variables
print("Getting time")
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
#ws = np.sqrt((u_wrfout ** 2) + (v_wrfout ** 2))
ht = wrf.getvar(wrfout, "z", units="m", msl = False)
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
south_north_u_w = wrf.ll_to_xy(wrfin, 29.38617222222222, -95.04138611111111, timeidx = 0, squeeze = False, meta = False, stagger = 'u')[1]
west_east_stag_u_w = wrf.ll_to_xy(wrfin, 29.38617222222222, -95.04138611111111, timeidx = 0, squeeze = False, meta = False, stagger = 'u')[0]

south_north_stag_v_w = wrf.ll_to_xy(wrfin, 29.38617222222222, -95.04138611111111, timeidx = 0, squeeze = False, meta = False, stagger = 'v')[1]
west_east_v_w = wrf.ll_to_xy(wrfin, 29.38617222222222, -95.04138611111111, timeidx = 0, squeeze = False, meta = False, stagger = 'v')[0]

south_north_w = wrf.ll_to_xy(wrfin, 29.38617222222222, -95.04138611111111, timeidx = 0, squeeze = False, meta = False, stagger = 'm')[1]
west_east_w = wrf.ll_to_xy(wrfin, 29.38617222222222, -95.04138611111111, timeidx = 0, squeeze = False, meta = False, stagger = 'm')[0]


print('Interpolating west tower at 5.33 meters')
Uw_h_533 = wrf.interplevel(u_wrfout, ht, 5.33)[240:841, south_north_u_w, west_east_stag_u_w]
Vw_h_533 = wrf.interplevel(v_wrfout, ht, 5.33)[240:841, south_north_stag_v_w, west_east_v_w]
wsw_h_533 = np.sqrt((Uw_h_533 ** 2) + (Vw_h_533 ** 2))
Ww_h_533 = wrf.interplevel(w_wrfout, ht, 5.33)[240:841, south_north_w, west_east_w]
Tw_h_533 = wrf.interplevel(T_wrfout, ht, 5.33)[240:841, south_north_w, west_east_w]

#east tower
south_north_u_e = wrf.ll_to_xy(wrfin, 29.38650833333333, -95.0402111111111, timeidx = 0, squeeze = False, meta = False, stagger = 'u')[1]
west_east_stag_u_e = wrf.ll_to_xy(wrfin, 29.38650833333333, -95.0402111111111, timeidx = 0, squeeze = False, meta = False, stagger = 'u')[0]

west_east_u_e = wrf.ll_to_xy(wrfin, 29.38650833333333, -95.0402111111111, timeidx = 0, squeeze = False, meta = False, stagger = 'v')[0]
south_north_stag_v_e = wrf.ll_to_xy(wrfin, 29.38650833333333, -95.0402111111111, timeidx = 0, squeeze = False, meta = False, stagger = 'v')[1]

south_north_e = wrf.ll_to_xy(wrfin, 29.38650833333333, -95.0402111111111, timeidx = 0, squeeze = False, meta = False, stagger = 'm')[1]
west_east_e = wrf.ll_to_xy(wrfin, 29.38650833333333, -95.0402111111111, timeidx = 0, squeeze = False, meta = False, stagger = 'm')[0]

print('Interpolating the east tower at 5.28 meters')
Ue_h_528 = wrf.interplevel(u_wrfout, ht, 5.28)[240:841, south_north_u_e, west_east_stag_u_e]
Ve_h_528 = wrf.interplevel(v_wrfout, ht, 5.28)[240:841, south_north_stag_v_e, west_east_e]
wse_h_528 = np.sqrt((Ue_h_528 ** 2) + (Ve_h_528 ** 2))
We_h_528 = wrf.interplevel(w_wrfout, ht, 5.28)[240:841, south_north_e, west_east_e]
Te_h_528 = wrf.interplevel(T_wrfout, ht, 5.28)[240:841, south_north_e, west_east_e]


#south tower
south_north_u_s = wrf.ll_to_xy(wrfin, 29.384775,-95.0403, timeidx = 0, squeeze = False, meta = False, stagger = 'u')[1]
west_east_stag_u_s = wrf.ll_to_xy(wrfin, 29.384775,-95.0403, timeidx = 0, squeeze = False, meta = False, stagger = 'u')[0]

south_north_stag_v_s = wrf.ll_to_xy(wrfin, 29.384775,-95.0403, timeidx = 0, squeeze = False, meta = False, stagger = 'v')[1]
west_east_v_s = wrf.ll_to_xy(wrfin, 29.384775,-95.0403, timeidx = 0, squeeze = False, meta = False, stagger = 'v')[0]

south_north_s = wrf.ll_to_xy(wrfin, 29.384775,-95.0403, timeidx = 0, squeeze = False, meta = False, stagger = 'm')[1]
west_east_s = wrf.ll_to_xy(wrfin, 29.384775,-95.0403, timeidx = 0, squeeze = False, meta = False, stagger = 'm')[0]

print('interpolating the south tower at 5.33 meters')
Us_h_533 = wrf.interplevel(u_wrfout, ht, 5.33)[240:841, south_north_u_s, west_east_stag_u_s]
Vs_h_533 = wrf.interplevel(v_wrfout, ht, 5.33)[240:841, south_north_stag_v_s, west_east_v_s]
wss_h_533 = np.sqrt((Us_h_533 ** 2) + (Vs_h_533 ** 2))
Ws_h_533 = wrf.interplevel(w_wrfout, ht, 5.33)[240:841, south_north_s, west_east_s]
Ts_h_533 = wrf.interplevel(T_wrfout, ht, 5.33)[240:841, south_north_s, west_east_s]

# %% Creating a plot for the short towers

# %% Creating a plot for the short towers
print("Creating the plot")
fig, ax = plt.subplots(3, 3, figsize = (12, 12))
# Plotting the west tower first
#wind speed
ax[0, 0].plot(np.arange(240, 841), wsw, color = 'blue', label = 'West Tower Wind Speed (m/s)') #plotting the wind speed from west tower
ax[0, 0].plot(np.arange(240, 841), wsw.rolling(window = n).mean(), color = 'black', label = 'West Tower Rolling Average') #plotting the rolling average from the west tower wind speed
ax[0, 0].plot(np.array(wrfout.variables['XTIME'][240:841]) * 60, wsw_h_533, color = 'red', label = 'wrfout file') #plotting the wind speed from the wrfout file
ax[0, 0].set_xlabel('Time', fontsize = 10)
ax[0, 0].set_ylabel('Wind Speed (m/s)', fontsize = 10)
ax[0, 0].set_title('West Tower Wind Speed vs. wrfout', fontsize = 10)
# w wind
ax[0, 1].plot(np.arange(240, 841), ww, color = 'blue', label = 'West Tower W Wind Speed (m/s)') #plotting the wind speed from west tower
ax[0, 1].plot(np.arange(240, 841), ww.rolling(window = n).mean(), color = 'black', label = 'West Tower Rolling Average') #plotting the rolling average from the west tower wind speed
ax[0, 1].plot(np.array(wrfout.variables['XTIME'][240:841]) * 60, Ww_h_533, color = 'red', label = 'wrfout file') #plotting the wind speed from the wrfout file
ax[0, 1].set_xlabel('Time', fontsize = 10)
ax[0, 1].set_ylabel('Wind Speed (m/s)', fontsize = 10)
ax[0, 1].set_title('West Tower W Wind vs. wrfout', fontsize = 10)
#temperature
ax[0, 2].plot(np.arange(240, 841), tw, color = 'blue', label = 'West Tower Temp (C)') #plotting the wind speed from west tower
ax[0, 2].plot(np.arange(240, 841), tw.rolling(window = n).mean(), color = 'black', label = 'West Tower Rolling Average') #plotting the rolling average from the west tower wind speed
ax[0, 2].plot(np.array(wrfout.variables['XTIME'][240:841] * 60), Tw_h_533, color = 'red', label = 'wrfout file') #plotting the wind speed from the wrfout file
ax[0, 2].set_xlabel('Time', fontsize = 10)
ax[0, 2].set_ylabel('Temperature (C)', fontsize = 10)
ax[0, 2].set_title('West Tower Temperature vs. wrfout', fontsize = 10)

# Plotting the South Tower
#wind speed
ax[1, 0].plot(np.arange(240, 841), wss, color = 'blue', label = 'South Tower Wind Speed (m/s)') #plotting the wind speed from South tower
ax[1, 0].plot(np.arange(240, 841), wss.rolling(window = n).mean(), color = 'black', label = 'South Tower Rolling Average') #plotting the rolling average from the South tower wind speed
ax[1, 0].plot(np.array(wrfout.variables['XTIME'][240:841]) * 60, wss_h_533, color = 'red', label = 'wrfout file') #plotting the wind speed from the wrfout file
ax[1, 0].set_xlabel('Time', fontsize = 10)
ax[1, 0].set_ylabel('Wind Speed (m/s)', fontsize = 10)
ax[1, 0].set_title('South Tower Wind Speed vs. wrfout', fontsize = 10)
# w wind
ax[1, 1].plot(np.arange(240, 841), ws, color = 'blue', label = 'South Tower W Wind Speed (m/s)') #plotting the wind speed from South tower
ax[1, 1].plot(np.arange(240, 841), ws.rolling(window = n).mean(), color = 'black', label = 'South Tower Rolling Average') #plotting the rolling average from the South tower wind speed
ax[1, 1].plot(np.array(wrfout.variables['XTIME'][240:841]) * 60, Ws_h_533, color = 'red', label = 'wrfout file') #plotting the wind speed from the wrfout file
ax[1, 1].set_xlabel('Time', fontsize = 10)
ax[1, 1].set_ylabel('Wind Speed (m/s)', fontsize = 10)
ax[1, 1].set_title('South Tower W Wind vs. wrfout', fontsize = 10)
#temperature
ax[1, 2].plot(np.arange(240, 841), ts, color = 'blue', label = 'South Tower Temp (C)') #plotting the wind speed from South tower
ax[1, 2].plot(np.arange(240, 841), ts.rolling(window = n).mean(), color = 'black', label = 'South Tower Rolling Average') #plotting the rolling average from the South tower wind speed
ax[1, 2].plot(np.array(wrfout.variables['XTIME'][240:841]) * 60, Ts_h_533, color = 'red', label = 'wrfout file') #plotting the wind speed from the wrfout file
ax[1, 2].set_xlabel('Time', fontsize = 10)
ax[1, 2].set_ylabel('Temperature (C)', fontsize = 10)
ax[1, 2].set_title('South Tower Temperature vs. wrfout', fontsize = 10)

# Plotting the East Tower
#wind speed
ax[2, 0].plot(np.arange(240, 841), wse, color = 'blue', label = 'East Tower Wind Speed (m/s)') #plotting the wind speed from South tower
ax[2, 0].plot(np.arange(240, 841), wse.rolling(window = n).mean(), color = 'black', label = 'South Tower Rolling Average') #plotting the rolling average from the South tower wind speed
ax[2, 0].plot(np.array(wrfout.variables['XTIME'][240:841]) * 60, wse_h_528, color = 'red', label = 'wrfout file') #plotting the wind speed from the wrfout file
ax[2, 0].set_xlabel('Time', fontsize = 10)
ax[2, 0].set_ylabel('Wind Speed (m/s)', fontsize = 10)
ax[2, 0].set_title('East Tower Wind Speed vs. wrfout', fontsize = 10)
# w wind
ax[2, 1].plot(np.arange(240, 841), we, color = 'blue', label = 'East Tower W Wind Speed (m/s)') #plotting the wind speed from South tower
ax[2, 1].plot(np.arange(240, 841), we.rolling(window = n).mean(), color = 'black', label = 'South Tower Rolling Average') #plotting the rolling average from the South tower wind speed
ax[2, 1].plot(np.array(wrfout.variables['XTIME'][240:841]) * 60, We_h_528, color = 'red', label = 'wrfout file') #plotting the wind speed from the wrfout file
ax[2, 1].set_xlabel('Time', fontsize = 10)
ax[2, 1].set_ylabel('Wind Speed (m/s)', fontsize = 10)
ax[2, 1].set_title('East Tower W Wind vs. wrfout', fontsize = 10)
#temperature
ax[2, 2].plot(np.arange(240, 841), te, color = 'blue', label = 'East Tower Temp (C)') #plotting the wind speed from South tower
ax[2, 2].plot(np.arange(240, 841), te.rolling(window = n).mean(), color = 'black', label = 'South Tower Rolling Average') #plotting the rolling average from the South tower wind speed
ax[2, 2].plot(np.array(wrfout.variables['XTIME'][240:841]) * 60, Te_h_528, color = 'red', label = 'wrfout file') #plotting the wind speed from the wrfout file
ax[2, 2].set_xlabel('Time', fontsize = 10)
ax[2, 2].set_ylabel('Temperature (C)', fontsize = 10)
ax[2, 2].set_title('East Tower Temperature vs. wrfout', fontsize = 10)


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
plt.savefig('/home/jbenik/FireFlux2/Codes_and_Data/Data/wrf_files/images/wrfout_short_towers2.png')
plt.show()
plt.pause(0.0001)
plt.close()

