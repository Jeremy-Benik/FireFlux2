# -*- coding: utf-8 -*-
"""
Created on Thu Nov 11 12:40:05 2021

@author: Rubix
"""
import matplotlib.pyplot as plt
import pandas as pd
from metpy.plots import SkewT, Hodograph
from metpy.units import units
import metpy.calc as mpcalc
from mpl_toolkits.axes_grid1.inset_locator import inset_axes
import numpy as np

df = pd.read_csv('F:/Fireflux2/Website_Docs/Soundings/FF2_Sounding.csv', skiprows = (0, 1, 2, 3, 4, 5, 6, 7, 8))
#df = df.dropna(subset=('T[C]', 'DewPoint[C]', 'Wdir[Grd]', 'Wsp[m/s]', 'Time[min:sec]', 'P[mB]',
                       #), how='all').reset_index(drop=True)
print(df)
# %% Defining my variables
time = df['Time[min:sec]']
#p = df['P[mB]']
p = df['P[mB]'].values * units.hPa
#temp = df['T[C]']
T = df['T[C]'].values * units.degC
#dwpt = df['DewPoint[C]']
Td = df['DewPoint[C]'].values * units.degC
#wind_speed = df['Wsp[m/s]']
#float(df['Wsp[m/s]'])
wind_speed = df['Wsp[m/s]'].values * units.knots
#float(wind_speed)
wind_dir = df['Wdir[Grd]'].values * units.degrees
print(wind_speed, wind_dir)
# %%
u, v = mpcalc.wind_components(wind_speed, wind_dir)
# wind_dir = df['Wdir[Grd]']
lon = df['Lon[°]']
lat = df['Lat[°]']
z = df['Altitude[m]']
# np.isnan(dwpt)
# np.isnan(p)
# np.isnan(temp)
# np.isnan(wind_speed)
# np.isnan(lon)
# np.isnan(lat)
# %% Plotting a skewt from the FF2_Sounding data
'''Note, for this one I could only plot t vs pressure since a dewpoint wasn't given in the data'''
fig = plt.figure(figsize = (9, 9))
skew = SkewT(fig, rotation = 45)
skew.plot(p, T, 'r')
skew.plot(p, Td, 'g')
skew.ax.set_ylim(1000, 100)
skew.ax.set_xlim(-40, 40)
skew.ax.set_xlabel('Temperature$^\circ$C', fontweight = 'bold', fontsize = 18)
skew.ax.set_ylabel('Pressure (hPa)', fontweight = 'bold', fontsize = 18)
skew.plot_dry_adiabats()
skew.plot_moist_adiabats()
skew.plot_mixing_lines()
skew.ax.set_title('FireFlux2 Skew-T', 
                  fontweight = 'bold', fontsize = 18)

ax_hod = inset_axes(skew.ax, '25%', '25%', loc=1)
h = Hodograph(ax_hod, component_range=80.)
h.add_grid(increment=20)
h.plot_colormapped(u, v, wind_speed)
skew.plot_barbs(p[::130], u[::130], v[::130])
# %% plotting it versus height since height was also given. Not going to make this a skewt since that's difficult
fig = plt.figure(figsize = (9, 9))
plt.plot(T, z, 'r', label = 'Temperature \u00b0C')
plt.xlabel('Temperature \u00b0C', fontweight = 'bold', fontsize = 18)
plt.ylabel('Altitude (m)', fontweight = 'bold', fontsize = 18)
plt.legend()
plt.tight_layout()
plt.show()
# %% Plotting the wind speeds
fig, ax = plt.subplots(nrows = 1, ncols = 2)
ax[0].plot(wind_speed, z)
ax[0].set_ylim(0, 40)
ax[0].set_title('Wind Speed first 40 Meters', fontweight = 'bold', fontsize = 12)
ax[0].set_xlabel('Wind Speed (m/s)', fontweight = 'bold', fontsize = 9)
ax[0].set_ylabel('Height (m)', fontweight = 'bold', fontsize = 9)
ax[0].grid()
ax[1].plot(wind_speed, z)
ax[1].set_title('Wind Speed vs. Height', fontweight = 'bold', fontsize = 12)
ax[1].set_xlabel('Wind Speed (m/s)', fontweight = 'bold', fontsize = 9)
ax[1].set_ylabel('Height (m)', fontweight = 'bold', fontsize = 9)
ax[1].grid()
plt.tight_layout()
plt.show()
# %%
plt.gca().invert_yaxis()
plt.plot(u, p)
plt.plot(v, p)
plt.show()
# %% Trying to write to a new file
df = 
f = open("new_input_Sounding_File.csv", "w")
f.write(p, )
