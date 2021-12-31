# -*- coding: utf-8 -*-
"""
Created on Mon Dec 20 15:44:32 2021

@author: Jeremy Benik
"""
#F:/Fireflux2/Website_Docs/Clipped_to_30_minutes_Proc_FF2_10HzMTdespiked_rotated.csv
# %% Importing necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
#import datetime
#from metpy.plots import SkewT, Hodograph
from metpy.units import units
import metpy.calc as mpcalc
#from mpl_toolkits.axes_grid1.inset_locator import inset_axes
import metpy
import statistics as st
# %% Reading in the data
#df = pd.read_csv('F:/Fireflux2/Website_Docs/Proc_FF2_10HzMTdespiked_rotated.csv', parse_dates=['TIMESTAMP'], skiprows = (0, 2, 3))
df = pd.read_csv('F:/Fireflux2/Website_Docs/other_Clipped_to_35_minutes_Proc_FF2_10HzMTdespiked_rotated.csv')
#write a script to play with this csv so I can work with other ones if needed. such as5 seconds and 10 seconds. 
# %% Assigning variables
time = df['times']
ux20 = df['Ux_20m']
uy20 = df['Uy_20m']
uz20 = df['Uz_20m']
tz20 = df['Ts_20m']
ux10 = df['Ux_10m']
uy10 = df['Uy_10m']
uz10 = df['Uz_10m']
ts10 = df['Ts_10m']
ux6 = df['Ux_6m']
uy6 = df['Uy_6m']
uz6 = df['Uz_6m']
ts6 = df['Ts_6m']
# %% Creating my function to average the data in 500 intervals with time
n = 500
x = []
def loops(p, x): # u is the wind, x is the list we are using
    x = []
    for i in range(0, (int(len(time) / n))):
        x.append(st.mean(p[i:n*(i + 1)]))
    return x
# %% These graphs are not averaged over any time, they are all variables plotted over the 30 minutes of data
fig, ax = plt.subplots(4, 3, figsize = (20, 10))
plt.title('Plots of variables without an average')
ax[0, 0].plot(range(len(time)), ux20, 'r', label = 'ux20m winds')
ax[0, 0].set_title('ux20 winds vs time(s)', fontsize = 18, fontweight = 'bold')
ax[0, 0].set_ylabel('Speed (m/s)', fontsize = 18, fontweight = 'bold')
ax[0, 0].set_xlabel('Time (seconds)', fontsize = 18, fontweight = 'bold')
ax[0, 0].legend(prop={'size': 10})
ax[1, 0].plot(range(len(time)), uy20, 'blue', label = 'uy20m winds')
ax[1, 0].legend(prop={'size': 10})
ax[1, 0].set_xlabel('Time (seconds)', fontsize = 18, fontweight = 'bold')
ax[1, 0].set_ylabel('Speed (m/s)', fontsize = 18, fontweight = 'bold')
ax[1, 0].set_title('uy20 winds vs time (s)', fontsize = 18, fontweight = 'bold')
ax[1, 0].set_xlim(0, len(time))
ax[0, 0].set_xlim(0, len(time))
ax[2, 0].plot(range(len(time)), uz20, 'purple', label = 'uz20m winds')
ax[2, 0].set_title('uz20 winds vs time(s)', fontsize = 18, fontweight = 'bold')
ax[2, 0].set_ylabel('Speed (m/s)', fontsize = 18, fontweight = 'bold')
ax[2, 0].set_xlabel('Time (seconds)', fontsize = 18, fontweight = 'bold')
ax[2, 0].legend(prop={'size': 10})
ax[2, 0].set_xlim(0, len(time))
ax[3, 0].plot(range(len(time)), tz20, 'green', label = 'Temperature$^\circ$C 20m')
ax[3, 0].set_title('tz20 winds vs time(s)', fontsize = 18, fontweight = 'bold')
ax[3, 0].set_ylabel('Temperature C', fontsize = 18, fontweight = 'bold')
ax[3, 0].set_xlabel('Time (seconds)', fontsize = 18, fontweight = 'bold')
ax[3, 0].legend(prop={'size': 10})
ax[3, 0].set_xlim(0, len(time))
ax[0, 1].plot(range(len(time)), ux10, 'red', label = 'ux10 winds')
ax[0, 1].set_title('ux10 winds vs time(s)', fontsize = 18, fontweight = 'bold')
ax[0, 1].set_ylabel('Speed (m/s)', fontsize = 18, fontweight = 'bold')
ax[0, 1].set_xlabel('Time (seconds)', fontsize = 18, fontweight = 'bold')
ax[0, 1].legend(prop={'size': 10})
ax[0, 1].set_xlim(0, len(time))
ax[1, 1].plot(range(len(time)), uy10, 'blue', label = 'uy10m winds')
ax[1, 1].set_title('uy10 winds vs time(s)', fontsize = 18, fontweight = 'bold')
ax[1, 1].set_ylabel('Speed (m/s)', fontsize = 18, fontweight = 'bold')
ax[1, 1].set_xlabel('Time (seconds)', fontsize = 18, fontweight = 'bold')
ax[1, 1].legend(prop={'size': 10})
ax[1, 1].set_xlim(0, len(time))
ax[2, 1].plot(range(len(time)), uz10, 'purple', label = 'uz10m winds')
ax[2, 1].set_title('uz10 winds vs time(s)', fontsize = 18, fontweight = 'bold')
ax[2, 1].set_ylabel('Speed (m/s)', fontsize = 18, fontweight = 'bold')
ax[2, 1].set_xlabel('Time (seconds)', fontsize = 18, fontweight = 'bold')
ax[2, 1].legend(prop={'size': 10})
ax[2, 1].set_xlim(0, len(time))
ax[3, 1].plot(range(len(time)), ts10, 'green', label = 'Temperature$^\circ$C 10m')
ax[3, 1].set_title('ts10 winds vs time(s)', fontsize = 18, fontweight = 'bold')
ax[3, 1].set_ylabel('Temperature C', fontsize = 18, fontweight = 'bold')
ax[3, 1].set_xlabel('Time (seconds)', fontsize = 18, fontweight = 'bold')
ax[3, 1].legend(prop={'size': 10})
ax[3, 1].set_xlim(0, len(time))
ax[0, 2].plot(range(len(time)), ux6, 'red', label = 'ux6m winds')
ax[0, 2].set_title('ux6 winds vs time(s)', fontsize = 18, fontweight = 'bold')
ax[0, 2].set_ylabel('Speed (m/s)', fontsize = 18, fontweight = 'bold')
ax[0, 2].set_xlabel('Time (seconds)', fontsize = 18, fontweight = 'bold')
ax[0, 2].legend(prop={'size': 10})
ax[0, 2].set_xlim(0, len(time))
ax[1, 2].plot(range(len(time)), uy6, 'blue', label = 'uy6m winds')
ax[1, 2].set_title('uy6 winds vs time(s)', fontsize = 18, fontweight = 'bold')
ax[1, 2].set_ylabel('Speed (m/s)', fontsize = 18, fontweight = 'bold')
ax[1, 2].set_xlabel('Time (seconds)', fontsize = 18, fontweight = 'bold')
ax[1, 2].legend(prop={'size': 10})
ax[1, 2].set_xlim(0, len(time))
ax[2, 2].plot(range(len(time)), uz6, 'purple', label = 'uz6m winds')
ax[2, 2].set_title('uz6 winds vs time(s)', fontsize = 18, fontweight = 'bold')
ax[2, 2].set_ylabel('Speed (m/s)', fontsize = 18, fontweight = 'bold')
ax[2, 2].set_xlabel('Time (seconds)', fontsize = 18, fontweight = 'bold')
ax[2, 2].legend(prop={'size': 10})
ax[2, 2].set_xlim(0, len(time))
ax[3, 2].plot(range(len(time)), ts6, 'green', label = 'Temperature$^\circ$C 6m')
ax[3, 2].set_title('ts6 winds vs time(s)', fontsize = 18, fontweight = 'bold')
ax[3, 2].set_ylabel('Temperature C', fontsize = 18, fontweight = 'bold')
ax[3, 2].set_xlabel('Time (seconds)', fontsize = 18, fontweight = 'bold')
ax[3, 2].legend(prop={'size': 10})
ax[3, 2].set_xlim(0, len(time))
ax[0, 0].grid()
ax[1, 0].grid()
ax[2, 0].grid()
ax[3, 0].grid()
ax[0, 1].grid()
ax[1, 1].grid()
ax[2, 1].grid()
ax[3, 1].grid()
ax[0, 2].grid()
ax[1, 2].grid()
ax[2, 2].grid()
ax[3, 2].grid()
plt.tight_layout()
plt.show()
# %% Making a plots
time2 = np.arange(0, len(time[::n]) - 1)
fig, ax = plt.subplots(4, 3, figsize = (20, 10))
ax[0, 0].plot(time2, loops(ux20, x) , 'r', label = 'ux20m winds')
ax[0, 0].set_title('ux20 winds vs time(s)', fontsize = 18, fontweight = 'bold')
ax[0, 0].set_ylabel('Speed (m/s)', fontsize = 18, fontweight = 'bold')
ax[0, 0].set_xlabel('Time (seconds)', fontsize = 18, fontweight = 'bold')
ax[0, 0].legend(prop={'size': 10})
ax[1, 0].plot(time2, loops(uy20, x), 'blue', label = 'uy20m winds')
ax[1, 0].legend(prop={'size': 10})
ax[1, 0].set_xlabel('Time (seconds)', fontsize = 18, fontweight = 'bold')
ax[1, 0].set_ylabel('Speed (m/s)', fontsize = 18, fontweight = 'bold')
ax[1, 0].set_title('uy20 winds vs time (s)', fontsize = 18, fontweight = 'bold')
ax[1, 0].set_xlim(0, len(time[::n]))
ax[0, 0].set_xlim(0, len(time[::n]))
ax[2, 0].plot(time2, loops(uz20, x), 'purple', label = 'uz20m winds')
ax[2, 0].set_title('uz20 winds vs time(s)', fontsize = 18, fontweight = 'bold')
ax[2, 0].set_ylabel('Speed (m/s)', fontsize = 18, fontweight = 'bold')
ax[2, 0].set_xlabel('Time (seconds)', fontsize = 18, fontweight = 'bold')
ax[2, 0].legend(prop={'size': 10})
ax[2, 0].set_xlim(0, len(time[::n]))
ax[3, 0].plot(time2, loops(tz20, x), 'green', label = 'Temperature$^\circ$C 20m')
ax[3, 0].set_title('tz20 winds vs time(s)', fontsize = 18, fontweight = 'bold')
ax[3, 0].set_ylabel('Temperature C', fontsize = 18, fontweight = 'bold')
ax[3, 0].set_xlabel('Time (seconds)', fontsize = 18, fontweight = 'bold')
ax[3, 0].legend(prop={'size': 10})
ax[3, 0].set_xlim(0, len(time[::n]))
ax[0, 1].plot(time2, loops(ux10, x), 'red', label = 'ux10 winds')
ax[0, 1].set_title('ux10 winds vs time(s)', fontsize = 18, fontweight = 'bold')
ax[0, 1].set_ylabel('Speed (m/s)', fontsize = 18, fontweight = 'bold')
ax[0, 1].set_xlabel('Time (seconds)', fontsize = 18, fontweight = 'bold')
ax[0, 1].legend(prop={'size': 10})
ax[0, 1].set_xlim(0, len(time[::n]))
ax[1, 1].plot(time2, loops(uy10, x), 'blue', label = 'uy10m winds')
ax[1, 1].set_title('uy10 winds vs time(s)', fontsize = 18, fontweight = 'bold')
ax[1, 1].set_ylabel('Speed (m/s)', fontsize = 18, fontweight = 'bold')
ax[1, 1].set_xlabel('Time (seconds)', fontsize = 18, fontweight = 'bold')
ax[1, 1].legend(prop={'size': 10})
ax[1, 1].set_xlim(0, len(time[::n]))
ax[2, 1].plot(time2, loops(uz10, x), 'purple', label = 'uz10m winds')
ax[2, 1].set_title('uz10 winds vs time(s)', fontsize = 18, fontweight = 'bold')
ax[2, 1].set_ylabel('Speed (m/s)', fontsize = 18, fontweight = 'bold')
ax[2, 1].set_xlabel('Time (seconds)', fontsize = 18, fontweight = 'bold')
ax[2, 1].legend(prop={'size': 10})
ax[2, 1].set_xlim(0, len(time[::n]))
ax[3, 1].plot(time2, loops(ts10, x), 'green', label = 'Temperature$^\circ$C 10m')
ax[3, 1].set_title('ts10 winds vs time(s)', fontsize = 18, fontweight = 'bold')
ax[3, 1].set_ylabel('Temperature C', fontsize = 18, fontweight = 'bold')
ax[3, 1].set_xlabel('Time (seconds)', fontsize = 18, fontweight = 'bold')
ax[3, 1].legend(prop={'size': 10})
ax[3, 1].set_xlim(0, len(time[::n]))
ax[0, 2].plot(time2, loops(ux6, x), 'red', label = 'ux6m winds')
ax[0, 2].set_title('ux6 winds vs time(s)', fontsize = 18, fontweight = 'bold')
ax[0, 2].set_ylabel('Speed (m/s)', fontsize = 18, fontweight = 'bold')
ax[0, 2].set_xlabel('Time (seconds)', fontsize = 18, fontweight = 'bold')
ax[0, 2].legend(prop={'size': 10})
ax[0, 2].set_xlim(0, len(time[::n]))
ax[1, 2].plot(time2, loops(uy6, x), 'blue', label = 'uy6m winds')
ax[1, 2].set_title('uy6 winds vs time(s)', fontsize = 18, fontweight = 'bold')
ax[1, 2].set_ylabel('Speed (m/s)', fontsize = 18, fontweight = 'bold')
ax[1, 2].set_xlabel('Time (seconds)', fontsize = 18, fontweight = 'bold')
ax[1, 2].legend(prop={'size': 10})
ax[1, 2].set_xlim(0, len(time[::n]))
ax[2, 2].plot(time2, loops(uz6, x), 'purple', label = 'uz6m winds')
ax[2, 2].set_title('uz6 winds vs time(s)', fontsize = 18, fontweight = 'bold')
ax[2, 2].set_ylabel('Speed (m/s)', fontsize = 18, fontweight = 'bold')
ax[2, 2].set_xlabel('Time (seconds)', fontsize = 18, fontweight = 'bold')
ax[2, 2].legend(prop={'size': 10})
ax[2, 2].set_xlim(0, len(time[::n]))
ax[3, 2].plot(time2, loops(ts6, x), 'green', label = 'Temperature$^\circ$C 6m')
ax[3, 2].set_title('ts6 winds vs time(s)', fontsize = 18, fontweight = 'bold')
ax[3, 2].set_ylabel('Temperature C', fontsize = 18, fontweight = 'bold')
ax[3, 2].set_xlabel('Time (seconds)', fontsize = 18, fontweight = 'bold')
ax[3, 2].legend(prop={'size': 10})
ax[3, 2].set_xlim(0, len(time[::n]))
ax[0, 0].grid()
ax[1, 0].grid()
ax[2, 0].grid()
ax[3, 0].grid()
ax[0, 1].grid()
ax[1, 1].grid()
ax[2, 1].grid()
ax[3, 1].grid()
ax[0, 2].grid()
ax[1, 2].grid()
ax[2, 2].grid()
ax[3, 2].grid()
plt.tight_layout()
plt.show()
# %% Making the plot
'''
fig, ax = plt.subplots(figsize = (15, 10))
u = ux20.values * units('m/s')
v = uy20.values * units('m/s')

loops(-v, x)
uv = np.sqrt(u**2 + v**2)
direction = metpy.calc.wind_direction(u, v, convention='from')
#ax.quiver(time2, 20, -v, u, uv)
ax.quiver(range(len(time)), 20, loops(-v, x), loops(u, x), loops(uv, x))
ax.set_ylim([0, 25])
u = ux10.values * units('m/s')
v = uy10.values * units('m/s')
uv = np.sqrt(u**2 + v**2)
#quiver wants u and v
#other notes, put library.__version__ to see the version of it. I'm using matplotlib 3.3.4
ax.quiver(range(len(time)), 10, loops(-v, x), loops(u, x), loops(uv, x)) #change the 0 around to plot them at different levels
u = ux6.values * units('m/s')
v = uy6.values * units('m/s')
uv = np.sqrt(u**2 + v**2)
ax.quiver(range(len(time)), 6, loops(-v, x), loops(u, x), loops(uv, x))
# there's gonna be a lot of arrows. Use a subset. Maybe every minute to see what's going on. I could even do an average across some time period.
ax.set_xlabel('Time', fontsize = 18, fontweight = 'bold')
ax.set_ylabel('Height (m)', fontsize = 18, fontweight = 'bold')
ax.set_title('Wind Vectors From Main Tower At 20 Meters', fontsize = 22, fontweight = 'bold' )
# up against tower, down going down tower, then direction is the wind. all the time the wind was blwoing against the tower.
plt.show() '''
