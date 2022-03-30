''' This code is designed to test plotting the tower data and see if it's offset with the other variables'''
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
print("Main tower data")
main_tower1 = pd.read_csv('/home/jbenik/FireFlux2/Codes_and_Data/Data/Main_Tower_Data/Proc_FF2_10HzMTdespiked_rotated.csv', parse_dates=['TIMESTAMP'], skiprows = (0, 2, 3))

main_tower = main_tower1.truncate(before= np.where(main_tower1['TIMESTAMP'] == '1/30/2013  15:04:00')[0][0], 
                    after=np.where(main_tower1['TIMESTAMP'] == '1/30/2013  15:06:00')[0][0])
# Wrfout file 
#This file is from a run that didn't complete, I tried to get the one off ember but it wasn't working when I wrote this code. 
print("wrfout file")
wrfout = nc.Dataset('/home/jbenik/FireFlux2/Codes_and_Data/Data/wrf_files/wrfout_d01_2013-01-30_15:00:00', 'r')
wrfout_xr = xr.open_dataset('/home/jbenik/FireFlux2/Codes_and_Data/Data/wrf_files/wrfout_d01_2013-01-30_15:00:00')

wrfin = nc.Dataset('/home/jbenik/FireFlux2/Codes_and_Data/Data/wrf_files/wrfin_d01_real', 'r')


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

print('6 meter variable')
ux6 = main_tower['Ux_6m']
uy6 = main_tower['Uy_6m']
ws_6 = np.sqrt((ux6 ** 2) + (uy6 ** 2))
uz6 = main_tower['Uz_6m']
ts6 = main_tower['Ts_6m']
# %%
# Wrfout variables
print("Getting variables from the wrfout file")
#locations
# %% U variable

south_north_u = wrf.ll_to_xy(wrfin, 29.387975, -95.04142222222222, timeidx = 0, squeeze = False, meta = False, stagger = 'u')[1]
west_east_stag_u = wrf.ll_to_xy(wrfin, 29.387975, -95.04142222222222, timeidx = 0, squeeze = False, meta = False, stagger = 'u')[0]

# %% V Variable
south_north_stag_v = wrf.ll_to_xy(wrfin, 29.387975, -95.04142222222222, timeidx = 0, squeeze = False, meta = False, stagger = 'v')[1]
west_east_v = wrf.ll_to_xy(wrfin, 29.387975, -95.04142222222222, timeidx = 0, squeeze = False, meta = False, stagger = 'v')[0]

# %% Other variables
south_north_wrfout = wrf.ll_to_xy(wrfin, 29.387975, -95.04142222222222, timeidx = 0, squeeze = False, meta = False, stagger = 'm')[1]
west_east_wrfout = wrf.ll_to_xy(wrfin, 29.387975, -95.04142222222222, timeidx = 0, squeeze = False, meta = False, stagger = 'm')[0]

# %% getting the variables
levels = [20, 10, 5.77]
print("Getting xlat")
#xlat = wrfout.variables['XLAT'][:, :, :]
print("Getting xlong")
#xlong = wrfout.variables['XLONG'][:, :, :]
print("Getting time")
time = wrfout.variables['XTIME'][:]
print("I am getting the u variable from the wrfout file")
#u_wrfout = wrf.getvar(wrfout, "ua", None, units = "m/s")
print("U wind is done, now I am getting the V wind")
#v_wrfout = wrf.getvar(wrfout, "va", None, units = "m/s")
print("V wind is done, now I am getting the W wind")
w_wrfout = wrf.getvar(wrfout, "wa", None, units = "m/s")
print("W wind is done, now I am getting Temperature")
#T_wrfout = wrf.getvar(wrfout, "temp", None, units = 'K')
#T_wrfout -= 273.15 #converting it to celcius
print("Now I am getting height")
#ws = np.sqrt((u_wrfout ** 2) + (v_wrfout ** 2))
#ht = wrf.getvar(wrfout, "z", units="m", msl = False)

ht = wrf.getvar(wrfout, "z", units="m", msl = False)

# %% Interpolating the variables to specific heights
# 20 meters
print("Interpolating heights")
print("Interpolating U at 20 meters")
#U_h_20 = wrf.interplevel(u_wrfout, ht, 20)[241:361, south_north_u, west_east_stag_u]
print("Interpolating V at 20 meters")
#V_h_20 = wrf.interplevel(v_wrfout, ht, 20)[241:361, south_north_stag_v, west_east_v]
print("Calculating Wind Speed")
#ws_h_20 = np.sqrt((U_h_20 ** 2) + (V_h_20 ** 2))
print("Interpolating W at 20 meters")
W_h_20 = wrf.interplevel(w_wrfout, ht, 20)[241:361, south_north_wrfout, west_east_wrfout]
print("Interpolating T at 20 meters")
#T_h_20 = wrf.interplevel(T_wrfout, ht, 20)[241:361, south_north_wrfout, west_east_wrfout]
# 10 meters
print("Interpolating U at 10 meters")
#U_h_10 = wrf.interplevel(u_wrfout, ht, 10)[241:361, south_north_u, west_east_stag_u]
#V_h_10 = wrf.interplevel(v_wrfout, ht, 10)[241:361, south_north_stag_v, west_east_v]
#ws_h_10 = np.sqrt((U_h_10 ** 2) + (V_h_10 ** 2))
W_h_10 = wrf.interplevel(w_wrfout, ht, 10)[241:361, south_north_wrfout, west_east_wrfout]
#T_h_10 = wrf.interplevel(T_wrfout, ht, 10)[241:361, south_north_wrfout, west_east_wrfout]
# 5.77 meters
#U_h_577 = wrf.interplevel(u_wrfout, ht, 5.77)[241:361, south_north_u, west_east_stag_u]
#V_h_577 = wrf.interplevel(v_wrfout, ht, 5.77)[241:361, south_north_stag_v, west_east_v]
#ws_h_577 = np.sqrt((U_h_577 ** 2) + (V_h_577 ** 2))
W_h_577 = wrf.interplevel(w_wrfout, ht, 5.77)[241:361, south_north_wrfout, west_east_wrfout]
#T_h_577 = wrf.interplevel(T_wrfout, ht, 5.77)[241:361, south_north_wrfout, west_east_wrfout]

fig, ax = plt.subplots(1, 3)
ax[0].plot(np.arange(240, 360), W_h_20)
ax[0].plot(time2, uz20)
ax[0].set_ylabel('20 meters')
ax[1].plot(time2, uz10)
ax[1].plot(np.arange(240, 360), W_h_10)
ax[1].set_ylabel('10 meters')
ax[2].plot(time2, uz6)
ax[2].plot(np.arange(240, 360), W_h_577)
plt.show()
# %%
#