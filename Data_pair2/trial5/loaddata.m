clear
close all

action_1 = loadaction("action_h1.csv");
action_2 = loadaction("action_h2.csv");
state = loadstate("state.csv");

%plot traj
figure
plot(state(:,1),state(:,2))
 
%plot action
figure
plot(action_1)
hold on
plot(action_2)