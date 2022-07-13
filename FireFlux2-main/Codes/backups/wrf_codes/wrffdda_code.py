#this file will open the wrffdda files, create a plot of the U, V, W winds and Q (hopefully), 
#Then compare that to the winds of the wrfinput file to see how they match up
#After that, then transfer the data from the wrfinput with the new input_sounding file to the wrffdda file

# %% Importing necessary libraries
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
df1 = xr.open_dataset('/home/jbenik/FirefluxII/Codes_and_Data/Data/wrf_files/wrffdda_d01') #this reads in the file using xarray so I can better see what's in the file
df = nc.Dataset('/home/jbenik/FirefluxII/Codes_and_Data/Data/wrf_files/wrffdda_d01', 'r', format='NETCDF4') #this reads in the file using netCDF4 so I can analyze and plot the data
wrfin = nc.Dataset('/home/jbenik/FirefluxII/FireFlux2_modified_input_sounding/FireFlux2_base/wrfinput_d01', 'r', format='NETCDF4') #opening the wrfinput file using netCDF
wrfin2 = xr.open_dataset('/home/jbenik/FirefluxII/FireFlux2_modified_input_sounding/FireFlux2_base/wrfinput_d01')
df2 = pd.read_csv('/home/jbenik/FirefluxII/Codes_and_Data/Data/sounding_files/modified_sounding.csv', skiprows = [1])
# %% Once you know the location, change these variables to match them.
x = 30
y = 30
t = 0 #since this is being compared to a wrfinput file, and those only have one timestep, I am just
#using the first timestep in the file. I may need to change this later. 
# %% Reading in variables
#These are all the old variables
U_old = df.variables['U_NDG_OLD'][t, :, x, y] #old u wind m/s
V_old = df.variables['V_NDG_OLD'][t, :, x, y] #old v wind m/s
Q_old = df.variables['Q_NDG_OLD'][t, :, x, y] #old mixing ratio kg/kg
T_old = df.variables['T_NDG_OLD'][t, :, x, y] #old pert pot temp K (-300)
T_old += 300 #adding 300 since that was originally taken away
PH_old = df.variables['PH_NDG_OLD'][t, :, x, y] #old pert height kg/kg
#PH_old /= 9.81
#These are all the new variables
U_new = df.variables['U_NDG_NEW'][t, :, x, y] #new u wind
V_new = df.variables['V_NDG_NEW'][t, :, x, y] #new v wind
Q_new = df.variables['Q_NDG_NEW'][t, :, x, y] #new mixing ratio
T_new = df.variables['T_NDG_NEW'][t, :, x, y] #new pert pot temp
T_new += 300 #adding 300 since that was originally taken away
PH_new = df.variables['PH_NDG_NEW'][t, :, x, y] #new pert height
#PH_new /= 9.81
#These are all the wrfin variables
u = wrfin.variables['U'][t, :, x, y] #defining the U wind and setting that to u
v = wrfin.variables['V'][t, :, x, y] #defining the v wind and setting that to v
Q = wrfin.variables['QVAPOR'][t, :, x, y]
temps = wrfin.variables['T'][t, :, x, y]
t = temps + 300
PH = wrfin.variables['PH'][:, :, x, y]
PHB = wrfin.variables['PHB'][:, :, x, y]
height = (0.5*(PHB[:,:-1] + PH[:,:-1] + PHB[: , 1:] + PH[:, 1:])/9.81)[0]
#These are all the input_sound vars
h = df2['Height']
u_wind = df2['u']
v_wind = df2['v']
pot = df2['Potential_Temp']
mix = df2['mixing_ratio']
mix /= 1000
# Creating a figure and seeing if I can plot these
fig, ax = plt.subplots(2, 2, figsize = (12, 12))
ax[0, 0].plot(T_old, PH_old, label = 'Old Temp vs Height', color = 'blue')
ax[0, 0].plot(T_new, PH_new, label = 'New Temp vs Height', color = 'red', linestyle = '-')
#ax[0, 0].plot(t, height, label = 'wrfin t vs h', color = 'purple')
#ax[0, 0].plot(pot, h, label = 'sounding t vs h', color = 'black', linestyle = '--')
#ax[0, 0].set_ylim(0, PH_old[137])
#ax[0, 0].set_xlim(260, 300)
ax[0, 0].set_xlabel('Pot Pert Temp with 300 K added', fontweight = 'bold', fontsize = 12)
ax[0, 0].set_title('Temp Vs. Height', fontweight = 'bold', fontsize = 12)
ax[0, 0].set_ylabel('Pert Geo height', fontweight = 'bold', fontsize = 12)
ax[0, 0].legend()
ax[0, 1].plot(U_old, PH_old, label = 'Old U vs Height')
ax[0, 1].plot(U_new, PH_new, label = 'New U vs Height', color = 'red', linestyle = '-')
#ax[0, 1].plot(u, height, label = 'wrfin u vs h', color = 'purple')
#ax[0, 1].plot(u_wind, h, label = 'sounding u vsh', color = 'black', linestyle = '--')
#ax[0, 1].set_ylim(0, PH_old[137])
ax[0, 1].set_xlabel('U wind (m/s)', fontweight = 'bold', fontsize = 12)
ax[0, 1].set_title('U Vs. Height', fontweight = 'bold', fontsize = 12)
ax[0, 1].set_ylabel('Pert Geo height', fontweight = 'bold', fontsize = 12)
ax[0, 1].legend()
ax[1, 0].plot(V_old, PH_old, label = 'Old V vs Height')
ax[1, 0].plot(V_new, PH_new, label = 'New V vs Height', color = 'red', linestyle = '-')
#ax[1, 0].plot(v, height, label = 'wrfin v vs h', color = 'purple')
#ax[1, 0].plot(v_wind, h, label = 'sounding v vs h', color = 'black', linestyle = '--')
#ax[1, 0].set_ylim(0, PH_old[137])
ax[1, 0].set_xlabel('V wind (m/s)', fontweight = 'bold', fontsize = 12)
ax[1, 0].set_title('V Vs. Height', fontweight = 'bold', fontsize = 12)
ax[1, 0].set_ylabel('Pert Geo height', fontweight = 'bold', fontsize = 12)
ax[1, 0].legend()
ax[1, 1].plot(Q_old, PH_old, label = 'Old Q vs Height')
ax[1, 1].plot(Q_new, PH_new, label = 'New Q vs Height', color = 'red', linestyle = '-')
#ax[1, 1].plot(Q, height, label = 'wrfin Q vs h', color = 'purple')
#ax[1, 1].plot(mix, h, label = 'sounding q vs h', color = 'black', linestyle = '--')
#ax[1, 1].set_ylim(0, PH_old[137])
ax[1, 1].set_xlabel('Mixing ratio (kg/kg)', fontweight = 'bold', fontsize = 12)
ax[1, 1].set_title('Mixing ratio Vs. Height', fontweight = 'bold', fontsize = 12)
ax[1, 1].set_ylabel('Pert Geo height', fontweight = 'bold', fontsize = 12)
ax[1, 1].legend()
plt.suptitle('wrffdda old vs new vs wrfinput vs sounding', fontweight = 'bold', fontsize = 12)
plt.tight_layout()
plt.show()
# %%
print("These are the calculated differences between old and new")
print('Mean difference between them are', st.mean(U_old - U_new))