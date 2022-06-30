from math import radians, tan
from ros import load_fuel_data, ros_rothermel, ros_balbi

ros_params = [
    # category, speed, phi, fmc_g, T_a
    ['f1', 1.50, 3.0, 0.03, 297.4],
    ['f2', 2.67, 3.0, 0.10, 299.7],
    ['f3', 2.67, 3.0, 0.06, 286.9],
    ['f4', 3.11, 3.0, 0.10, 288.0],
    ['f5', 3.11, 3.0, 0.12, 302.4],
    ['f6', 3.56, 3.0, 0.07, 296.9],
]

title   = 'ROS     Category   Speed     Phi    fmc_g   T_a'
rosline = '{:.4f}   {:<8}   {:4.2f}    {:4.1f}    {:4.2f}    {:5.1f}'

load_fuel_data('fuel.json')

print('Rothermel')
print(title)
for p in ros_params:
    (category, speed, phi, fmc_g, T_a) = p[:]
    ros = ros_rothermel(category, speed, tan(radians(phi)), fmc_g)
    print(rosline.format(ros, category, speed, phi, fmc_g, T_a))


# %%
title   = 'ROS     Category   Speed     Phi    fmc_g   T_a'
rosline = '{:.4f}   {:<8}   {:4.2f}    {:4.1f}    {:4.2f}    {:5.1f}'

print()
print('Balbi')
print(title)
for p in ros_params:
    (category, speed, phi, fmc_g, T_a) = p[:]
    ros = ros_balbi(category, speed, tan(radians(phi)), fmc_g, T_a)
    print(rosline.format(ros, category, speed, phi, fmc_g, T_a))
