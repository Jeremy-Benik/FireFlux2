import pandas as pd
import matplotlib.pyplot as plt
import xarray as xr
import netCDF4 as nc
import numpy as np
import statistics as st
# %% Information about the file
''' TITLE:  OUTPUT FROM REAL_EM V4.2 PREPROCESSOR
    START_DATE: 2013-01-30_20:30:00
    WEST-EAST_GRID_DIMENSION: 200
    SOUTH-NORTH_GRID_DIMENSION: 320
    BOTTOM-TOP_GRID_DIMENSION: 160'''
# %% Reading in the file using both xarray and netCDF4
df_1 = nc.Dataset('/home/jbenik/FirefluxII/Codes_and_Data/Data/wrf_files/wrffdda_d01', 'r', format='NETCDF4') #this reads in the file using xarray so I can better see what's in the file
df_2 = nc.Dataset('/home/jbenik/FirefluxII/Codes_and_Data/Data/wrf_files/wrffdda_d02', 'r', format='NETCDF4') #this reads in the file using netCDF4 so I can analyze and plot the data
# %%
u_old_1 = df_1.variables['U_NDG_OLD'][0, :, :, :]
v_old_1 = df_1.variables['V_NDG_OLD'][0, :, 30, 30]

u_new_1 = df_1.variables['U_NDG_NEW'][0, :, :, :]
v_new_1 = df_1.variables['V_NDG_NEW'][0, :, 30, 30]

u_old_2 = df_2.variables['U_NDG_OLD'][0, :, :, :]
v_old_2 = df_2.variables['V_NDG_OLD'][0, :, 30, 30]

u_new_2 = df_2.variables['U_NDG_NEW'][0, :, 30, 30]
v_new_2 = df_2.variables['V_NDG_NEW'][0, :, 30, 30]

Q_old_1 = df_1.variables['Q_NDG_OLD'][0, :, 30, 30]
T_old_1 = df_1.variables['T_NDG_OLD'][0, :, 30, 30]

Q_new_1 = df_1.variables['Q_NDG_NEW'][0, :, 30, 30]
T_new_1 = df_1.variables['T_NDG_NEW'][0, :, 30, 30]

Q_old_2 = df_2.variables['Q_NDG_OLD'][0, :, 30, 30]
T_old_2 = df_2.variables['T_NDG_OLD'][0, :, 30, 30]

Q_new_2 = df_2.variables['Q_NDG_NEW'][0, :, 30, 30]
T_new_2 = df_2.variables['T_NDG_NEW'][0, :, 30, 30]
variables = [u_new_1, u_old_2, v_new_1, v_old_2, Q_new_1, Q_old_2, T_new_1, T_old_2]#new vals in first step same as old values in second step

variables_names = ['u_new_1', 'u_old_2', 'v_new_1', 'v_old_2', 'Q_new_1', 'Q_old_2', 'T_new_1', 'T_old_2']#new vals in first step same as old values in second step

# %%
for i in range(len(variables)):
    if i == 7:
        break
    print("There are no differences between variables", variables_names[i], "and", variables_names[i + 1])
    print(np.array_equal(variables[i], variables[i + 1]))
