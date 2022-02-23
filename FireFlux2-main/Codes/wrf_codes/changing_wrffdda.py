#This code appends data onto the existing wrffdda files using the interpolated wrfin from the ideal and real case. 
#Author: Jeremy Benik

# %% Importing necessary libraries
import netCDF4 as nc #This library is used to open the netCDF files
import xarray as xr #This library was used to open the netCDF files in a different way to better view them
import matplotlib.pyplot as plt #This library is used to plot the data to better visualize it as see if the changes
#that I made to the variables are accurate
import numpy as np 
import pandas as pd 
from wrf import vinterp, getvar #These are used to read in the wrf variables and to interpolate the variables at a list of heights. 
# %% Calling in the files and defining them
wrfin_ideal = nc.Dataset('/home/jbenik/FirefluxII/Codes_and_Data/Data/wrf_files/wrfinput_ideal_modified', 'r', format='NETCDF4')
wrfin_real = nc.Dataset('/home/jbenik/FirefluxII/Codes_and_Data/Data/wrf_files/wrfin_adam_real', 'r', format='NETCDF4')
wrffdda = nc.Dataset('/home/jbenik/FirefluxII/Codes_and_Data/Data/wrf_files/wrffdda_d01', 'r', format='NETCDF4')
# %% wrfin variables
U_ideal = getvar(wrfin_ideal, "ua", None, units = "m/s") 
V_ideal = getvar(wrfin_ideal, "va", None, units = "m/s") 
T_ideal = getvar(wrfin_ideal, "temp", None, units = 'K')
ph_ideal = getvar(wrfin_ideal, "geopt", None) 
Q_ideal = wrfin_ideal.variables['QVAPOR'][:, :, :, :] 
PH_ideal = wrfin_ideal.variables['PH'][:, :, :, :] 
PHB_ideal = wrfin_ideal.variables['PHB'][:, :, :, :] 
height_ideal = 0.5*(PHB_ideal[:,:-1] + PH_ideal[:,:-1] + PHB_ideal[: , 1:] + PH_ideal[:, 1:])/9.81 
height_ideal /= 1000
# %% wrfin real variables
U_real = getvar(wrfin_real, "ua", None, units = "m/s")

V_real = getvar(wrfin_real, 'va', None, units = "m/s")
PH_real = wrfin_real.variables['PH'][:, :, :, :]
PHB_real = wrfin_real.variables['PHB'][:, :, :, :]
height_real = 0.5*(PHB_real[:,:-1] + PH_real[:,:-1] + PHB_real[: , 1:] + PH_real[:, 1:])/9.81

height_real /= 1000
# %% wrffdda variables
print("Assigning wrffdda variables")
times = wrffdda.variables['Times'][:]
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
MU_new = wrffdda.variables['MU_NDG_NEW'][0, :, :, :]
MU_old = wrffdda.variables['MU_NDG_OLD'][0, :, :, :]
# %% Here I will interpolate the heights of the wrffdda to the heights of the wrfinput
print("Interpolating the heights from the wrfin_real")
wrffdda_u_old_height = vinterp(wrfin_real, U_old, 'ght_agl', height_real[0, :, 0, 0], extrapolate = True)
wrffdda_v_old_height = vinterp(wrfin_real, V_old, 'ght_agl', height_real[0, :, 0, 0], extrapolate = True)
wrffdda_t_old_height = vinterp(wrfin_real, T_old, 'ght_agl', height_real[0, :, 0, 0], extrapolate = True)
wrffdda_q_old_height = vinterp(wrfin_real, Q_old, 'ght_agl', height_real[0, :, 0, 0], extrapolate = True)
wrffdda_u_new_height = vinterp(wrfin_real, U_new, 'ght_agl', height_real[0, :, 0, 0], extrapolate = True)
wrffdda_v_new_height = vinterp(wrfin_real, V_new, 'ght_agl', height_real[0, :, 0, 0], extrapolate = True)
wrffdda_t_new_height = vinterp(wrfin_real, T_new, 'ght_agl', height_real[0, :, 0, 0], extrapolate = True)
wrffdda_q_new_height = vinterp(wrfin_real, Q_new, 'ght_agl', height_real[0, :, 0, 0], extrapolate = True)
print("Interpolating the heights from the wrfin_ideal")
wrfin_u = vinterp(wrfin_ideal, wrffdda_u_old_height, 'ght_agl', height_ideal[0, :, 0, 0], extrapolate = True)
wrfin_v = vinterp(wrfin_ideal, wrffdda_v_old_height, 'ght_agl', height_ideal[0, :, 0, 0], extrapolate = True)
wrfin_q = vinterp(wrfin_ideal, wrffdda_q_old_height, 'ght_agl', height_ideal[0, :, 0, 0], extrapolate = True)
wrfin_t = vinterp(wrfin_ideal, wrffdda_t_old_height, 'ght_agl', height_ideal[0, :, 0, 0], extrapolate = True)
#wrfin_mu = vinterp(wrfin_ideal, wrffdda_mu_old_height, 'ght_agl', height_ideal[0, :, 0, 0])
# %% Writing to the file
#defining the file. Note, this is not the wrffdda file, I made a copy and wrote my changes to that file. 
wrffdda_mod = nc.Dataset('/home/jbenik/FirefluxII/Codes_and_Data/Data/wrf_files/wrffdda_d01_mod', 'a', format='NETCDF4') #This is a copied file from the wrffdda and is the file that I will be writing my data to. 

#Changing the u_old winds
u_old_changed = wrffdda_mod.variables['U_NDG_OLD']
u_old_changed[0] = wrfin_u
u_old_changed[1] = wrfin_u
#Changing the U_new winds
u_new_changed = wrffdda_mod.variables['U_NDG_NEW']
u_new_changed[0] = wrfin_u
u_new_changed[1] = wrfin_u
#Changing the v_old winds
v_old_changed = wrffdda_mod.variables['V_NDG_OLD']
v_old_changed[0] = wrfin_v
v_old_changed[1] = wrfin_v
#changing the v_new winds
v_new_changed = wrffdda_mod.variables['V_NDG_NEW']
v_new_changed[0] = wrfin_v
v_new_changed[1] = wrfin_v
#changing the t_old winds
t_old_changed = wrffdda_mod.variables['T_NDG_OLD']
t_old_changed[0] = wrfin_t
t_old_changed[1] = wrfin_t
#Changing the t_new winds
t_new_changed = wrffdda_mod.variables['T_NDG_NEW']
t_new_changed[0] = wrfin_t
t_new_changed[1] = wrfin_t
#changing the q_old values
q_old_changed = wrffdda_mod.variables['Q_NDG_OLD']
q_old_changed[0] = wrfin_q
q_old_changed[1] = wrfin_q
#changing the q_new variables
q_new_changed = wrffdda_mod.variables['Q_NDG_NEW']
q_new_changed[0] = wrfin_q
q_new_changed[1] = wrfin_q
#closing the file
wrffdda_mod.close()
