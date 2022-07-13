# -*- coding: utf-8 -*-
"""
Created on Sun Nov  7 17:59:02 2021

@author: Jeremy Benik
'''"""
''' This program plots the temperature versus height
for input_sounding in the fireflux2 case study'''

import matplotlib.pyplot as plt
import pandas as pd
from metpy.plots import SkewT, Hodograph
from metpy.units import units
import metpy.calc as mpcalc
from mpl_toolkits.axes_grid1.inset_locator import inset_axes
import numpy as np

df1 = pd.read_csv('input_sounding_csv.csv')
print(df1.head())
theta = (df1['Theta'] - 273.15) #converting the temperature to celcius
fig = plt.figure(figsize = (9, 9)) #creating the figure
plt.plot(theta, df1['Height'], ) #plotting theta vs height
plt.title('Theta vs Z from input_sounding', fontsize = 18, fontweight = 'bold') #creating a title
plt.xlabel('Theta', fontsize = 18, fontweight = 'bold') #creating a x label
plt.ylabel('Z', fontsize = 18, fontweight = 'bold') #creating a y label
plt.grid() #adding grid lines to the graph
plt.show() #showing the graph