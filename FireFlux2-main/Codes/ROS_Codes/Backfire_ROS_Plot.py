# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 16:59:50 2022

@author: Jeremy Benik
"""
# %% Importing necessary libraries
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# %% Inputting the x and y data
x = [0.9067704, 0.93, 0.96, 0.98, 1]
y = [0.016343623213698418, 0.016343623213698418, 0.016968406861031387, 0.01733921815889029, 0.022056307586713404]

fig = plt.figure(figsize = (12, 12))
plt.plot(x, y, label = 'Rate of Spread Adjustment vs. Rate of Spread', color = 'red', marker = 'o')
plt.title('Backfire ROS vs. Adjustment Factor', fontsize = 18, fontweight = 'bold')
plt.xlabel('adjr0 Coefficient', fontsize = 12, fontweight = 'bold')
plt.ylabel('Backfire ROS (m/s)', fontsize = 12, fontweight = 'bold')
plt.xlim(x[0], 1)
plt.grid()
plt.show()