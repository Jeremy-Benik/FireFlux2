# %%
import netCDF4 as nc
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import xarray as xr
from wrf import getvar, interplevel
df = nc.Dataset('/home/jbenik/FirefluxII/Codes_and_Data/Data/wrf_files/wrffdda_d01', 'r', format='NETCDF4')
df1 = xr.open_dataset('/home/jbenik/FirefluxII/Codes_and_Data/Data/wrf_files/wrffdda_d01')
# %%
'''2. Grab the new wrffdda from /home/akochanski/wrfxpy/wksp/FF2_real/wrf and try to plot time series 
of the variables at a selected location. 
There will be 6 time frames in the file (at 10 min intervals) covering the first hour. '''
x = 30
y = 30
level = 1
time = df.variables['Times'][:]
#times = getvar(df, 'times')
times = ['20:30:00', '20:40:00', '20:50:00',
       '21:00:00', '21:10:00', '21:20:00']
U_old = df.variables['U_NDG_OLD'][:, level, x, y] #old u wind m/s

#U_old2 = np.array(np.tile(U_old, (time.shape[1], 1)).swapaxes(1, 0))
V_old = df.variables['V_NDG_OLD'][:, level, x, y] #old v wind m/s
Q_old = df.variables['Q_NDG_OLD'][:, level, x, y] #old mixing ratio kg/kg
T_old = df.variables['T_NDG_OLD'][:, level, x, y] #old pert pot temp K (-300)
T_old += 300 #adding 300 since that was originally taken away
PH_old = df.variables['PH_NDG_OLD'][:, level, x, y] #old pert height kg/kg
#PH_old /= 9.81
#These are all the new variables
U_new = df.variables['U_NDG_NEW'][:, level, x, y] #new u wind
V_new = df.variables['V_NDG_NEW'][:, level, x, y] #new v wind
Q_new = df.variables['Q_NDG_NEW'][:, level, x, y] #new mixing ratio
T_new = df.variables['T_NDG_NEW'][:, level, x, y] #new pert pot temp
T_new += 300 #adding 300 since that was originally taken away
PH_new = df.variables['PH_NDG_NEW'][:, level, x, y] #new pert height
#here I am trying to shift new by one time step
u_new = []
v_new = []
q_new = []
t_new = []
ph_new = []
U_new = df.variables['U_NDG_NEW'][:]
U_new = df.variables['U_NDG_NEW'][:]
V_new = df.variables['V_NDG_NEW'][:]
Q_new = df.variables['Q_NDG_NEW'][:]
T_new = df.variables['T_NDG_NEW'][:]
T_new += 300 
PH_new = df.variables['PH_NDG_NEW'][:]
x = 30
y = 30
level = 1
u_new = []
for idx, vals in enumerate(times):
    if idx + 1 < len(times):
        u_new.append(U_new[idx , level, x, y])
        v_new.append(V_new[idx , level, x, y])
        q_new.append(Q_new[idx , level, x, y])
        t_new.append(T_new[idx , level, x, y])
        ph_new.append(PH_new[idx , level, x, y])
    else:
        break

              
#time = np.tile(times, (U_new.shape[1], 1)).swapaxes(1, 0)
#time = np.array(time)
# %%

fig, ax = plt.subplots(3, 2, figsize = (15, 10))
ax[0, 0].plot(times, U_old, label = 'U_old', color = 'red')
ax[0, 0].plot(times[1:], u_new, label = 'U_new', color = 'blue', linestyle = '--')
ax[0, 0].set_xlabel('Time', fontsize = 12, fontweight = 'bold')
ax[0, 0].set_ylabel('U Wind (m/s)', fontsize = 12, fontweight = 'bold')
ax[0, 0].set_title(f'U Wind vs Time at level {level}', fontsize = 12, fontweight = 'bold')
ax[0, 0].tick_params(axis = 'x', labelrotation = 45)
ax[0, 0].legend()

ax[0, 1].plot(times, V_old, label = 'V_old', color = 'red')
ax[0, 1].plot(times[1:], v_new, label = 'V_new', color = 'blue', linestyle = '--')
ax[0, 1].set_xlabel('Time', fontsize = 12, fontweight = 'bold')
ax[0, 1].set_ylabel('V Wind (m/s)', fontsize = 12, fontweight = 'bold')
ax[0, 1].set_title(f'V Wind vs Time at level {level}', fontsize = 12, fontweight = 'bold')
ax[0, 1].tick_params(axis = 'x', labelrotation = 45)
ax[0, 1].legend()

ax[1, 0].plot(times, Q_old, label = 'Q_old', color = 'red')
ax[1, 0].plot(times[1:], q_new, label = 'Q_new', color = 'blue', linestyle = '--')
ax[1, 0].set_xlabel('Time', fontsize = 12, fontweight = 'bold')
ax[1, 0].set_ylabel('Water Vapor mising ratio (kg/kg)', fontsize = 12, fontweight = 'bold')
ax[1, 0].set_title(f'Water Vapor mixing ratio vs Time at level {level}', fontsize = 12, fontweight = 'bold')
ax[1, 0].tick_params(axis = 'x', labelrotation = 45)
ax[1, 0].legend()

ax[1, 1].plot(times, T_old, label = 'T_old', color = 'red')
ax[1, 1].plot(times[1:], t_new, label = 'T_new', color = 'blue', linestyle = '--')
ax[1, 1].set_xlabel('Time', fontsize = 12, fontweight = 'bold')
ax[1, 1].set_ylabel('Temperature (K)', fontsize = 12, fontweight = 'bold')
ax[1, 1].set_title(f'Temperature vs Time at level {level}', fontsize = 12, fontweight = 'bold')
ax[1, 1].tick_params(axis = 'x', labelrotation = 45)
ax[1, 1].legend()

ax[2, 1].plot(times, PH_old, label = 'PH_old', color = 'red')
ax[2, 1].plot(times[1:], ph_new, label = 'PH_new', color = 'blue', linestyle = '--')
ax[2, 1].set_xlabel('Time', fontsize = 12, fontweight = 'bold')
ax[2, 1].set_ylabel('Pert Height (kg/kg)', fontsize = 12, fontweight = 'bold')
ax[2, 1].set_title(f'Pert Height (kg/kg) vs Time at level {level}', fontsize = 12, fontweight = 'bold')
ax[2, 1].tick_params(axis = 'x', labelrotation = 45)
ax[2, 1].legend()

plt.suptitle("All Variables From wrffdda_d01 file for 2013-01-30 (new vars are time shifted)", fontsize = 18, fontweight = 'bold')
plt.tight_layout()
plt.show()
