'''This code creates a sounding plot from the sounding data on the website along with a lot of other plots comparing temperature, theta, and other variables with 
height'''
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 28 10:19:24 2021

@author: Jeremy Benik
"""
# %% Importing libraries
import matplotlib.pyplot as plt
import pandas as pd
from metpy.plots import SkewT, Hodograph
from metpy.units import units
import metpy.calc as mpcalc
from mpl_toolkits.axes_grid1.inset_locator import inset_axes
import numpy as np
# %% Reading in the data
df = pd.read_excel('F:/Fireflux2/Excel_File_Data/testing_sounding_data.xlsx', skiprows = (0, 1, 2, 3, 4, 5, 6, 7))
# %% Defining my variables in the excel file
time = df['Time[min:sec]']
p = df['P[mB]']
p1 = p[::10] #Here I am trying to go through every third pressure point since the wind barbs were very busy
temp = df['T[C]']
dwpt = df['DewPoint[C]']
u = df['U [m/s]']
x = u[::10] #Here I am trying to go through every third U point since the wind barbs were very busy
v = df['V[m/s]']
y = v[::10] #Here I am trying to go through every third v point since the wind barbs were very busy
wind_speed = df['Wsp[m/s]']
lon = df['Lon[∞]']
lat = df['Lat[∞]']
# %% Plotting the Skew T from the excel file adam gave me
fig = plt.figure(figsize = (9, 9))
skew = SkewT(fig, rotation = 45)
skew.plot(p, temp, 'r')
skew.plot(p, dwpt, 'g')
skew.ax.set_ylim(1000, 100)
skew.ax.set_xlim(-40, 40)
skew.ax.set_xlabel('Temperature$^\circ$C', fontweight = 'bold', fontsize = 18)
skew.ax.set_ylabel('Pressure (hPa)', fontweight = 'bold', fontsize = 18)
skew.plot_dry_adiabats()
skew.plot_moist_adiabats()
skew.plot_mixing_lines()
skew.ax.set_title('FireFlux2 Skew-T From Dr. Kochanski\'s Excel Sheet', 
                  fontweight = 'bold', fontsize = 18)
ax_hod = inset_axes(skew.ax, '25%', '25%', loc=1)
h = Hodograph(ax_hod, component_range=80.)
h.add_grid(increment=20)
h.plot_colormapped(u, v, wind_speed)
skew.plot_barbs(p1[::13], x[::13], y[::13]) #the indiexing is to skip even more points since they can't be read when 
#there are too many at one time
# %% Plotting u vs height (p)  from the excel file adam gave meTHIS ONE IS VERY IMPORTANT!!!!
fig, ax = plt.subplots(figsize = (9, 9))
plt.gca().invert_yaxis()
plt.plot(u, p, 'blue', label = 'U wind')
plt.plot(v, p, 'red', label = 'V wind')
ax.set_title('U and V Winds vs. Pressure (mb)', fontsize = 18, fontweight = 'bold')
ax.set_ylabel('Pressure (mb)', fontsize = 18, fontweight = 'bold')
ax.set_xlabel('Winds (U & V)', fontsize = 18, fontweight = 'bold')
ax.legend(loc=0, prop={'size': 15})
ax.grid()
plt.show()
#plot some moisture variable. Plot something that was directly measured in the experiment
#dig into the data folder and get the soundings and verify this one looks okay. 
# %% Making a plot of the U wind vs height from adams excel file
fig, ax = plt.subplots(figsize = (9, 9))
plt.gca().invert_yaxis()
plt.plot(u, p, 'blue', label = 'U wind')
plt.title('U wind vs. Pressure (mb)', fontsize = 18, fontweight = 'bold')
plt.xlabel('Wind Speed (m/s)', fontsize = 18, fontweight = 'bold')
plt.ylabel('Pressure (mb)', fontsize = 18, fontweight = 'bold')
ax.legend(loc=2, prop={'size': 15})
plt.grid()
plt.show()
# %% v wind versus height from adams excel file
fig, ax = plt.subplots(figsize = (9, 9))
plt.gca().invert_yaxis()
plt.plot(v, p, 'red', label = 'V wind')
plt.title('V wind vs. Pressure (mb)', fontsize = 18, fontweight = 'bold')
plt.xlabel('Wind Speed m/s', fontsize = 18, fontweight = 'bold')
plt.ylabel('Pressure (mb)', fontsize = 18, fontweight = 'bold')
plt.legend(loc = 2, prop={'size': 15})
plt.grid()
plt.show()
# %% Making another plot of theta vs height to see if it's the right one
print(df.head())
theta = (df['Theta[K]'] - 273.15)
fig = plt.figure(figsize = (9, 9))
plt.gca().invert_yaxis()
plt.plot(theta, p)
plt.title('Theta (${\Theta}$) vs Pressure (mb)', fontsize = 18, fontweight = 'bold')
plt.xlabel('${\Theta}$ \u00b0C', fontsize = 18, fontweight = 'bold')
plt.ylabel('Pressure (mb)', fontsize = 18, fontweight = 'bold')
plt.legend(loc = 0, prop={'size': 15})
plt.grid()
plt.show()
# %% Making a temperature vs height graph
fig , ax = plt.subplots(figsize = (9, 9))
plt.gca().invert_yaxis()
ax.plot(temp, p, label = 'Temperature \u00b0C')
ax.set_xlabel('Temperature \u00b0C', fontsize = 18, fontweight = 'bold')
ax.set_ylabel('Pressure (mb)', fontsize = 18, fontweight = 'bold')
ax.set_title('Temperature vs. Pressure (mb)', fontsize = 18, fontweight = 'bold')
ax.legend()
ax.grid()
plt.show()
# %%
# grab the sounding from the fireflux2 folder 
# I need to get the data from the repository and plot that. the excel file, ignore that for now
#The final thing is look at raw data in the fireflux2 repository, plot them, 
#compare them to what we have in the data
#plot the big text file.
#plot something before and after the ignition. Like 15 minutes before through 30 minutes after burning
#use this to find the averagng period. So theres time before and during the burn, then try to design the avg period
#so we have a good representation of what's happening. 
'''
This can all be done with the big file. Look at paper when the ignition time was
for soundings, convert them to same coordinate system (either p or h)
need to do the timeseries at different levels (6, 10, 20) to see if they all behave similarly.''' 
#for friday, tell them what I have, what data I have, and what I'm trying to accomplish
#I will be taking over the meetings for fireflux since Dr. Kochanski is leaving
'''PUT A FEW SLIDES TOGETHER! Be ready for a formal meeting in case. '''
# %% This is using the input sounding data. Not sure if it's theta or regular temperature
# this data was taken from spartan and plotted in python. the file is input_sounding
df1 = pd.read_excel('F:/Fireflux2/Spartan_Files/input_soundings/input_sounding_csv.xlsx')
print(df1.head())
theta = (df1['Theta'] - 273.15)
fig = plt.figure(figsize = (9, 9))
plt.plot(theta, df1['Height'], label = 'Potential Temperature ${\Theta}$')
plt.title('Theta (${\Theta}$) vs Z from input_sounding', fontsize = 18, fontweight = 'bold')
plt.xlabel('Theta \u00b0C', fontsize = 18, fontweight = 'bold')
plt.ylabel('Z (m)', fontsize = 18, fontweight = 'bold')
plt.grid()
plt.legend()
plt.show()
# %%Making a new plot of theta but vs p instead of versus z
fig = plt.figure(figsize = (9, 9))
plt.gca().invert_yaxis()
plt.plot(theta, df1['Added_P[mB]'], label = 'Potential Temperature ${\Theta}$')
plt.title('Theta (${\Theta}$) vs Pressure (mb) from modified input_sounding', fontsize = 18, fontweight = 'bold')
plt.xlabel('Theta \u00b0C', fontsize = 18, fontweight = 'bold')
plt.ylabel('Pressure (mb)', fontsize = 18, fontweight = 'bold')
plt.grid()
plt.legend()
plt.show()



