function err=check_ros(fuel)
% err=check_ros(fuel)
% check relative error between fortran and matlab
% example: fuels; check_ros(fuel) should return of order 1e-5
nfuels=length(fuel);
for k=1:nfuels
     switch fuel(k).ibeh 
    case 1
        spread_model='Rothermel';
        fire_ros=@ros_rothermel
    case 2
        spread_model='Balbi';
        fire_ros=@ros_balbi
    otherwise
        error(sprintf('spread model %g not known',fuel(k).ibeh))
    end

    nwinds=length(fuel(k).wind);
    for j=1:nwinds
        speed=fuel(k).wind(j);
        ros=fire_ros(fuel(k),speed*fuel(k).windrf,0,fuel(k).fuelmc_g);
        err(k,j,1)=(fuel(k).ros_wind(j)-ros)/(ros+eps);
    end
    nslopes=length(fuel(k).slope);
    for j=1:nslopes
        tanphi=fuel(k).slope(j);
        ros=fire_ros(fuel(k),0,tanphi,fuel(k).fuelmc_g);
        err(k,j,2)=(fuel(k).ros_slope(j)-ros)/(ros+eps);
    end
    nfmc_g=length(fuel(k).fmc_g);
    for j=1:nfmc_g
        fmc_g = fuel(k).fmc_g(j);
        ros=fire_ros(fuel(k),0,0,fmc_g);
        err(k,j,3)=(fuel(k).ros_fmc_g(j)-ros)/(ros+eps);
    end
end
err=big(err);