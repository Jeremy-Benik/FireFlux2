import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import xarray as xr
import netCDF4 as nc
from wrf import getvar, interplevel
from wrf import vinterp

#%% Importing the data using xarray and netcdf 
df1 = xr.open_dataset('/home/jbenik/FirefluxII/Codes_and_Data/Data/wrf_files/wrfout_d01_2013-01-30_15:00:00') #by using xarray, I can see the information of the file
#better than with netcdf
df = nc.Dataset('/home/jbenik/FirefluxII/Codes_and_Data/Data/wrf_files/wrfout_d01_2013-01-30_15:00:00', 'r', 
    format='NETCDF4') #using netcdf, this allows me to get the variables how I want to.
k = 5

#levels = [5.33, 5.77, 10, 20]
levels = [5.33, 20]
uu = []
vv = []
#ws = []
#colors = []
for i in levels:
    print("I am currently working at", i, "meters")
    time1 = df.variables['XTIME'][1]
    time0 = df.variables['XTIME'][0]
    dt = time1 - time0
    U = getvar(df, "ua", None, units = "m/s")
    V = getvar(df, "va", None, units = "m/s")
    ht = getvar(df, "z", units="m", msl = False)
    U_h = interplevel(U, ht, i)[30, 30]
    V_h = interplevel(V, ht, i)[30, 30]
    uu.append(U_h)
    vv.append(V_h)
    #level.append(level)
    #colors.append(levels.index(i))
#colors = np.array(colors)
uu = np.array(uu)
vv = np.array(vv)
ws = np.array(np.sqrt(np.sqrt((uu ** 2) + (vv ** 2))))
nt = uu.shape[-1]
ft = nt * dt
time = np.linspace(0, ft, nt)
height = np.tile(levels, (len(time), 1)).swapaxes(0, 1)
time = np.tile(time, (len(levels), 1))
u = uu[:, ::k]
v = vv[:, ::k]

# %%
colors = ['black', 'green', 'red', 'blue']
#comprehension loop. first is element I want to use as the iterator. outer most comment
#color1 = [e for g in [[c]*u.shape[1] for c in colors] for e in g]
fig, ax = plt.subplots(figsize = (12, 12))
for c in range(len(u)):
    ax.quiver(time[c,::k], height[c,::k], u[c], -v[c], color = colors[c])
#ax.quiver(time[:,::k], height[:,::k], u, -v, color = color1)
ax.set_ylim([0, 25])
ax.set_title("WRFOUT Vector Plot at 20m, 10m, 5.77m, and 5.33m", fontsize = 20, fontweight = 'bold')
ax.set_xlabel("Time (seconds)", fontsize = 18, fontweight = 'bold')
ax.set_ylabel("Height (m)", fontsize = 18, fontweight = 'bold')
ax.legend(['5.33m AGL', '20m AGL'])
#cbar = plt.colorbar(ws)
#cbar.set_label('Wind Speeds (m/s)')
plt.show()
# %%
