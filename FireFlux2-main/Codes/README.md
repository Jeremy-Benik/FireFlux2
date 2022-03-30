# This directory contains codes for verification of the FireFlux2 experiment

**Anemometer_Codes**

This directory contains a code that goes through all the anemometer files and creates a plot of the data from 30 minutes before the ignition and 30 minutes after the ignition. There is no averaging done in these plots.

**Combined_Tower_Codes**

This directory contains codes that plot data from all the towers in the field. The tower data is compared to the wrfoutput file from the ideal experiment to see how accurately the fire spread was calculated in the model compared to the observations. there are more details about the codes in the README.md document there.

**Main_Tower_Codes**

This directory contains codes that take the data from the main tower in the burn, and plot all the variables collected during the birn to see how they changed with the fire front passage

**ROS_Codes**

This directory contains MATLAB codes that were written by Dr. Adam Kochanski. These codes are used to calculate the fire rate of spread given certain fuel conditions and other parameters such as slope, wind speed, and fuel moisture

**Short_Tower_code**

This directory has codes that plot the data from the short towers from the burn plot. There is also a code that compares the short tower data to the wrfout file to see how accurately the model predicted the fire spread. This code should jsut be used for the real data however and not the ideal data.

**Sounding_Scripts**
This directory contains codes that plot the sounding file from the experiment.

**wrf_codes**

This directory contains codes that plot and manipulate wrffdda files, plots values from wrfout files, finds the rate of spread compared to towers, and plots data from the wrfinput files. More information can be found in the README.md there

