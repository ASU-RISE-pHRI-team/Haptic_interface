x=[];F=[];
x(:,1)=[4;10;0;0;-pi/2;0];
v(1)=0;

sys=loadsys(2);
N=sys.N;
theta=sys.theta;


BPB=sys.B'*sys.P*sys.B;
H_1_list=[];
for i=1:sum(sys.nu)
H_1_list=[H_1_list;BPB(i,i)];
end
H_2=BPB-diag(H_1_list);
Acl=eye(sys.nx)-sys.B*inv(H_2)*sys.B'*sys.P;
eig(eye(N*3)-sys.B*inv(H_2)*sys.B'*sys.P)

%%
thetahat=[];
thetahat(:,1)=[1;1];
len=50;
strategy=1;

R= thetatoR(sys.theta,sys.nu,sys.N);


dt=0.2;
for i=1:len-1
    %sys.A=[x(1,i)+x(2,i)*dt;x(2,i)-dt*(0.1*x(2,i))];
    sys.A=[x(1:2,i)+x(3:4,i)*dt;x(3:4,i)-dt*(0.1*x(3:4,i));x(5,i)+dt*x(6,i);x(6,i)-dt*(0.1*x(6,i))];
    sys.B(6,:)=[sin(x(5,i)) -cos(x(5,i)) -sin(x(5,i)) cos(x(5,i))].*3;
    F(:,i)=agent_control(thetahat(:,i),x(:,i),sys,strategy);
    
    %K=-inv(R+sys.B'*sys.P*sys.B)*sys.B'*sys.P; 
    %F(:,i)=K*sys.A;
    x(:,i+1)=sys.A+sys.B*F(:,i);
    x(5,i+1)=mod(x(5,i+1)+pi,2*pi)-pi;
    %x(:,i+1)=Acl*x(:,i);
    thetahat(:,i+1)=agent_learning(thetahat(:,i),F(:,i),x(:,i),x(:,i+1),sys,strategy);
end
%%
figure
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