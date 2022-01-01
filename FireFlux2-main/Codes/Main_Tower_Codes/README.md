# Main Tower Codes
The first and most important codes here are: Main_Tower_Plot_30min_All_Vars, Plotting_first_600seconds file, and Time_Averaged_Wind_Speed_Bar_Plot
The Main_Tower_Plot_34min_All_Vars file truncates the main file to show 4 minutes before the fire, and 30 minutes after the fire ignition. The main purpose of this plot is to see when the firefront passage occurred, and how the variables responded to the fire. There is also a 5 second rolling time average for the variables to see how the variables responded on a 5 second average. 

The Plotting_first_600seconds file truncates the original file to 10 minutes after ignition to better see how the measurements respomd to the fire passage. It's more defined than the 34min file. 

The Time_Averaged_Wind_Speed_Bar_Plot file averages u and v in certain time intervals of 4 minutes before ignition, 4min before and 4 min after (8min total), 10 minutes after the ignition, and 15 minutes after ignition. Then with these averaged wind directions and magnitudes, the wind speed was calculated for each time averaged. Since there were 3 levels the anemometers were located at, this averaging was done for all three levels. Once the wind speed was calculated for all time  averaged anemometers at the different levels, they were plotted on a bar graph to see how the different time averages change the winds.

The Calculating_Average_Wind_Profiles program averages the wind vectors over a given period of time. For example, if you want a 10 minute average, you would change the df.truncate line and change the times in there to however you wish to truncate the file and average those wind vectors. 

The File_Truncating file truncates the file and saves it as a new file to make working with the time easier since I won't need to constantly truncate the same file, instead, I will have the already cut files. 

The Time_Averaged_Variables_Bar_Plot_and_Direction file averages all the wind vecors and plots then in a bar graph with their respective height on the Main Tower. The direction of these winds was also calculated and plotted in a bar graph. 
