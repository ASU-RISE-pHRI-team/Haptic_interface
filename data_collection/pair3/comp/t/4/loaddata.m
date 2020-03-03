clear

action_1 = loadaction("new_action_h1.csv");
action_2 = loadaction("new_action_h2.csv");
state = loadstate("state.csv");

%plot traj
figure
plot(state(:,1),state(:,2))
hold on
plot(0,2,'b*')
plot(0,0,'r*')
hold off
xlim([-1.2 1.2])
ylim([-2 2])
 
%plot action
figure
plot(action_1)
hold on
plot(action_2)
hold off
ylim([-2.5 2.5])

%plot angular displacement
figure

[L1, L2] = size(state);
y1 = -0.785*ones(1,L1);
y2 = 0*ones(1,L1);
plot(state(:,5))
hold on
plot(y1,'r')
plot(y2,'b')
hold off