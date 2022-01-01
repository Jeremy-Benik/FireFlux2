# Main Tower Codes
The first and most important codes here are: Main_Tower_Plot_30min_All_Vars, Plotting_first_600seconds file, and Time_Averaged_Wind_Speed_Bar_Plot
Main_Tower_Plot_34min_All_Vars truncates the main file to show 4 minutes before the fire, and 30 minutes after the fire ignition.
The main purpose of this plot is to see when the firefront passage occurred, and how the variables responded to the fire. 

The Plotting_first_600seconds file truncates the original file to 10 minutes after ignition to better see how the measurements
respomd to the fire passage. It's more defined than the 34min file. 

The Time_Averaged_Wind_Speed_Bar_Plot file averages u and v in certain time intervals of 4 minutes before ignition, 4min before and 4 min after (8min total),
10 minutes after the ignition, and 15 minutes after ignition. Then with these averaged wind directions and magnitudes, the wind speed was calculated for each time
averaged. Since there were 3 levels the anemometers were located at, this averaging was done for all three levels. Once the wind speed was calculated for all time 
averaged anemometers at the different levels, they were plotted on a bar graph to see how the different time averages change the winds.


the 35_Minute_Main_Tower_Data_Plot_All_Variables file uses a file that has been truncated to 35 minutes and it plots all
variables. The variables in the data set were u, v, w, and T as 6m, 10m, and 20m. 
