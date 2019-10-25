clear
%%
Ts = 0.2;
% load('tf2.mat')
% nn = tf2.Numerator;
% aa = tf2.Denominator(1);
% bb = tf2.Denominator(2);
% cc = tf2.Denominator(3);
M = 1; % thetadd
b = 3; % thetad
k = 1;% theta
%state model
A=[0 1;-k/M -b/M];
B=[0;1/M];
C = [1 0];
D = 0;
ss1 = ss(A,B,C,D);
ssd = c2d(ss1,Ts,'zoh')
