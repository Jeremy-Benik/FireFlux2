'''The purpose of this code is to find when the fire reaches the points on the grid'''
# -*- coding: utf-8 -*-
"""
Created on Sat March 15 11:36:54 2022

@author: Jeremy Benik
"""
# %% Getting the towers location on the new grid
#use an interpolation routine to try and find the towers for me. Whenever we switch to the 2 domain setup, then it will be more difficult, and then we will need to interpolate. It's fine with what I have now
# At some point I will need to switch to the external interpolation routines. There should be somehting in: https://wrf-python.readthedocs.io/en/latest/index.html
#check is the w0 does anything so test that in the balbi code. 
#https://wrf-python.readthedocs.io/en/latest/user_api/generated/wrf.xy_to_ll.html?highlight=wrf.ll_to_xy
# wrf.xy_to_ll(wrfin, x, y, timeidx=0, squeeze=True, meta=True, stagger=None)
#might need to modify the matlab code if needed. 
#Fire start (first ignition) on the grid
#fire_ignition_start_x1 = 405
#fire_ignition_start_y1 = 997
'''The time at which the fire area arrives at the MAIN TOWER is: 341
*****************************
The time at which the fire area arrives at the EAST TOWER is: 401
*****************************
The time at which the fire area arrives at the WEST TOWER is: 497
*****************************
The time at which the fire area arrives at the SOUTH TOWER is: 551'''
# %% Importing libraries
print("importing necessary libraries")
import netCDF4 as nc
import numpy as np
import xarray as xr
import pandas as pd
import wrf
# %% Reading in the files
print("Reading in the wrfout file")
wrfout = nc.Dataset('/home/jbenik/FireFlux2/Codes_and_Data/Data/wrf_files/wrfout_files/wrfout_d01_2013-01-30_15:00:00', 'r')
print('Reading in the wrfin file')
wrfin = nc.Dataset('/home/jbenik/FireFlux2/Codes_and_Data/Data/wrf_files/wrfin_d01_real', 'r')
print('reading in the short towers')
df_w1 = pd.read_csv('/home/jbenik/FireFlux2/Codes_and_Data/Data/Short_Tower_Data/Proc_FF2_1HzSTWdespikedrotated.csv')

df_e1 = pd.read_csv('/home/jbenik/FireFlux2/Codes_and_Data/Data/Short_Tower_Data/Proc_FF2_1HzSTEdespikedrotated.csv')

df_s1 = pd.read_csv('/home/jbenik/FireFlux2/Codes_and_Data/Data/Short_Tower_Data/Proc_FF2_1HzSTSdespikedrotated.csv')


# %% finding where the towers are

#main tower
south_north_u = wrf.ll_to_xy(wrfin, 29.387975, -95.04142222222222, timeidx = 0, squeeze = False, meta = False, stagger = 'u')[1]
west_east_stag_u = wrf.ll_to_xy(wrfin, 29.387975, -95.04142222222222, timeidx = 0, squeeze = False, meta = False, stagger = 'u')[0]

south_north_stag_v = wrf.ll_to_xy(wrfin, 29.387975, -95.04142222222222, timeidx = 0, squeeze = False, meta = False, stagger = 'v')[1]
west_east_v = wrf.ll_to_xy(wrfin, 29.387975, -95.04142222222222, timeidx = 0, squeeze = False, meta = False, stagger = 'v')[0]

south_north_wrfout = wrf.ll_to_xy(wrfin, 29.387975, -95.04142222222222, timeidx = 0, squeeze = False, meta = False, stagger = 'm')[1]
west_east_wrfout = wrf.ll_to_xy(wrfin, 29.387975, -95.04142222222222, timeidx = 0, squeeze = False, meta = False, stagger = 'm')[0]


#west tower
south_north_u_w = wrf.ll_to_xy(wrfin, 29.38617222222222, -95.04138611111111, timeidx = 0, squeeze = False, meta = False, stagger = 'u')[1]
west_east_stag_u_w = wrf.ll_to_xy(wrfin, 29.38617222222222, -95.04138611111111, timeidx = 0, squeeze = False, meta = False, stagger = 'u')[0]

south_north_stag_v_w = wrf.ll_to_xy(wrfin, 29.38617222222222, -95.04138611111111, timeidx = 0, squeeze = False, meta = False, stagger = 'v')[1]
west_east_v_w = wrf.ll_to_xy(wrfin, 29.38617222222222, -95.04138611111111, timeidx = 0, squeeze = False, meta = False, stagger = 'v')[0]

south_north_w = wrf.ll_to_xy(wrfin, 29.38617222222222, -95.04138611111111, timeidx = 0, squeeze = False, meta = False, stagger = 'm')[1]
west_east_w = wrf.ll_to_xy(wrfin, 29.38617222222222, -95.04138611111111, timeidx = 0, squeeze = False, meta = False, stagger = 'm')[0]

#east tower
south_north_u_e = wrf.ll_to_xy(wrfin, 29.38650833333333, -95.0402111111111, timeidx = 0, squeeze = False, meta = False, stagger = 'u')[1]
west_east_stag_u_e = wrf.ll_to_xy(wrfin, 29.38650833333333, -95.0402111111111, timeidx = 0, squeeze = False, meta = False, stagger = 'u')[0]

west_east_v_e = wrf.ll_to_xy(wrfin, 29.38650833333333, -95.0402111111111, timeidx = 0, squeeze = False, meta = False, stagger = 'v')[0]
south_north_stag_v_e = wrf.ll_to_xy(wrfin, 29.38650833333333, -95.0402111111111, timeidx = 0, squeeze = False, meta = False, stagger = 'v')[1]

south_north_e = wrf.ll_to_xy(wrfin, 29.38650833333333, -95.0402111111111, timeidx = 0, squeeze = False, meta = False, stagger = 'm')[1]
west_east_e = wrf.ll_to_xy(wrfin, 29.38650833333333, -95.0402111111111, timeidx = 0, squeeze = False, meta = False, stagger = 'm')[0]

#south tower
south_north_u_s = wrf.ll_to_xy(wrfin, 29.384775,-95.0403, timeidx = 0, squeeze = False, meta = False, stagger = 'u')[1]
west_east_stag_u_s = wrf.ll_to_xy(wrfin, 29.384775,-95.0403, timeidx = 0, squeeze = False, meta = False, stagger = 'u')[0]

south_north_stag_v_s = wrf.ll_to_xy(wrfin, 29.384775,-95.0403, timeidx = 0, squeeze = False, meta = False, stagger = 'v')[1]
west_east_v_s = wrf.ll_to_xy(wrfin, 29.384775,-95.0403, timeidx = 0, squeeze = False, meta = False, stagger = 'v')[0]

south_north_s = wrf.ll_to_xy(wrfin, 29.384775,-95.0403, timeidx = 0, squeeze = False, meta = False, stagger = 'm')[1]
west_east_s = wrf.ll_to_xy(wrfin, 29.384775,-95.0403, timeidx = 0, squeeze = False, meta = False, stagger = 'm')[0]
# %% Calling fire area
print('I am now reading in the fire_area')
fire_area = wrfout.variables['FIRE_AREA'][:, :, :] #time, south_north_subgrid, west_east_subgrid
print('I am reading in the time variable')
time = wrfout.variables['XTIME'][:]
time2 = np.arange(0, 1000)
# %% finding where it is greater than zero for specified tower to see when it reaches the area

#main tower
print('The index for when the time where the main tower saw the fire in the wrfout file is: ', np.where(fire_area[:, south_north_wrfout * 10, west_east_wrfout * 10] >= 1)[0][0])
print('The time of arrival at the main tower is:', time[np.where(fire_area[:, south_north_wrfout * 10, west_east_wrfout * 10] >= 1)[0][0]])

# west tower
print('The index for when the time where the west tower saw the fire in the wrfout file is: ', np.where(fire_area[:, south_north_w * 10, west_east_w * 10] >= 1)[0][0])
print('The time of arrival at the west tower is:', time[np.where(fire_area[:, south_north_w * 10, west_east_w * 10] >= 1)[0][0]])

# east tower
print('The index for when the time2 where the east tower saw the fire in the wrfout file is: ', np.where(fire_area[:, south_north_e * 10, west_east_e * 10] >= 1)[0][0])
print('The time of arrival at the east tower is:', time[np.where(fire_area[:, south_north_e * 10, west_east_e * 10] >= 1)[0][0]])

# south tower
print('The index for when the time where the south tower saw the fire in the wrfout file is: ', np.where(fire_area[:, south_north_s * 10, west_east_s * 10] >= 1)[0][0])
print('The time of arrival at the south tower in minutes is:', time[np.where(fire_area[:, south_north_s * 10, west_east_s * 10] >= 1)[0][0]])
print('***********************')
# %% Getting the indexes for these all
#main tower
print('south_north_u, west_east_stag main tower', south_north_u, west_east_stag_u)
print('south_north_stag_v, west_east_v main tower', south_north_stag_v, west_east_v)
print('using the other grid:', south_north_wrfout, west_east_wrfout)
#west tower
print('south_north_w_u, west_east_stag west tower', south_north_u_w, west_east_stag_u_w)
print('south_north_stag_v, west_east_v west tower', south_north_stag_v_w, west_east_v_w)
print('using the other grid:', south_north_w, west_east_w)

# east tower
print('south_north_u, west_east_stag east tower', south_north_u_e, west_east_stag_u_e)
print('south_north_stag_v, west_east_v east tower', south_north_stag_v_e, west_east_v_e)
print('using the other grid:', south_north_e, west_east_e)

# South tower
print('south_north_u, west_east_stag south tower', south_north_u_s, west_east_stag_u_s)
print('south_north_stag_v, west_east_v south tower', south_north_stag_v_s, west_east_v_s)
print('using the other grid:', south_north_s, west_east_s)
# %% Using a different method using the AVG_FUEL_FRAC
'''THIS IS WHAT DR. KOCHANSKI SENT TO ME:
The fire mesh has a separate mesh defined by FXLAT and FXLONG. 
The right way, is to do the same thing you did to find the indexes on the atmospheric mesh, but find indexes with respect to the FXLAT and FXLON instead of XLAT and XLONG.
 Converting indexes will be tricky because there is not exactly 10 time more points in the fire mesh than in the atmospheric mesh (compare the sizes of FXLAT and XTAL), 
 so your assumption is not ntirely correct.

Another crude first cut method woudl be to look at the AVG_FUEL_FRAC variable, 
which represents the fuel fraction on the atmospheric mesh. The time when AVG_FUEL_FRAC drops below 1 indicates that there is a fire in this cell. 
It is not going to be as precise as the using the FIRE_AREA or FUEL_FRAC from the fire mesh, but it should be easy to plug it into your current code to have a quick estimate.'''
# Trying it out
print('Reading in the fuel_frac')
fuel_frac = wrfout.variables['AVG_FUEL_FRAC'][:, :, :]
#print(fuel_frac[0, :, :])

#main tower
print('The index for when the time where the main tower saw the fire in the wrfout file is: ', np.where(fuel_frac[:, south_north_wrfout, west_east_wrfout] < 1)[0][1])
print('The time of arrival at the main tower is:', time[np.where(fuel_frac[:, south_north_wrfout, west_east_wrfout] < 1)[0][1]])
print('The time of arrival at the main tower in seconds is:', time[np.where(fuel_frac[:, south_north_wrfout, west_east_wrfout] < 1)[0][1]] * 60)

# west tower
print('The index for when the time where the west tower saw the fire in the wrfout file is: ', np.where(fuel_frac[:, south_north_w, west_east_w] < 1)[0][1])
print('The time of arrival at the west tower is:', time[np.where(fuel_frac[:, south_north_w, west_east_w] < 1)[0][1]])
print('The time of arrival at the west tower in seconds is:', time[np.where(fuel_frac[:, south_north_w, west_east_w] < 1)[0][1]] * 60)

# east tower
print('The index for when the time2 where the east tower saw the fire in the wrfout file is: ', np.where(fuel_frac[:, south_north_e, west_east_e] < 1)[0][1])
print('The time of arrival at the east tower is:', time[np.where(fuel_frac[:, south_north_e, west_east_e] < 1)[0][1]])
print('The time of arrival at the east tower in seconds is:', time[np.where(fuel_frac[:, south_north_e, west_east_e] < 1)[0][1]] * 60)

# south tower
print('The index for when the time where the south tower saw the fire in the wrfout file is: ', np.where(fuel_frac[:, south_north_s, west_east_s] < 1)[0][1])
print('The time of arrival at the south tower in minutes is:', time[np.where(fuel_frac[:, south_north_s, west_east_s] < 1)[0][1]])
print('The time of arrival at the south tower in seconds is:', time[np.where(fuel_frac[:, south_north_s, west_east_s] < 1)[0][1]] * 60)

'''
#main tower
print('The index for when the time where the main tower saw the fire in the wrfout file is: ', np.where(fuel_frac[:, south_north_wrfout, west_east_wrfout] < 1)[0][1])
print('The time of arrival at the main tower is:', time[np.where(fuel_frac[:, south_north_wrfout, west_east_wrfout] < 1)[0][1]])
print('The time of arrival at the main tower is:', time[np.where(fuel_frac[:, south_north_wrfout, west_east_wrfout] < 1)[0][1]] * 60)

# west tower
print('The index for when the time where the west tower saw the fire in the wrfout file is: ', np.where(fuel_frac[:, south_north_w, west_east_w] < 1)[0][1])
print('The time of arrival at the west tower is:', time[np.where(fuel_frac[:, south_north_w, west_east_w] < 1)[0][1]])
print('The time of arrival at the west tower is:', time[np.where(fuel_frac[:, south_north_w, west_east_w] < 1)[0][1]] * 60)

# east tower
print('The index for when the time2 where the east tower saw the fire in the wrfout file is: ', np.where(fuel_frac[:, south_north_e, west_east_e] < 1)[0][1])
print('The time of arrival at the east tower is:', time[np.where(fuel_frac[:, south_north_e, west_east_e] < 1)[0][1]])
print('The time of arrival at the east tower is:', time[np.where(fuel_frac[:, south_north_e, west_east_e] < 1)[0][1]] * 60)

# south tower
print('The index for when the time where the south tower saw the fire in the wrfout file is: ', np.where(fuel_frac[:, south_north_s, west_east_s] < 1)[0][1])
print('The time of arrival at the south tower in minutes is:', time[np.where(fuel_frac[:, south_north_s, west_east_s] < 1)[0][1]])
print('The time of arrival at the south tower in seconds is:', time[np.where(fuel_frac[:, south_north_s, west_east_s] < 1)[0][1]] * 60)
'''
# %% Trying to use the fire mesh here instead of the atms mesh. For this I need to use the 2nd domain wrfin file from the real case to see where the fxlat and fxlong are for better accuracy in the file.
print('**************************************************************************************\n')
print('\n')
print('Reading in the second domain wrfin file')
wrfin2 = nc.Dataset('/home/jbenik/FireFlux2/Codes_and_Data/Data/wrf_files/wrfinput_d02_real', 'r')
# The coordinates were taken from the google earth file. The wrfin file from the second domain real case is being used since it has the fire mesh.
print('Getting locations using fire mesh')
#main tower
south_north_wrfout = wrf.ll_to_xy(wrfin2, 29.387975, -95.04142222222222, timeidx = 0, squeeze = False, meta = False, stagger = 'm')[1]
west_east_wrfout = wrf.ll_to_xy(wrfin2, 29.387975, -95.04142222222222, timeidx = 0, squeeze = False, meta = False, stagger = 'm')[0]
print('south_north main tower =', south_north_wrfout)
print('west_east main tower = ', west_east_wrfout)
#west tower
south_north_w = wrf.ll_to_xy(wrfin2, 29.38617222222222, -95.04138611111111, timeidx = 0, squeeze = False, meta = False, stagger = 'm')[1]
west_east_w = wrf.ll_to_xy(wrfin2, 29.38617222222222, -95.04138611111111, timeidx = 0, squeeze = False, meta = False, stagger = 'm')[0]
print('south_north west tower =', south_north_w)
print('west_east west tower = ', west_east_w)

#east tower
south_north_e = wrf.ll_to_xy(wrfin2, 29.38650833333333, -95.0402111111111, timeidx = 0, squeeze = False, meta = False, stagger = 'm')[1]
west_east_e = wrf.ll_to_xy(wrfin2, 29.38650833333333, -95.0402111111111, timeidx = 0, squeeze = False, meta = False, stagger = 'm')[0]
print('south_north east tower =', south_north_e)
print('west_east east tower = ', west_east_e)

#south tower
south_north_s = wrf.ll_to_xy(wrfin2, 29.384775,-95.0403, timeidx = 0, squeeze = False, meta = False, stagger = 'm')[1]
west_east_s = wrf.ll_to_xy(wrfin2, 29.384775,-95.0403, timeidx = 0, squeeze = False, meta = False, stagger = 'm')[0]
print('south_north south tower =', south_north_s)
print('west_east south tower = ', west_east_s)

print('\n')
print('Figuring out where the fire area is greater than zero at the new points and see when the time it does this to compare it to the towers')
# %% seeing where the fire area is greater than zero using the new grid
print('TESTING', fire_area[:, south_north_wrfout, west_east_wrfout])
'''
#main tower
print('The index for when the time where the main tower saw the fire in the wrfout file is: ', np.where(fire_area[:, south_north_wrfout, west_east_wrfout] > 0)[0][0])
print('The time of arrival at the main tower is:', time[np.where(fire_area[:, south_north_wrfout, west_east_wrfout] > 0)[0][0]])

# west tower
print('The index for when the time where the west tower saw the fire in the wrfout file is: ', np.where(fire_area[:, south_north_w, west_east_w] > 0)[0][0])
print('The time of arrival at the west tower is:', time[np.where(fire_area[:, south_north_w, west_east_w] > 0)[0][0]])

# east tower
print('The index for when the time2 where the east tower saw the fire in the wrfout file is: ', np.where(fire_area[:, south_north_e, west_east_e] > 0)[0][0])
print('The time of arrival at the east tower is:', time[np.where(fire_area[:, south_north_e, west_east_e] > 0)[0][0]])

# south tower
print('The index for when the time where the south tower saw the fire in the wrfout file is: ', np.where(fire_area[:, south_north_s, west_east_s] > 0)[0][0])
print('The time of arrival at the east tower is:', time[np.where(fire_area[:, south_north_s, west_east_s] > 0)[0][0]])
'''
