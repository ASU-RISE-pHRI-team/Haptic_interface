clear                               
x=[];F=[];
x(:,1)=[1;0];
v(1)=0;
% agent 1: teacher; agent 2: student
sys=loadsys(5);
N=sys.N;
theta=sys.theta;


BPB=sys.B'*sys.P*sys.B;
H_1_list=[];
for i=1:sum(sys.nu)
H_1_list=[H_1_list;BPB(i,i)];
end
H_2=BPB-diag(H_1_list);
   
%%
thetahat=[];
thetahat(:,1)=[1;1];
len=200;
strategy=1;

R= thetatoR(sys.theta,sys.nu,sys.N);
load('ref.mat')
t = 0:1/25:(len-1)/5;
ref = [traj vel]';
F0 = [];
xi= [];
xi(:,1)=ref(:,1);
dt=1/25;
for i=1:len-1
%     sys.A=[x(1:2,i)+x(3:4,i)*dt;x(3:4,i)-dt*(0.1*x(3:4,i));x(5,i)+dt*x(6,i);x(6,i)-dt*(0.1*x(6,i))];
%     sys.B(6,:)=[sin(x(5,i)) -cos(x(5,i)) -sin(x(5,i)) cos(x(5,i))].*3;
    F(:,i)=agent_control(thetahat(:,i),x(:,i),sys,strategy);
    %K=-inv(R+sys.B'*sys.P*sys.B)*sys.B'*sys.P;
    %F(:,i)=K*sys.A;
    x(:,i+1)=sys.A*x(:,i)+sys.B*F(:,i);
    %x(:,i+1)=Acl*x(:,i);
    thetahat(:,i+1)=agent_learning(thetahat(:,i),F(:,i),x(:,i),x(:,i+1),sys,strategy);
    %thetahat(2,i+1) = theta(2);
    xi(:,i+1) = x(:,i+1) + ref(:,i+1);
    F0(:,i) = F(:,i) + [0.4*u0(i),0.6*u0(i)]';
end
xi(1,:) = xi(1,:)/pi*180;
ref(1,:) = ref(1,:)/pi*180;
%%j
figure(strategy)
clf
subplot(311)
hold on
plot([0:len-1],xi(1,:),'b-.');
plot([0:len-1],ref(1,1:len),'r-');
ylabel('Angle (deg)')
legend('$$x$$','$$x_{ref}$$','Interpreter','Latex')
% h=legend('$p_x$','$p_y$','$v_x$','$v_y$','$\theta$','$\omega$');%,'x(k+1)/x(k)')
% set(h,'Interpreter','Latex');

subplot(312)
hold on
plot([0:len-2],F0(2,:)','b-.');
plot([0:len-2],F0(1,:)','r-');
ylabel('Torque (Nm)')
legend('$$u_{h}$$','$$u_{r}$$','Interpreter','Latex')
% h=legend('$F_1^x$','$F_1^y$','$F_2^x$','$F_2^y$');%,'x(k+1)/x(k)')
% set(h,'Interpreter','Latex');

subplot(313)
hold on
theta1 = theta(1) * ones(1,20);
theta2 = theta(2) * ones(1,20);

plot([0:len-1],thetahat(1,:)','b-.')
plot([0:len-1],thetahat(2,:)','r-')
scatter([0:10:len-1],theta1,'bo')
scatter([0:10:len-1],theta2,'ro')

ylabel('Parameter estimation')
legend('$$\hat{\theta}^h_r$$','$$\hat{\theta}^{r}_{h}$$','Interpreter','Latex')
% l=legend('$\hat\theta_1^{(2)}$','$\hat\theta_2^{(1)}$');
% set(l,'Interpreter','Latex');
xlabel('Time step k')