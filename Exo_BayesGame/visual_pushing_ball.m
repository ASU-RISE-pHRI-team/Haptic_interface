clear

sys=loadsys(3);
strategy=2;%0:non-cooperative;1:blameme;2:blameall

len=20;
u=zeros(sum(sys.nu),len);
x=zeros(1,len);
thetahat=zeros(sys.N,len);
thetahat(:,1)=[0.01;0.01;0.01];
x(1)=10;
H_1_list=[];
BPB=sys.B'*sys.P*sys.B;
for i=1:sum(sys.nu)
H_1_list=[H_1_list;BPB(i,i)];
end
H_2=BPB-diag(H_1_list);
H_1=diag(H_1_list)+thetatoR(sys.theta,sys.nu,sys.N);

%closed looo matrix
A_cl_n=sys.A-sys.B*inv(H_1)*sys.B'*sys.P
%% Setup the Plots
fighandle = figure(1);%simulation plane
%set(gcf,'Position',get(0,'ScreenSize'),'color','w')

hold on;
axis equal
axis([-20 20 -20 20]);
grid on;

object.pos=[10;0];

object.handle = plot(object.pos(1,end),object.pos(2,end),'o','linewidth',3,'color','r','markersize',50);
set(object.handle,'XDataSource','object.pos(1,end)');
set(object.handle,'YDataSource','object.pos(2,end)');

robot1.handle = plot(object.pos(1,end)-1,object.pos(2,end),'o','linewidth',3,'color','k','markersize',10);
set(robot1.handle,'XDataSource','object.pos(1,end)-1');
set(robot1.handle,'YDataSource','object.pos(2,end)');

robot2.handle = plot(object.pos(1,end)+1,object.pos(2,end),'o','linewidth',3,'color','k','markersize',10);
set(robot2.handle,'XDataSource','object.pos(1,end)+1');
set(robot2.handle,'YDataSource','object.pos(2,end)');

robot3.handle = plot(object.pos(1,end),object.pos(2,end)+1,'o','linewidth',3,'color','k','markersize',10);
set(robot3.handle,'XDataSource','object.pos(1,end)');
set(robot3.handle,'YDataSource','object.pos(2,end)+1');

%% Animation
pause(0.5);
%initialize
u(:,1)=agent_control(thetahat(:,1),x(1),sys,strategy);
umax=2;
for i=2:len
    d=randn(sum(sys.nu),1)./10;
    x(i)=sys.A*x(i-1)+sys.B*u(:,i-1);
    thetahat(:,i)=agent_learning(thetahat(:,i-1),u(:,i-1)+d,x(i-1),sys,strategy);
    u(:,i)=agent_control(thetahat(:,i),x(i),sys,strategy);
    for j=1:size(u,1)
     if norm(u(j,i))>umax
         u(j,i)=u(j,i)/norm(u(j,i))*umax;
     end
    end
    
    object.pos=[object.pos [x(i);0]];
    refreshdata([object.handle,robot1.handle,robot2.handle,robot3.handle])
    pause(0.5);
end


%%
figure(2)
clf
subplot(211)
hold on
plot([0:len-1],x,'r');
plot([0:len-1],u');
h=legend('$x(k)$','$u_1(k)$','$u_2(k)$');%,'x(k+1)/x(k)')
set(h,'Interpreter','Latex');

subplot(212)
plot([0:len-1],thetahat')
l=legend('$\hat\theta_1^{(2)}$','$\hat\theta_2^{(1)}$');
set(l,'Interpreter','Latex');
xlabel('Time step k')