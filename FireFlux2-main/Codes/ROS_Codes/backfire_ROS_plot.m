%This code plots the backfire rate of spread with the modified adjr0 coefficient 
x = [0.90677 0.93 0.96 0.98 0.995 0.998 0.9999 1];
%y = [0.016343623213698418 0.016343623213698418 0.016968406861031387 ...
%    0.01733921815889029 0.018134509124451997 0.017712621441470035 ...
%    0.017739540319040657 0.022056307586713404];

y = [0.015989734039574453 0.016798221788879665 0.01709021600282394 ...
    0.01720178385015444 0.01767115575900313 0.017712621441470035 ...
    0.017739540319040657 0.02106970673272338];
plot(x, y, '-o')
title('ROS Coefficients vs. Calculated ROS','fontweight','bold','fontsize',18);
xlabel('ROS Coefficients', 'fontweight','bold','fontsize',16);
ylabel('ROS (m/s)','fontweight','bold','fontsize',16);
legend('ROS');
grid on;
