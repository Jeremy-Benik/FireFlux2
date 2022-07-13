#This code will plot the new wrffdda and the new wrfinput to see how they compare to each other.
# %% Importing necessary libraries
import matplotlib.pyplot as plt
import netCDF4 as nc
import xarray as xr
import numpy as np
from metpy import units
from wrf import vinterp, getvar
# %% Reading in the data. I used both xarray and netcdf4 as it's easier to read in data with netcdf and it's easier to view it with xarray
wrffdda_new = nc.Dataset('/home/jbenik/FirefluxII/Codes_and_Data/Data/wrf_files/wrffdda_d01_test4', mode = 'r', format = 'NETCDF4') #reading in the new wrffdda variable
wrfin_real = nc.Dataset('/home/jbenik/FirefluxII/Codes_and_Data/Data/wrf_files/wrfin_adam_real', 'r', format='NETCDF4') #reading in the wrfin_real file using netcdf4 to compare to the file
wrfin_ideal = nc.Dataset('/home/jbenik/FirefluxII/Codes_and_Data/Data/wrf_files/wrfinput_ideal_modified', 'r', format='NETCDF4') #reading in the wrfin from the ideal case to compare the files. This used netcdf4
# %% Reading in the data using xarray to better visualize the dataset in the command console
wrffdda_new_xr = xr.open_dataset('/home/jbenik/FirefluxII/Codes_and_Data/Data/wrf_files/wrffdda_d01_test4') #reading in the new wrffdda variable
wrfin_real_xr = xr.open_dataset('/home/jbenik/FirefluxII/Codes_and_Data/Data/wrf_files/wrfin_adam_real') #reading in the wrfin_real file using xarray
wrfin_ideal_xr = xr.open_dataset('/home/jbenik/FirefluxII/Codes_and_Data/Data/wrf_files/wrfinput_ideal_modified') #reading in the wrfin from the ideal case using xarray
# %% Reading in the variables to make plotting easier'
#reading in the old wrffdda variables first. 
u_old = wrffdda_new.variables['U_NDG_OLD'][:, :, :, :]
v_old = wrffdda_new.variables['V_NDG_OLD'][:, :, :, :]
t_old = wrffdda_new.variables['T_NDG_OLD'][:, :, :, :]
q_old = wrffdda_new.variables['Q_NDG_OLD'][:, :, :, :]
ph_old = wrffdda_new.variables['PH_NDG_OLD'][:, :, :, :]
mu_old = wrffdda_new.variables['MU_NDG_OLD'][:, :, :, :]
#reading in the new wrffdda variables.
u_new = wrffdda_new.variables['U_NDG_NEW'][:, :, :, :]
v_new = wrffdda_new.variables['V_NDG_NEW'][:, :, :, :]
t_new = wrffdda_new.variables['T_NDG_NEW'][:, :, :, :]
q_new = wrffdda_new.variables['Q_NDG_NEW'][:, :, :, :]
ph_new = wrffdda_new.variables['PH_NDG_NEW'][:, :, :, :]
mu_new = wrffdda_new.variables['MU_NDG_NEW'][:, :, :, :]
#reading in the wrfin ideal variables
u_ideal = getvar(wrfin_ideal, "ua", None, units = "m/s")
v_ideal = getvar(wrfin_ideal, "va", None, units = "m/s")
t_ideal = getvar(wrfin_ideal, "temp", None, units = 'K')
q_ideal = wrfin_ideal.variables['QVAPOR'][:, :, :, :]
PH_ideal = wrfin_ideal.variables['PH'][:, :, :, :] #Defining PH to calculate height
PHB_ideal = wrfin_ideal.variables['PHB'][:, :, :, :] #Defining the height pertubation which will then be used to calculate height
height_ideal = 0.5*(PHB_ideal[:,:-1] + PH_ideal[:,:-1] + PHB_ideal[: , 1:] + PH_ideal[:, 1:])/9.81 #calculating height and doing it in a way where it isn't staggered
#reading in the wrfin real variables
u_real = getvar(wrfin_real, "ua", None, units = "m/s")
v_real = getvar(wrfin_real, 'va', None, units = "m/s")
t_real = getvar(wrfin_real, "temp", None, units = 'K')
q_real = wrfin_real.variables['QVAPOR'][:, :, :, :]
PH_real = wrfin_real.variables['PH'][:, :, :, :]
PHB_real = wrfin_real.variables['PHB'][:, :, :, :]
height_real = 0.5*(PHB_real[:,:-1] + PH_real[:,:-1] + PHB_real[: , 1:] + PH_real[:, 1:])/9.81
# %% Making the figure
fig, ax = plt.subplots(2, 2, figsize = (12, 12))
#Making U wind plot
ax[0, 0].plot(u_old[0, :, 30, 30], height_ideal[0, :, 30, 30], label = 'U_old', color = 'red')
ax[0, 0].plot(u_ideal[:, 30, 30], height_ideal[0, :, 30, 30], label = 'V_ideal', color = 'blue')
ax[0, 0].set_xlabel('U wind (m/s)', fontweight = 'bold', fontsize = 10)
ax[0, 0].set_ylabel('Height (m)', fontweight = 'bold', fontsize = 10)
ax[0, 0].legend()
ax[0, 0].grid()
ax[0, 0].set_ylim(0, height_ideal[0, :, 30, 30][-1])
ax[0, 0].set_title('U wind vs Height', fontweight = 'bold', fontsize = 10)
# Making V wind plot
ax[0, 1].plot(v_old[0, :, 30, 30], height_ideal[0, :, 30, 30], label = 'V_old', color = 'red')
ax[0, 1].plot(v_ideal[:, 30, 30], height_ideal[0, :, 30, 30], label = 'V_ideal', color = 'blue')
ax[0, 1].set_xlabel('V wind (m/s)', fontweight = 'bold', fontsize = 10)
ax[0, 1].set_ylabel('Height (m)', fontweight = 'bold', fontsize = 10)
ax[0, 1].legend()
ax[0, 1].grid()
ax[0, 1].set_ylim(0, height_ideal[0, :, 30, 30][-1])
ax[0, 1].set_title('V wind vs Height', fontweight = 'bold', fontsize = 10)
#Making plot of mixing ratio
ax[1, 0].plot(q_old[0, :, 30, 30], height_ideal[0, :, 30, 30], label = 'q_old', color = 'red')
ax[1, 0].plot(q_ideal[0, :, 30, 30], height_ideal[0, :, 30, 30], label = 'q_ideal', color = 'blue')
ax[1, 0].set_xlabel('Q', fontweight = 'bold', fontsize = 10)
ax[1, 0].set_ylabel('Height (m)', fontweight = 'bold', fontsize = 10)
ax[1, 0].grid()
ax[1, 0].legend()
ax[1, 0].set_ylim(0, height_ideal[0, :, 30, 30][-1])
ax[1, 0].set_title('Mixing Ratio vs. Height', fontweight = 'bold', fontsize = 10)
# Making plot of wind speed
ws_ideal = np.sqrt((u_ideal[:, :, :] ** 2) + (v_ideal[:, :, :] ** 2))
ws_old = np.sqrt((u_old[0, :, :, :] ** 2) + (v_old[0, :, :, :] ** 2))
ax[1, 1].plot(ws_old[:, 30, 30], height_ideal[0, :, 30, 30], label = 'ws_old', color = 'red')
ax[1, 1].plot(ws_ideal[:, 30, 30], height_ideal[0, :, 30, 30], label = 'Wind Speed Ideal', color = 'blue')
ax[1, 1].set_xlabel('Wind (m/s)', fontweight = 'bold', fontsize = 10)
ax[1, 1].set_ylabel('Height (m)', fontweight = 'bold', fontsize = 10)
ax[1, 1].legend()
ax[1, 1].grid()
ax[1, 1].set_ylim(0, height_ideal[0, :, 30, 30][-1])
ax[1, 1].set_title('Wind vs Height', fontweight = 'bold', fontsize = 10)

plt.tight_layout()
plt.show()






# %%
