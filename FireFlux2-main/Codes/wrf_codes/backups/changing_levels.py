import netCDF4 as nc
import xarray as xr
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd 
from wrf import interplevel, vinterp, interpline, getvar 
# %%
wrfin_ideal = nc.Dataset('/home/jbenik/FirefluxII/Codes_and_Data/Data/wrf_files/wrfinput_ideal', 'r', format='NETCDF4')
wrfin_real = nc.Dataset('/home/jbenik/FirefluxII/FireFlux2_modified_input_sounding/FireFlux2_base/wrfinput_d01', 'r', format='NETCDF4')
wrfin_mod = nc.Dataset('/home/jbenik/FirefluxII/Codes_and_Data/Data/wrf_files/wrfinput_d01_modified', 'a', format='NETCDF4')
wrffdda = nc.Dataset('/home/jbenik/FirefluxII/Codes_and_Data/Data/wrf_files/wrffdda_d01', 'r', format='NETCDF4')
# %% wrfin variables
U_ideal = getvar(wrfin_ideal, "ua", None, units = "m/s")
V_ideal = getvar(wrfin_ideal, 'va', None, units = "m/s")
PH_ideal = wrfin_ideal.variables['PH'][:, :, :, :]
PHB_ideal = wrfin_ideal.variables['PHB'][:, :, :, :]
height_ideal = 0.5*(PHB_ideal[:,:-1] + PH_ideal[:,:-1] + PHB_ideal[: , 1:] + PH_ideal[:, 1:])/9.81
#wrfin heights are always the same everywhere. 
height_ideal = np.array(height_ideal[0, :, 0, 0]) #these are the heights I need to interpolate from
#but I need the wrfin from the wrffdda run to get these new heights
#then with these new heights, interplevel to these new heights
#use vinterp for this part as I can already use a list for that. 
#the vinterp first argument is a wrfin, second is the var from wrffdda, the third one is height (’ght_agl’: grid point height agl [km])
#THIS IS IN KM!!! I will need to provide those in KM

#to put data into the files, I will use netcdf, change the 'r' to a 'a'
#nc.Dataset(‘path’,’a’) #this means append mode.
#the default mode is read mode, but I need to change that
#to actaully put a var in the file, I will need to do:
#ex: ds = nc.Dataset(‘path’,’a’)
#lets wrtie the u var (u = ds.variables[‘U’])
#u[:] = array
#u[0, :, 0, 0] = array
#MAKE A COPY OF THE FILES IN CASE I MESS UP!!!!
# %% wrffdda variables
U_old = wrffdda.variables['U_NDG_OLD'][0, :, :, :]
U_new = wrffdda.variables['U_NDG_NEW'][0, :, :, :]
V_old = wrffdda.variables['V_NDG_OLD'][0, :, :, :]
V_new = wrffdda.variables['V_NDG_NEW'][0, :, :, :]
T_old = wrffdda.variables['T_NDG_OLD'][0, :, :, :]
T_new = wrffdda.variables['T_NDG_NEW'][0, :, :, :]
Q_old = wrffdda.variables['Q_NDG_OLD'][0, :, :, :]
Q_new = wrffdda.variables['Q_NDG_NEW'][0, :, :, :]
PH_old = wrffdda.variables['PH_NDG_OLD'][0, :, :, :]
PH_new = wrffdda.variables['PH_NDG_NEW'][0, :, :, :]


#U_old_interp = interplevel(U_old, height)
#this should return a 2d array, then concatenate all heights to get a 3d array.
#this would be for both wrfin and wrffdda

# %%
#need to find a variable that has the height saved into it.
#I will need some variable to get the value at the point.
#the wrf library gives you the value at the paticular height
#All I need to do is ask what heights am I comparing too.
#I can interpolate a series of levels using that library.
#to make it easier to compare, I should decide. 
#Stick to the coarser level. The var that has less resolution
#less data, so I can only go to that accuracy. Stick to the coarser one (one with less data)
#thought I just had. So I want to interpolate to the levels of the wrfinput since there aren't as many
#so somehow using wrfinterp, interpolate to the levels in height and all the variables
#so for picking points, pick some heights like 1m, 2m, 3m, etc...
#Should end up with a 3d array. One of the 3d dimensions will be height that 
#i will be creating
#create some range between height1 min and max and try to interpolate levels
#more of a question for Adam.
#wrfin is staggered (middle of the cube) but interpolating the wrfin should as for the one at the center

#the times are 5 hours off. Ask Adam about this. 
#ask adam about the heights from the wrffdda files. There is no height in the file
#is there any other file to get the height for the wrffdda? There's likely to be a file with the height
#i need his wrfinput file from his case. Since there will be the same heights from those files. 
#get the height from the wrfinput
#interpolate the wrffdda into those heights
#to write into the wrfinput, that may always be the same height (for the U and V)
#need the height at one location and interpolate those locations