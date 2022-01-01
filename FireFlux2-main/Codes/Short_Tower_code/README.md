# Short tower code
This code iterates through all the small tower files (there are three of them for the East towe, South tower, and West tower) and creates plots of all the variables
recorded on those towers. In this case just u, v, w, and t. So these plots show how those change with time for 30 minutes after the fire was first ignited. 
The code then averages u, v, and w in different intervals (4 min before the fire, 4min before and 4 minutes after (8min total), 10 min after fire ignition, and 15
minutes after fire ignition), then calculates the wind speed and plots the wind speeds.
This was done to see what averaging would be best to use to add wind values in the input_sounding file.
