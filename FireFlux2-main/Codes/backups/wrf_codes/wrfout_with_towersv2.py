# -*- coding: utf-8 -*-
"""
Created on Sat March 5 11:36:54 2022

@author: Jeremy Benik
"""

# %% Importing libraries
import pandas as pd
import netCDF4 as nc
import xarray as xr
import matplotlib.pyplot as plt
import numpy as np
from wrf import getvar, interplevel
import statistics as st
import glob
# %% Reading in data
# Main Tower Data
main_tower1 = pd.read_csv('/home/jbenik/FirefluxII/Codes_and_Data/Data/Main_Tower_Data/Proc_FF2_10HzMTdespiked_rotated.csv', parse_dates=['TIMESTAMP'], skiprows = (0, 2, 3))

main_tower = main_tower1.truncate(before= np.where(main_tower1['TIMESTAMP'] == '1/30/2013  15:00:00')[0][0], 
                    after=np.where(main_tower1['TIMESTAMP'] == '1/30/2013  15:06:00')[0][80])
# Wrfout file 
#This file is from a run that didn't complete, I tried to get the one off ember but it wasn't working when I wrote this code. 
wrfout = nc.Dataset('/home/jbenik/FirefluxII/Codes_and_Data/Data/wrf_files/backup_files/wrfout_d01_2013-01-30_15:00:00', 'r')
wrfout_xr = xr.open_dataset('/home/jbenik/FirefluxII/Codes_and_Data/Data/wrf_files/backup_files/wrfout_d01_2013-01-30_15:00:00')

# %% Getting the variables from the files
# Main tower variables
time_main_tower = main_tower['TIMESTAMP']
time2 = np.arange(0, len(time_main_tower)) / 10
ux20 = main_tower['Ux_20m']
uy20 = main_tower['Uy_20m']
ws_20 = np.sqrt((ux20 ** 2) + (uy20 ** 2))
uz20 = main_tower['Uz_20m']
ts20 = main_tower['Ts_20m']
ux10 = main_tower['Ux_10m']
uy10 = main_tower['Uy_10m']
ws_10 = np.sqrt((ux10 ** 2) + (uy10 ** 2))
uz10 = main_tower['Uz_10m']
ts10 = main_tower['Ts_10m']
ux6 = main_tower['Ux_6m']
uy6 = main_tower['Uy_6m']
ws_6 = np.sqrt((ux6 ** 2) + (uy6 ** 2))
uz6 = main_tower['Uz_6m']
ts6 = main_tower['Ts_6m']
# %%
# Wrfout variables
south_north = 190
west_east = 93
levels = [20, 10, 5.77]
xlat = wrfout.variables['XLAT'][:, :, :]
xlong = wrfout.variables['XLONG'][:, :, :]
time = wrfout.variables['XTIME'][:]
print("I am getting the u variable from the wrfout file")
u_wrfout = getvar(wrfout, "ua", None, units = "m/s")
print("U wind is done, now I am getting the V wind")
v_wrfout = getvar(wrfout, "va", None, units = "m/s")
print("V wind is done, now I am getting the W wind")
w_wrfout = getvar(wrfout, "wa", None, units = "m/s")
print("W wind is done, now I am getting Temperature")
T_wrfout = getvar(wrfout, "temp", None, units = 'K')
T_wrfout -= 273.15 #converting it to celcius
print("Now I am getting height")
#ws = np.sqrt((u_wrfout ** 2) + (v_wrfout ** 2))
ht = getvar(wrfout, "z", units="m", msl = False)
# %% Interpolating the variables to specific heights
# 20 meters
print("Interpolating heights")
U_h_20 = interplevel(u_wrfout, ht, 20)[:, 190, 93]
V_h_20 = interplevel(v_wrfout, ht, 20)[:, 190, 93]
ws_h_20 = np.sqrt((U_h_20 ** 2) + (V_h_20 ** 2))
W_h_20 = interplevel(w_wrfout, ht, 20)[:, 190, 93]
T_h_20 = interplevel(T_wrfout, ht, 20)[:, 190, 93]
# 10 meters
U_h_10 = interplevel(u_wrfout, ht, 10)[:, 190, 93]
V_h_10 = interplevel(v_wrfout, ht, 10)[:, 190, 93]
ws_h_10 = np.sqrt((U_h_10 ** 2) + (V_h_10 ** 2))
W_h_10 = interplevel(w_wrfout, ht, 10)[:, 190, 93]
T_h_10 = interplevel(T_wrfout, ht, 10)[:, 190, 93]
# 5.77 meters
U_h_577 = interplevel(u_wrfout, ht, 5.77)[:, 190, 93]
V_h_577 = interplevel(v_wrfout, ht, 5.77)[:, 190, 93]
ws_h_577 = np.sqrt((U_h_577 ** 2) + (V_h_577 ** 2))
W_h_577 = interplevel(w_wrfout, ht, 5.77)[:, 190, 93]
T_h_577 = interplevel(T_wrfout, ht, 5.77)[:, 190, 93]
# %% Making the plots
#defining n which is the number of intervals for the rolling average
n = 10
#I chose 10 here since the data is taken at 10Hz, so this way I can see what it is like every second

print("Plotting")
fig, ax  = plt.subplots(3, 3, figsize = (15, 15))
plt.suptitle("Wind Speeds and Temperature at the Main tower comapred to the wrfout file")
ax[0, 0].plot(np.array(wrfout.variables['XTIME'][:]), ws_h_20, label = 'wrfout file', color = 'red')
#ax[0, 0].plot(np.array(wrfout.variables['XTIME'][:]), ws_h_20.rolling(window = n).mean(), label = 'Average Winds', color = 'black')
ax[0, 0].plot(time2, ws_20, color = 'blue', label = 'Main Tower Data (20 meters)')
ax[0, 0].plot(time2, ws_20.rolling(window = n).mean(), color = 'black', label = 'Average Winds')
ax[0, 0].set_xlabel('Time (seconds)', fontsize = 8, fontweight = 'bold')
ax[0, 0].set_ylabel('Wind Speed (m/s)', fontsize = 8, fontweight = 'bold')
ax[0, 0].set_xlim(220, 350)
ax[0, 0].set_title("Wind Speed at 20 Meters", fontsize = 12, fontweight = 'bold')
ax[0, 0].legend()

ax[0, 1].plot(time2, ws_10, color = 'blue', label = 'Main Tower Data (10 meters)')
ax[0, 1].plot(time2, ws_10.rolling(window = n).mean(), color = 'black', label = 'Average Winds')
ax[0, 1].plot(np.array(wrfout.variables['XTIME'][:]), ws_h_10, label = 'wrfout file', color = 'red')
#ax[0, 1].plot(np.array(wrfout.variables['XTIME'][:]), ws_h_10.rolling(window = n).mean(), label = 'wrfout file', color = 'black')
ax[0, 1].set_title("Wind Speed at 10 Meters", fontsize = 12, fontweight = 'bold')
ax[0, 1].set_xlabel('Time (seconds)', fontsize = 8, fontweight = 'bold')
ax[0, 1].set_ylabel('Wind Speed (m/s)', fontsize = 8, fontweight = 'bold')
ax[0, 1].set_xlim(220, 350)
ax[0, 1].set_title("Wind Speed at 10 Meters", fontsize = 12, fontweight = 'bold')
ax[0, 1].legend()


ax[0, 2].plot(time2, ws_6, color = 'blue', label = 'Main Tower Data (5.77 meters)')
ax[0, 2].plot(time2, ws_6.rolling(window = n).mean(), color = 'black', label = 'Main Tower Data (5.77 meters)')
ax[0, 2].plot(np.array(wrfout.variables['XTIME'][:]), ws_h_577, label = 'wrfout file', color = 'red')
#ax[0, 2].plot(np.array(wrfout.variables['XTIME'][:]), ws_h_577.rolling(window = n).mean(), label = 'wrfout file', color = 'black')
ax[0, 2].set_xlabel('Time (seconds)', fontsize = 8, fontweight = 'bold')
ax[0, 2].set_ylabel('Wind Speed (m/s)', fontsize = 8, fontweight = 'bold')
ax[0, 2].set_xlim(220, 350)
ax[0, 2].set_title("Wind Speed at 5.77 Meters", fontsize = 12, fontweight = 'bold')
ax[0, 2].legend()


ax[1, 0].plot(time2, ts20, color = 'blue', label = 'Main tower Data (Temperature at 20 meters)')
ax[1, 0].plot(time2, ts20.rolling(window = n).mean(), color = 'black', label = 'Main tower Data (Temperature at 20 meters)')
ax[1, 0].plot(np.array(wrfout.variables['XTIME'][:]), T_h_20, color = 'red', label = 'wrfout file')
#ax[1, 0].plot(np.array(wrfout.variables['XTIME'][:]), T_h_20.rolling(window = n).mean(), color = 'black', label = 'wrfout file')
ax[1, 0].set_xlabel('Time (seconds)', fontsize = 8, fontweight = 'bold')
ax[1, 0].set_ylabel('Temperature (C)', fontsize = 8, fontweight = 'bold')
ax[1, 0].set_title("Temperature at 20 Meters", fontsize = 12, fontweight = 'bold')
ax[1, 0].set_xlim(220, 350)
ax[1, 0].legend()

ax[1, 1].plot(time2, ts10, color = 'blue', label = 'Main tower Data (Temperature at 10 meters)')
ax[1, 1].plot(time2, ts10.rolling(window = n).mean(), color = 'black', label = 'Main tower Data (Temperature at 10 meters)')
ax[1, 1].plot(np.array(wrfout.variables['XTIME'][:]), T_h_10, color = 'red', label = 'wrfout file')
#ax[1, 1].plot(np.array(wrfout.variables['XTIME'][:]), T_h_10.rolling(window = n).mean(), color = 'black', label = 'wrfout file')
ax[1, 1].set_xlabel('Time (seconds)', fontsize = 8, fontweight = 'bold')
ax[1, 1].set_ylabel('Temperature (C)', fontsize = 8, fontweight = 'bold')
ax[1, 1].set_title("Temperature at 10 Meters", fontsize = 12, fontweight = 'bold')
ax[1, 1].set_xlim(220, 350)
ax[1, 1].legend()

ax[1, 2].plot(time2, ts6, color = 'blue', label = 'Main tower Data (Temperature at 5.77 meters)')
ax[1, 2].plot(time2, ts6.rolling(window = n).mean(), color = 'black', label = 'Main tower Data (Temperature at 5.77 meters)')
ax[1, 2].plot(np.array(wrfout.variables['XTIME'][:]), T_h_577, color = 'red', label = 'wrfout file')
#ax[1, 2].plot(np.array(wrfout.variables['XTIME'][:]), T_h_577.rolling(window = n).mean(), color = 'black', label = 'wrfout file')
ax[1, 2].set_xlabel('Time (seconds)', fontsize = 8, fontweight = 'bold')
ax[1, 2].set_ylabel('Temperature (C)', fontsize = 8, fontweight = 'bold')
ax[1, 2].set_title("Temperature at 5.77 Meters", fontsize = 12, fontweight = 'bold')
ax[1, 2].set_xlim(220, 350)
ax[1, 2].legend()


ax[2, 0].plot(time2, ws_20, color = 'blue', label = 'Main tower Data (W wind 20 meters)')
ax[2, 0].plot(time2, ws_20.rolling(window = n).mean(), color = 'black', label = 'Main tower Data (W wind 20 meters)')
ax[2, 0].plot(np.array(wrfout.variables['XTIME'][:]), W_h_20, color = 'red', label = 'wrfout file')
#ax[2, 0].plot(np.array(wrfout.variables['XTIME'][:]), W_h_20.rolling(window = n).mean(), color = 'black', label = 'wrfout file')
ax[2, 0].set_xlabel('Time (seconds)', fontsize = 8, fontweight = 'bold')
ax[2, 0].set_ylabel('Wind Speed (m/s)', fontsize = 8, fontweight = 'bold')
ax[2, 0].set_title("W Wind Speed at 20 Meters", fontsize = 12, fontweight = 'bold')
ax[2, 0].set_xlim(220, 350)
ax[2, 0].legend()

ax[2, 1].plot(time2, ws_10, color = 'blue', label = 'Main tower Data (W wind 10 meters)')
ax[2, 1].plot(time2, ws_10.rolling(window = n).mean(), color = 'black', label = 'Main tower Data (W wind 10 meters)')
ax[2, 1].plot(np.array(wrfout.variables['XTIME'][:]), W_h_10, color = 'red', label = 'wrfout file')
#ax[2, 1].plot(np.array(wrfout.variables['XTIME'][:]), W_h_10.rolling(window = n).mean(), color = 'black', label = 'wrfout file')
ax[2, 1].set_xlabel('Time (seconds)', fontsize = 8, fontweight = 'bold')
ax[2, 1].set_ylabel('Wind Speed (m/s)', fontsize = 8, fontweight = 'bold')
ax[2, 1].set_title("W Wind Speed at 10 Meters", fontsize = 12, fontweight = 'bold')
ax[2, 1].set_xlim(220, 350)
ax[2, 1].legend()
ax[2, 1].grid()



ax[2, 2].plot(time2, ws_6, color = 'blue', label = 'Main tower Data (W wind 5.77 meters)')
ax[2, 2].plot(time2, ws_6.rolling(window = n).mean(), color = 'black', label = 'Main tower Data (W wind 5.77 meters)')
ax[2, 2].plot(np.array(wrfout.variables['XTIME'][:]), W_h_577, color = 'red', label = 'wrfout file')
#ax[2, 2].plot(np.array(wrfout.variables['XTIME'][:]), W_h_577.rolling(window = n).mean(), color = 'black', label = 'wrfout file')
ax[2, 2].set_xlabel('Time (seconds)', fontsize = 8, fontweight = 'bold')
ax[2, 2].set_ylabel('Wind Speed (m/s)', fontsize = 8, fontweight = 'bold')
ax[2, 2].set_title("W Wind Speed at 5.77 Meters", fontsize = 12, fontweight = 'bold')
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
#plt.savefig('/home/jbenik/FireFlux2/Codes_and_Data/Data/wrf_files/images/wrfout_with_towers2.png')
plt.show()
print("That was the main tower plot, now I will work on the short towers")
# %% Short towers
n = 5 #this is a 5 second average of the data
df_w = pd.read_csv('/home/jbenik/FirefluxII/Codes_and_Data/Data/Short_Tower_Data/Proc_FF2_1HzSTWdespikedrotated.csv')
df_e = pd.read_csv('/home/jbenik/FirefluxII/Codes_and_Data/Data/Short_Tower_Data/Proc_FF2_1HzSTEdespikedrotated.csv')
df_s = pd.read_csv('/home/jbenik/FirefluxII/Codes_and_Data/Data/Short_Tower_Data/Proc_FF2_1HzSTSdespikedrotated.csv')
print("Short tower data read in")
# %%
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
# %%
# Interpolating the vars to heights and defining the location of them
#west tower is at 5.33m
#east tower is at 5.28 meters
#south tower is at 5.33m

#west tower
print("Interpolating vars for west tower")
Uw_h_533 = interplevel(u_wrfout, ht, 5.33)[:, 94, 151]
Vw_h_533 = interplevel(v_wrfout, ht, 5.33)[:, 94, 151]
wsw_h_533 = np.sqrt((Uw_h_533 ** 2) + (Vw_h_533 ** 2))
Ww_h_533 = interplevel(w_wrfout, ht, 5.33)[:, 94, 151]
Tw_h_533 = interplevel(T_wrfout, ht, 5.33)[:, 94, 151]

#east tower
print("Interpolating vars for east tower")
Ue_h_528 = interplevel(u_wrfout, ht, 5.28)[:, 116, 158]
Ve_h_528 = interplevel(v_wrfout, ht, 5.28)[:, 116, 158]
wse_h_528 = np.sqrt((Ue_h_528 ** 2) + (Ve_h_528 ** 2))
We_h_528 = interplevel(w_wrfout, ht, 5.28)[:, 116, 158]
Te_h_528 = interplevel(T_wrfout, ht, 5.28)[:, 116, 158]


#south tower
print("Interpolating vars for south tower")
Us_h_533 = interplevel(u_wrfout, ht, 5.33)[:, 115, 119]
Vs_h_533 = interplevel(v_wrfout, ht, 5.33)[:, 115, 119]
wss_h_533 = np.sqrt((Us_h_533 ** 2) + (Vs_h_533 ** 2))
Ws_h_533 = interplevel(w_wrfout, ht, 5.33)[:, 115, 119]
Ts_h_533 = interplevel(T_wrfout, ht, 5.33)[:, 115, 119]

# %% Creating a plot for the short towers
print("Creating the plot")
fig, ax = plt.subplots(3, 3, figsize = (12, 12))
# Plotting the west tower first
#wind speed
ax[0, 0].plot(range(len(time_short_tower_w)), wsw, color = 'blue', label = 'West Tower Wind Speed (m/s)') #plotting the wind speed from west tower
ax[0, 0].plot(range(len(time_short_tower_w)), wsw.rolling(window = n).mean(), color = 'black', label = 'West Tower Rolling Average') #plotting the rolling average from the west tower wind speed
ax[0, 0].plot(np.array(wrfout.variables['XTIME'][:]), wsw_h_533, color = 'red', label = 'wrfout file') #plotting the wind speed from the wrfout file
ax[0, 0].set_xlabel('Time', fontsize = 8, fontweight = 'bold')
ax[0, 0].set_ylabel('Wind Speed (m/s)', fontsize = 8, fontweight = 'bold')
ax[0, 0].set_title('West Tower Wind Speed vs. wrfout', fontsize = 12, fontweight = 'bold')
# w wind
ax[0, 1].plot(range(len(time_short_tower_w)), ww, color = 'blue', label = 'West Tower W Wind Speed (m/s)') #plotting the wind speed from west tower
ax[0, 1].plot(range(len(time_short_tower_w)), ww.rolling(window = n).mean(), color = 'black', label = 'West Tower Rolling Average') #plotting the rolling average from the west tower wind speed
ax[0, 1].plot(np.array(wrfout.variables['XTIME'][:]), Ww_h_533, color = 'red', label = 'wrfout file') #plotting the wind speed from the wrfout file
ax[0, 1].set_xlabel('Time', fontsize = 8, fontweight = 'bold')
ax[0, 1].set_ylabel('Wind Speed (m/s)', fontsize = 8, fontweight = 'bold')
ax[0, 1].set_title('West Tower W Wind vs. wrfout', fontsize = 12, fontweight = 'bold')
#temperature
ax[0, 2].plot(range(len(time_short_tower_w)), tw, color = 'blue', label = 'West Tower Temp (C)') #plotting the wind speed from west tower
ax[0, 2].plot(range(len(time_short_tower_w)), tw.rolling(window = n).mean(), color = 'black', label = 'West Tower Rolling Average') #plotting the rolling average from the west tower wind speed
ax[0, 2].plot(np.array(wrfout.variables['XTIME'][:]), Tw_h_533, color = 'red', label = 'wrfout file') #plotting the wind speed from the wrfout file
ax[0, 2].set_xlabel('Time', fontsize = 8, fontweight = 'bold')
ax[0, 2].set_ylabel('Wind Speed (m/s)', fontsize = 8, fontweight = 'bold')
ax[0, 2].set_title('West Tower Temperature vs. wrfout', fontsize = 12, fontweight = 'bold')

# Plotting the South Tower
#wind speed
ax[1, 0].plot(range(len(time_short_tower_s)), wss, color = 'blue', label = 'South Tower Wind Speed (m/s)') #plotting the wind speed from South tower
ax[1, 0].plot(range(len(time_short_tower_s)), wss.rolling(window = n).mean(), color = 'black', label = 'South Tower Rolling Average') #plotting the rolling average from the South tower wind speed
ax[1, 0].plot(np.array(wrfout.variables['XTIME'][:]), wss_h_533, color = 'red', label = 'wrfout file') #plotting the wind speed from the wrfout file
ax[1, 0].set_xlabel('Time', fontsize = 8, fontweight = 'bold')
ax[1, 0].set_ylabel('Wind Speed (m/s)', fontsize = 8, fontweight = 'bold')
ax[1, 0].set_title('South Tower Wind Speed vs. wrfout', fontsize = 12, fontweight = 'bold')
# w wind
ax[1, 1].plot(range(len(time_short_tower_s)), ws, color = 'blue', label = 'South Tower W Wind Speed (m/s)') #plotting the wind speed from South tower
ax[1, 1].plot(range(len(time_short_tower_s)), ws.rolling(window = n).mean(), color = 'black', label = 'South Tower Rolling Average') #plotting the rolling average from the South tower wind speed
ax[1, 1].plot(np.array(wrfout.variables['XTIME'][:]), Ws_h_533, color = 'red', label = 'wrfout file') #plotting the wind speed from the wrfout file
ax[1, 1].set_xlabel('Time', fontsize = 8, fontweight = 'bold')
ax[1, 1].set_ylabel('Wind Speed (m/s)', fontsize = 8, fontweight = 'bold')
ax[1, 1].set_title('South Tower W Wind vs. wrfout', fontsize = 12, fontweight = 'bold')
#temperature
ax[1, 2].plot(range(len(time_short_tower_s)), ts, color = 'blue', label = 'South Tower Temp (C)') #plotting the wind speed from South tower
ax[1, 2].plot(range(len(time_short_tower_s)), ts.rolling(window = n).mean(), color = 'black', label = 'South Tower Rolling Average') #plotting the rolling average from the South tower wind speed
ax[1, 2].plot(np.array(wrfout.variables['XTIME'][:]), Ts_h_533, color = 'red', label = 'wrfout file') #plotting the wind speed from the wrfout file
ax[1, 2].set_xlabel('Time', fontsize = 8, fontweight = 'bold')
ax[1, 2].set_ylabel('Wind Speed (m/s)', fontsize = 8, fontweight = 'bold')
ax[1, 2].set_title('South Tower Temperature vs. wrfout', fontsize = 12, fontweight = 'bold')

# Plotting the East Tower
#wind speed
ax[2, 0].plot(range(len(time_short_tower_e)), wse, color = 'blue', label = 'South Tower Wind Speed (m/s)') #plotting the wind speed from South tower
ax[2, 0].plot(range(len(time_short_tower_e)), wse.rolling(window = n).mean(), color = 'black', label = 'South Tower Rolling Average') #plotting the rolling average from the South tower wind speed
ax[2, 0].plot(np.array(wrfout.variables['XTIME'][:]), wse_h_528, color = 'red', label = 'wrfout file') #plotting the wind speed from the wrfout file
ax[2, 0].set_xlabel('Time', fontsize = 8, fontweight = 'bold')
ax[2, 0].set_ylabel('Wind Speed (m/s)', fontsize = 8, fontweight = 'bold')
ax[2, 0].set_title('South Tower Wind Speed vs. wrfout', fontsize = 12, fontweight = 'bold')
# w wind
ax[2, 1].plot(range(len(time_short_tower_e)), we, color = 'blue', label = 'South Tower W Wind Speed (m/s)') #plotting the wind speed from South tower
ax[2, 1].plot(range(len(time_short_tower_e)), we.rolling(window = n).mean(), color = 'black', label = 'South Tower Rolling Average') #plotting the rolling average from the South tower wind speed
ax[2, 1].plot(np.array(wrfout.variables['XTIME'][:]), We_h_528, color = 'red', label = 'wrfout file') #plotting the wind speed from the wrfout file
ax[2, 1].set_xlabel('Time', fontsize = 8, fontweight = 'bold')
ax[2, 1].set_ylabel('Wind Speed (m/s)', fontsize = 8, fontweight = 'bold')
ax[2, 1].set_title('South Tower W Wind vs. wrfout', fontsize = 12, fontweight = 'bold')
#temperature
ax[2, 2].plot(range(len(time_short_tower_e)), te, color = 'blue', label = 'South Tower Temp (C)') #plotting the wind speed from South tower
ax[2, 2].plot(range(len(time_short_tower_e)), te.rolling(window = n).mean(), color = 'black', label = 'South Tower Rolling Average') #plotting the rolling average from the South tower wind speed
ax[2, 2].plot(np.array(wrfout.variables['XTIME'][:]), Te_h_528, color = 'red', label = 'wrfout file') #plotting the wind speed from the wrfout file
ax[2, 2].set_xlabel('Time', fontsize = 8, fontweight = 'bold')
ax[2, 2].set_ylabel('Wind Speed (m/s)', fontsize = 8, fontweight = 'bold')
ax[2, 2].set_title('South Tower Temperature vs. wrfout', fontsize = 12, fontweight = 'bold')


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
plt.show()

