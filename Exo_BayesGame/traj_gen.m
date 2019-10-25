clear 
load('AvgKneeGait.mat')

N = 10;
Traj = [];
for ii = 1:N
    Traj = [Traj;LkneeAvg*pi/180];
end
traj = resample(Traj,25,100);
v = diff(Traj)*25;
a = diff(v);
vel = resample(v,25,100);
u0 = resample(a,25,100);

