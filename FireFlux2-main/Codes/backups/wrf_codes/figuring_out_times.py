# %%
import netCDF4 as nc
import numpy as np
import pandas as pd
# %% Importing the Dataset
df = nc.Dataset('/home/jbenik/FirefluxII/Codes_and_Data/Data/wrf_files/wrfout_d01_2013-01-30_15:00:00', 'r')
# %% Importing times 
time = df.variables['XTIME'][:]
u = df.variables['U'][:, :, :, :]
#This time is in minutes, * 60 for seconds