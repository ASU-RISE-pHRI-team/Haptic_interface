clear

x=[];F=[];
x(:,1)=[0;4;0;0;0;0];
v(1)=0;
% agent 1: teacher; agent 2: student
sys=loadsys(2);
N=sys.N;
theta=sys.theta;
M = 0.2; % mass of the object
a = 0.3; % width of the object
b = 2; %lenth of the object
I = 0.067;
l = b/2;
T = 0.1;
cfr1 = 0.2;
cfr2 = 0.067;
% 
% BPB=sys.B'*sys.P*sys.B;
% H_1_list=[];
% for i=1:sum(sys.nu)
% H_1_list=[H_1_list;BPB(i,i)];
% end
% H_2=BPB-diag(H_1_list);
% Acl=eye(sys.nx)-sys.B*inv(H_2)*sys.B'*sys.P;
% eig(eye(N*3)-sys.B*inv(H_2)*sys.B'*sys.P)

%%
thetahat=[];
thetahat(:,1)=[1e-3;1e-3];
thetahat1=[];
thetahat1(:,1)=[1e-3;1e-3];
thetahat2=[];
thetahat2(:,1)=[1e-3;1e-3];
len=500;
strategy1=2; % agent one is Blame-All
strategy2=2; % agent two is Blame-Me

R= thetatoR(sys.theta,sys.nu,sys.N);


dt= T;
for i=1:len-1
    %sys.A=[x(1,i)+x(2,i)*dt;x(2,i)-dt*(0.1*x(2,i))];
    theta = x(5);
    fr_1 = eye(2)*(1-(cfr1/M)*T);
    fr_2 = 1 - cfr2*T/I;    
    sys.A=[eye(2),T*eye(2),zeros(2); zeros(2), fr_1,zeros(2); 0, 0, 0, 0, 1, T; 0, 0, 0, 0, 0, fr_2];
    B1 = [0, 0;0, 0;T/M, 0;0, T/M;0, 0;sin(theta)*T*l/I, -cos(theta)*T*l/I];
    B2 =[0, 0;0, 0;T/M, 0;0, T/M;0, 0;-sin(theta)*T*l/I, cos(theta)*T*l/I];
    sys.B = [B1,B2];
    F2(:,i)= agent_control(thetahat2(:,i),x(:,i),sys,strategy2);
    F1(:,i) = agent_control(thetahat1(:,i),x(:,i),sys,strategy1);
    %K=-inv(R+sys.B'*sys.P*sys.B)*sys.B'*sys.P;
    F(:,i) = [F1(1:2,i);F2(3:4,i)];
    %F(:,i)=K*sys.A;
    x(:,i+1)=sys.A * x(:,i)+sys.B*F(:,i);
    x(5,i+1)=mod(x(5,i+1)+pi,2*pi)-pi;
    %x(:,i+1)=Acl*x(:,i);
    thetahat1(:,i+1)=agent_learning(thetahat1(:,i),F(:,i),x(:,i),x(:,i+1),sys,strategy1);
    thetahat2(:,i+1)=agent_learning(thetahat2(:,i),F(:,i),x(:,i),x(:,i+1),sys,strategy2);
    thetahat(:,i+1) = [thetahat2(1,i+1);thetahat1(2,i+1)];
    %thetahat(2,i+1) = theta(2);
end
%%j
figure(2)
clf
subplot(311)
hold on
plot([0:len-1],x);
h=legend('$p_x$','$p_y$','$v_x$','$v_y$','$\theta$','$\omega$');%,'x(k+1)/x(k)')
set(h,'Interpreter','Latex');

subplot(312)
plot([0:len-2],F');
h=legend('$F_1^x$','$F_1^y$','$F_2^x$','$F_2^y$');%,'x(k+1)/x(k)')
set(h,'Interpreter','Latex');

subplot(313)
plot([0:len-1],thetahat')
l=legend('$\hat\theta_1^{(2)}$','$\hat\theta_2^{(1)}$');
set(l,'Interpreter','Latex');
xlabel('Time step k')