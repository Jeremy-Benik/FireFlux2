# -*- coding: utf-8 -*-
"""
Created on Sat March 15 11:36:54 2022

@author: Jeremy Benik
"""
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
wrfout = nc.Dataset('/home/jbenik/FireFlux2/Codes_and_Data/Data/wrf_files/wrfout_d01_2013-01-30_15:00:00', 'r')
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
