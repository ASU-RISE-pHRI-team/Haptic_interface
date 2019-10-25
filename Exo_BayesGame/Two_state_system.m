syms x y 
kx=1; ky=1;
Gx=3; Gy=1;
[solx,soly] = solve(x^2-(Gx+y+1)*x+Gx*(y+1)-kx/2 == 0, y^2-(Gy+x-1)*y+Gy*(x-1)-ky/2 == 0)

%%
%dim(N)=N=2
theta1=0.1;
theta2=0.9;
len=51;
u=zeros(2,len);
x=zeros(1,len);
a=zeros(1,len);
theta=zeros(2,len);
theta(:,1)=[1;1];
x(1)=5;
u(1,1)=-theta(2,1)*x(1)/(theta1*(1+theta(2,1))+theta(2,1));
u(2,1)=-theta(1,1)*x(1)/(theta2*(1+theta(1,1))+theta(1,1));



thetahat=zeros(2,len);

for i=1:len-1
    x(i+1)=x(i)+u(1,i)+u(2,i);
    %frac=u(2,i)/(x(i)+u(2,i));
    u(1,i+1)=x(i+1)^2/(theta1*u(2,i)-(1+theta1)*x(i+1));
    
    %frac=u(1,i)/(x(i)+u(1,i));
    u(2,i+1)=x(i+1)^2/(theta2*u(1,i)-(1+theta2)*x(i+1));
    
    theta(2,i+1)=-(x(i)+u(1,i))/u(2,i)-1;
    theta(1,i+1)=-(x(i)+u(2,i))/u(1,i)-1;
    if theta(1,i+1)<-1
        theta(1,i+1)=-1;
    end
    if theta(2,i+1)<-1
        theta(2,i+1)=-1;
    end
        
    a(i+1)=x(i+1)/x(i);
end
figure(1)
clf
subplot(211)
hold on
plot([0:len-1],x,'r');
plot([0:len-1],u');
%plot(a,'k');
h=legend('$x(k)$','$u_1(k)$','$u_2(k)$')%,'x(k+1)/x(k)')
set(h,'Interpreter','Latex');

subplot(212)
plot([0:len-1],theta')
axis([1,30,-1.5,6])
l=legend('$\hat\theta_1^{(2)}$','$\hat\theta_2^{(1)}$')
set(l,'Interpreter','Latex');
xlabel('Time step k')
%%
%one side 
theta1=100;
theta2=100;
a=zeros(1,100);a(1)=-1;
for i=1:99
    k11=theta1*theta2*(1+theta1)/(theta1+theta2+theta1*theta2);
    k12=theta1*theta2+theta2-1;
    k21=theta1;
    k22=(1+theta1)*(theta1+theta2+theta1*theta2)/theta1;
    a(i+1)=(k11+k12*a(i))/(k21+k22*a(i));
end
k=theta1*theta2/(theta1+theta2+theta1*theta2);
figure(1)
clf
hold on
plot(a(1:50));
plot(ones(50,1)*k,'r');
%%
%dim=1
len=10;
u=zeros(2,len);
x=zeros(1,len);
a=zeros(1,len);
theta=zeros(2,len);
theta(:,1)=[2;2];
x(1)=5;
u(1,1)=-theta(2,1)*x(1)/(theta1*(1+theta(2,1))+theta(2,1));
u(2,1)=-theta(1,1)*x(1)/(theta2*(1+theta(1,1))+theta(1,1));

theta1=0.1;
theta2=0.9;

thetahat=zeros(2,len);

for i=1:len-1
    x(i+1)=x(i)+u(1,i)+u(2,i);
    %frac=u(2,i)/(x(i)+u(2,i));
    u(1,i+1)=x(i+1)^2/(theta1*u(2,i)-(1+theta1)*x(i+1));
    
    %frac=u(1,i)/(x(i)+u(1,i));
    %u(2,i+1)=x(i+1)^2/(theta2*u(1,i)-(1+theta2)*x(i+1));
    
    theta(2,i+1)=-(x(i)+u(1,i))/u(2,i)-1;
    %theta(1,i+1)=-(x(i)+u(2,i))/u(1,i)-1;
    theta(1,i+1)=theta(1,i);
    if theta(1,i+1)<-1
        theta(1,i+1)=-1;
    end
    if theta(2,i+1)<-1
        theta(2,i+1)=-1;
    end
    u(2,i+1)=-theta1*x(i+1)/(theta2*(1+theta1)+theta1);
        
    a(i+1)=x(i+1)/x(i);
end
figure(1)
clf
subplot(211)
hold on
plot(x,'r');
plot(u');
%axis([1,10,-5,5])
%plot(a,'k');
h=legend('$x(k)$','$u_1(k)$','$u_2(k)$')%,'x(k+1)/x(k)')
set(h,'Interpreter','Latex');

subplot(212)
hold on
plot(theta2*ones(1,len));
plot(theta(2,:),'k')
%axis([1,10,-1.5,2])
l=legend('$\theta_2$','$\hat\theta_2^{(1)}$')
set(l,'Interpreter','Latex');
xlabel('Time step k')