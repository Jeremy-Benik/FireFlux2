# wrffdda codes
changing_wrffdda_d01.py and changing_wrffdda_d02.py: This code takes a wrfinput file from both a real case and an ideal case, and it takes in wrffdda files from the real case. With those code, it interpolates the variables from the wrffdda file to the heights in the real wrfinput since there is no height coordinate in the wrffdda files. With this, I then interpolate the data to the levels in the wrfinput from the ideal case, and I change the data in the wrffdda file to match that of the wrfinput file. I set both the old and new values, and both timesteps to the values in the wrfinput file (a file with only one timestep). The d01 case interpolates and writes data for the first domain in the real case, and the d02 code does it for the second domain. I had to make a new wrfinput file by running ideal.exe on the original namelist.input, then I changed the grid size to the size of the d02 real case, and I changed the resolution to 5 (dx, dy). In order for this to run I also modified the fire_read_lu and set that equal to false (fire_read_lu=.false.). Lastly, I set fire_fuel_read=0 from it's original value of 2

wrffdda_code.py: this code will create a plot of the wrffdda variables versus the PH variable. This code also plots the data compared to the wrfinput file from an idealized run, and the input_sounding file used to make the ideal wrfinput file. Those lines have been commented out but can be easily uncommented and run to see how the files are different.

wrffdda_time_shifted_plot.py: This code time shifts the old and new variables to see how those two variables compare to each other. What I found is the new variables are time shifted by one time step. Meaning the values are identical, but off by one timestep.