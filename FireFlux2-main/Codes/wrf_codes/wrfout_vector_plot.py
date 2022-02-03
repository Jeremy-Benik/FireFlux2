import matplotlib.pyplot as plt
import numpy as np
import xarray as xr
import netCDF4 as nc
from wrf import getvar, interplevel

df1 = xr.open_dataset('/home/jbenik/FirefluxII/Codes_and_Data/Data/wrf_files/wrfout_d01_2013-01-30_15:00:00')
df = nc.Dataset('/home/jbenik/FirefluxII/Codes_and_Data/Data/wrf_files/wrfout_d01_2013-01-30_15:00:00', 'r', 
    format='NETCDF4') 
k = 5

levels = [20, 10, 5.77, 5.33]
uu = []
vv = []
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
uu = np.array(uu)
vv = np.array(vv)
ws = np.array(np.sqrt(np.sqrt((uu ** 2) + (vv ** 2))))
nt = uu.shape[-1]
ft = nt * dt
u = uu[:, ::k]
v = vv[:, ::k]
time = np.linspace(0, ft, nt)
height = np.tile(levels, (len(time), 1)).swapaxes(0, 1)
time = np.tile(time, (len(levels), 1))
colors = ['black', 'green', 'red', 'blue']
fig, ax = plt.subplots(figsize = (12, 12))
for c in range(len(u)):
    ax.quiver(time[c,::k], height[c,::k], u[c], -v[c], color = colors[c])
ax.set_ylim([0, 25])
ax.set_title("WRFOUT Vector Plot at 20m, 10m, 5.77m, 5.33m AGL", fontsize = 20, fontweight = 'bold')
ax.set_xlabel("Time (seconds)", fontsize = 18, fontweight = 'bold')
ax.set_ylabel("Height (m)", fontsize = 18, fontweight = 'bold')
ax.legend(['20 meters AGL', '10 meters AGL', '5.77 meters AGL', '5.33 meters AGL'])
plt.show()
