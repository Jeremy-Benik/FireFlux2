# Short tower code
The Short_Tower_Code.py code iterates through all the small tower files (there are three of them for the East towe, South tower, and West tower) and creates plots of all the variables recorded on those towers. In this case just u, v, w, and t. So these plots show how those change with time for 30 minutes after the fire was first ignited. The code then averages u, v, and w in different intervals (4 min before the fire, 4min before and 4 minutes after (8min total), 10 min after fire ignition, and 15 minutes after fire ignition), then calculates the wind speed and plots the wind speeds. This was done to see what averaging would be best to use to add wind values in the input_sounding file.

The Short_towers_with_wrfout.py code plots all variables from the short towers and compares them to the wrfout file to see how the wrf model performed against the observed data.

The Short_towers_with_wrfout_real.py code plots the variables from a real wrfout case. This code is not needed for the ideal case and would not work for it. It should really only be used for the real cases.

The short_tower_temp_wrfout_comparison.py code plots the temperatures from the short towers and compares them to the wrfout file to see how the rate of spread differs from observed data to the model data. 

The short_tower_wind_wrfout_comparison.py code plots the winds from the short towers and compares them to the wrfout file to see how the rate of spread differs from observed data to the model data. 
