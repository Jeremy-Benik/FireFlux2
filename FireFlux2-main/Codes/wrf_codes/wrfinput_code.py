# -*- coding: utf-8 -*-
"""
Created on Sun Nov  7 19:27:25 2021

@author: Jeremy Benik
"""
#I belive he wants me to plot u v and W and moisture profiles to see how it compares to the original file
# %% Importing libraries
import matplotlib.pyplot as plt
import pandas as pd
#from metpy.plots import SkewT, Hodograph
#from metpy.units import units
#import metpy.calc as mpcalc
#from mpl_toolkits.axes_grid1.inset_locator import inset_axes
import numpy as np
import xarray as xr
import netCDF4 as nc
#import cartopy.crs as ccrs
#import cartopy.feature as cfeature
#from wrf import getvar, interplevel
#Path = /home/jbenik/FirefluxII/fireflux2_3
# %% #reading in the file
# df = xr.open_dataset('wrfinput_d01') 
# df1 = nc.Dataset('wrfinput_d01') 
df1 = nc.Dataset('/home/jbenik/FirefluxII/FireFlux2_modified_input_sounding/FireFlux2_base/wrfinput_d01', 'r', format='NETCDF4') #opening the file using netcdf
df = xr.open_dataset('/home/jbenik/FirefluxII/FireFlux2_modified_input_sounding/FireFlux2_base/wrfinput_d01') # opening the file using xarray since it opens it a different way
print(df1.variables.keys())
print(df.info())
levels = [5.33, 5.77, 10, 20]

#height = getvar(df1, "height_agl")

#pblh = getvar(df1, "PBLH")
# u_h = interplevel(u, height, levels)
# v_h = interplevel(v, height, levels)
# w_h = interplevel(w, height, levels) 
# print('U winds at 5.77m, 10m, 20m', u_h[:, 0, 0].values)
# print('V winds at 5.77m, 10m, 20m', v_h[:, 0, 0].values)
# print('W winds at 5.77m, 10m, 20m', w_h[:, 0, 0].values)

#see what these codes say vs the actual data. See how different they are in the wrf code (this code)
#versus how differnt they are vs actual tower data
#next will be plotting the wrfout to see how it changes in the wrfout vs modified input_sounding
#print(df1.variables.keys()) #this is used to see all the variables in the dataframe
lat = df1.variables['XLAT'][:]
lon = df1.variables['XLONG'][:]
#lon, lat = np.meshgrid(lon, lat)
# %%
u = df1.variables['U'][:] #defining the U wind and setting that to u
v = df1.variables['V'][:] #defining the v wind and setting that to v
w = df1.variables['W'][:] #defining the w wind and setting that to w
pres = df1.variables['P'][:] #defining pressure and setting it to p this is in pa
u10 = df1.variables['U10'][:] #defining u at 10 meters as u10
v10 = df1.variables['V10'][:] #defining v at 10 meters as v10
temp = df1.variables['T00'][:]
temps = df1.variables['T'][:]
height = df1.variables['ZSF'][:]
pressure = df1.variables['PB'][:]
PH = df.variables['PH'][:]
PHB = df.variables['PHB'][:]
Q = df1.variables['QVAPOR'][:]
# %% Attempting to make a plot of the variables vs Height (200m)
#print(df.info())
u_wind = []
v_wind = []
p = []
wind = []
t = []
ph = []
phb = []
q = []
p = []
for i in range(0, 80):
    u_wind.append(u[0, i, 0, 0])
    v_wind.append(v[0, i, 0, 0])
    p.append(pressure[0, i, 0, 0] / 100) #i can plot versus pressure if need be too
    wind.append(np.sqrt((u[0, i, 0, 0] ** 2) + (v[0, i, 0, 0] ** 2)))
    t.append(temps[0, i, 0, 0])
    q.append(Q[0, i, 0, 0] * 1000)
    ph.append(PH[0, i, 0, 0])
    phb.append(PHB[0, i, 0, 0])
for j in range(len(ph)):
    p[j] = ph[j] + phb[j]
p = np.array(p)
p /= 9.81
t = np.array(t)
t += 300
# %%

df = pd.read_csv('/home/jbenik/FirefluxII/Codes_and_Data/Data/sounding_files/modified_sounding.csv', skiprows = [1])
h = df['Height']
u = df['u']
v = df['v']
pot = df['Potential_Temp']
mix = df['mixing_ratio'] #/ 1000

# %%
fig, ax = plt.subplots(3, 2, figsize = (10, 10))
ax[0, 0].plot(u, h, color = 'red', label = 'U wind From Sounding (m/s)')
ax[0, 0].plot(u_wind, p, color = 'b', label = 'U Wind From WRF input (m/s)')
ax[0, 0].set_xlabel('U Wind (m/s)', fontsize = 10, fontweight = 'bold')
ax[0, 0].set_ylim(5, p[73])
ax[0, 0].set_ylabel('Height (m)', fontsize = 10, fontweight = 'bold')
ax[0, 0].set_title('U wind vs Height', fontsize = 10, fontweight = 'bold')

ax[0, 0].legend()

ax[0, 1].plot(v, h, color = 'red', label = 'V wind From Sounding (m/s)')
ax[0, 1].plot(v_wind, p, color = 'blue', label = 'V Wind From WRF input (m/s)')
#ax[0, 1].set_ylim(5, p[73])
ax[0, 1].set_ylabel('Height (m)', fontsize = 10, fontweight = 'bold')
ax[0, 1].set_xlabel('V Wind (m/s)', fontsize = 10, fontweight = 'bold')
ax[0, 1].set_title('V wind vs Height', fontsize = 10, fontweight = 'bold')

ax[0, 1].legend()

total_wind = np.sqrt((u**2) + (v**2))
ax[1, 0].plot(total_wind, h, color = 'black', label = 'Wind Speed From Sounding (m/s)', linestyle = '--')
ax[1, 0].plot(wind, p, color = 'green', label = 'Wind Speed From WRF input (m/s)')
#ax[1, 0].set_ylim(5, p[73])
ax[1, 0].set_ylabel('Height (m)', fontsize = 10, fontweight = 'bold')
ax[1, 0].set_xlabel('Calculated Wind Speed (m/s)', fontsize = 10, fontweight = 'bold')
ax[1, 0].set_title('Wind Speed vs Height', fontsize = 10, fontweight = 'bold')

ax[1, 0].legend()

ax[1, 1].plot(pot, h, color = '#49796b', label = 'Potential Temp From Sounding (K)')
ax[1, 1].plot(t, p, color = 'purple', label = 'Temperature From WRF input (K)')
#ax[1, 1].set_ylim(5, p[73])
ax[1, 1].set_ylabel('Height (m)', fontsize = 10, fontweight = 'bold')
ax[1, 1].set_xlabel('Temperature (K)', fontsize = 10, fontweight = 'bold')
ax[1, 1].set_title('Temperature vs Height', fontsize = 10, fontweight = 'bold')
#ax3.set_ylabel('Height (m)', fontsize = 18, fontweight = 'bold')

ax[1, 1].legend()

ax[2, 1].plot(mix, h, color = 'black', label = 'Mixing Ratio From Sounding (kg/kg)', linestyle = '--')
ax[2, 1].plot(q, p, color = 'green', label = 'Mixing Ratio From WRF input (kg/kg)')
ax[2, 1].set_xlabel('Water Vapour Mixing Ratio (kg/kg)', fontsize = 10, fontweight = 'bold')
ax[2, 1].set_ylabel('Height (m)', fontsize = 10, fontweight = 'bold')
#ax[2, 1].set_ylim(5, p[73])
ax[2, 1].set_title('Mixing Ratio vs Height', fontsize = 10, fontweight = 'bold')
ax[2, 1].legend()

plt.tight_layout()
plt.show()
# %%
'''


u = getvar(df1, 'ua')
v = getvar(df1, 'va')
w = getvar(df1, 'wa')
p = getvar(df1, 'p')

u_wind = []
v_wind = []
pres = []
wind = []
for i in range(0, 80):
    u_wind.append(u[i, 0, 0])
    v_wind.append(v[i, 0, 0])
    pres.append(p[i, 0, 0]) #i can plot versus pressure if need be too
    #wind.append(np.sqrt((u[i, 0, 0] ** 2) + (v[i, 0, 0] ** 2)))
    #t.append(temps[i])
fig, ax = plt.subplots(2, 2, figsize = (12, 12))
ax[0, 0].plot(u_wind, pres)
ax[0, 0].invert_yaxis()
#plt.plot(u_wind, pres)

fig, ax = plt.subplots(3, 1, figsize = (12, 12))
ax[0].plot()
'''
#need the coordinates of the towers, then we can compute some distance from them. 
#Find where the towers are and find the location of the lower left corner of the domain
#ask adams what the 4 corners of the mesh are, like the location of them
#then I can compute the distance from the lower left corner to the towers, then I can find 
#with those, then we can find the i j in the varibles.
# u var has height (x, y), time, to fix the time we need to know location of towers
#we need to put where the height of the towers is. don't worry about bottom top, it's already done.
#for south_north and west_east we need to know location from the lower left

#what he probably wants, just want to see what's in the wrfinput file. 
#u wind only changes vertically, not horizontally
#where heights where tower is 5.77m, 10m, 20m. 
#install wrf-python
'''
fig = plt.figure(figsize = (12, 12))
plt.plot(q, p, color = 'blue', label = 'Mixing Ratio from WRF input (k)')
plt.plot(mix, h, color = 'red', label = 'Mixing Ratio from  Sounding (k)')
plt.ylim(20, p[-1])
plt.xlabel('Mixing Ratio', fontsize = 18, fontweight = 'bold')
plt.ylabel('Height', fontsize = 18, fontweight = 'bold')
plt.title('Mixing Ratio Vs. Height', fontsize = 18, fontweight = 'bold')
plt.legend()
plt.show() '''

# %%
'''
fig = plt.figure(figsize = (15, 15))

ax1 = fig.add_subplot(321)
ax2 = fig.add_subplot(323)
ax3 = fig.add_subplot(325)
ax4 = fig.add_subplot(222)
ax5 = fig.add_subplot(224)

ax1.plot(u, h, color = 'red', label = 'U wind From Sounding (m/s)')
ax1.plot(u_wind, p, color = 'b', label = 'U Wind From WRF input (m/s)')
ax1.set_xlabel('U Wind (m/s)', fontsize = 10, fontweight = 'bold')
ax1.set_ylim(0, p[36])
ax1.set_ylabel('Height (m)', fontsize = 10, fontweight = 'bold')
ax1.set_title('U wind vs Height (200m)', fontsize = 10, fontweight = 'bold')

ax1.legend()


ax2.plot(v, h, color = 'red', label = 'V wind From Sounding (m/s)')
ax2.plot(v_wind, p, color = 'blue', label = 'V Wind From WRF input (m/s)')
ax2.set_ylim(0, p[36])
ax2.set_ylabel('Height (m)', fontsize = 10, fontweight = 'bold')
ax2.set_xlabel('V Wind (m/s)', fontsize = 10, fontweight = 'bold')
ax2.set_title('V wind vs Height (200m)', fontsize = 10, fontweight = 'bold')

ax2.legend()

total_wind = np.sqrt((u**2) + (v**2))
ax3.plot(total_wind, h, color = 'black', label = 'Wind Speed From Sounding (m/s)')
ax3.plot(wind, p, color = 'green', label = 'Wind Speed From WRF input (m/s)')
ax3.set_ylim(0, p[36])
ax3.set_ylabel('Height (m)', fontsize = 10, fontweight = 'bold')
ax3.set_xlabel('Calculated Wind Speed (m/s)', fontsize = 10, fontweight = 'bold')
ax3.set_title('Wind Speed vs Height (200m)', fontsize = 10, fontweight = 'bold')

ax3.legend()


ax4.plot(pot, h, color = '#49796b', label = 'Potential Temp From Sounding (m/s)')
ax4.plot(t, p, color = 'purple', label = 'Temperature From WRF input (K)')
ax4.set_ylim(0, p[36])
ax4.set_ylabel('Height (m)', fontsize = 10, fontweight = 'bold')
ax4.set_xlabel('Temperature (K)', fontsize = 10, fontweight = 'bold')
ax4.set_title('Temperature vs Height (200m)', fontsize = 10, fontweight = 'bold')
ax4.set_ylabel('Height (m)', fontsize = 10, fontweight = 'bold')

ax4.legend()

ax5.plot(mix, h, color = 'red', label = 'Mixing Ratio From WRF input (kg/kg)')
ax5.plot(q, p, color = 'green', label = 'Mixing Ratio From WRF input (kg/kg)')
ax5.set_xlabel('Water Vapour Mixing Ratio (kg/kg)', fontsize = 10, fontweight = 'bold')
ax5.set_ylabel('Height (m)', fontsize = 10, fontweight = 'bold')
ax5.set_ylim(0, p[36])
ax5.set_title('Mixing Ratio vs Height (200m)', fontsize = 10, fontweight = 'bold')

plt.tight_layout()
plt.show() '''
