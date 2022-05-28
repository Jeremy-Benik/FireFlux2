# WRF Codes (input and output files)
Most of the files necessary for these codes can be found on the ember or spartan cluster at: /home/jbenik/FireFlux2/Codes_and_Data/Data/wrf_files. I try to keep the two servers the same in terms of what files I have on there. 

wrfinput_code.py: this code creates a plot of the variables in the wrfinput file. The file used in the code was from my idealized run. 

wrfout_vector_plot.py creates a wind vector plot at certain levels. The winds are pointed towards the tower if looking at it that way. This code takes in a wrfout file and plots U and V at various height levels. This code will have to be put into a server with a wrfout file since the files are too big to fit into the data file in this github. 

tower_data_compared_to_wrfout.py gets the data from the wrfout file and from the towers, and compares the variables from the towers and from the wrfout file to see how they compare. This can help verify the ROS of the model output as well as seee the differences between the model output and what the towers recorded. This code plots both the main tower data and short tower data. As a quick note, this code will take about an hour to run on the ember cluster. This code also needs a wrfinput file from the real case. This is needed as a way to find the location of the towers on the atmospheric grid and to speficy the projection of the map. The coordinates used to find the towers were from the google earth document. I looked at the towers and got their location from google earth and put those values in. 

ROS_finder.py is still a work in progress, however the goal of this program is to find when the fire reaches the grid points for the towers and the time it does that. This code uses a wrfin from the real case to find the towers and the second domain wrfin file from the real case as an attempt to use the fire mesh. 

Backfire_ROS_Calculation.py calculates the backfire rate of spread. It does this in 3 different ways. The first way is it uses the ignition point, then goes up 4 meters (8 grid cells) and left 4 meters (8 grid cells), then calculates the backfire ROS for that. Then it calcualtes the backfire ROS based on the house since that is what was used in the video where I found where the fire area is parallel to the roof of the building, then when it gets to the other side of the building and caluclates ROS that way. Lastly, I used the ignition point, and then I went to the last timestep, found where the last cell with fire_area is, then calculates the distance between them, and the time it took for the fire to reach that cell. 


FF2_Backfire_ROS_Calculator.py calculates the backfire rate of spread from the ignition point (this was taken from the namelist.input file), and goes to the last point I can manually find on ncview of the fire area. For picking a point, I pick a point that isn't fully covered in fire (fire_area < 1), and use that point. ncview gives the grid point so I can just use that for the inputs
