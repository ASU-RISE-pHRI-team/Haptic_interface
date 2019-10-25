
%blame all
len=11;
u=zeros(2,len);
x=zeros(1,len);
a=zeros(1,len);
theta=zeros(2,len);
theta(:,1)=[0.1;0.1];
x(1)=5;
theta1=3;
theta2=1;
Uhat=zeros(2,len);
Uhat(:,1)=-inv([1+theta(1,1) 1; 1 1+theta(2,1)])*[1;1]*x(1);
u(1,1)=-inv(theta1+1)*(x(1)+Uhat(2,1));%+randn(1);
u(2,1)=-inv(theta2+1)*(x(1)+Uhat(1,1));%+randn(1);

%u(1,1)=randn(1);
%u(2,1)=randn(1);

for i=1:len-1
    x(i+1)=x(i)+u(1,i)+u(2,i);
    
    theta(1,i+1)=-(x(i)+Uhat(2,i)+u(1,i))/u(1,i);
    theta(2,i+1)=-(x(i)+Uhat(1,i)+u(2,i))/u(2,i);

    if theta(1,i+1)<-1
        theta(1,i+1)=-1;
    end
    if theta(2,i+1)<-1
        theta(2,i+1)=-1;
    end
    Uhat(:,i+1)=-inv([1+theta(1,i+1) 1; 1 1+theta(2,1+i)])*[1;1]*x(1+i);
    u(1,i+1)=-inv(theta1+1)*(x(i+1)+Uhat(2,i+1));%+randn(1)/100;
    u(2,i+1)=-inv(theta2+1)*(x(i+1)+Uhat(1,i+1));%+randn(1)/100;

    a(i+1)=x(i+1)/x(i);
end
figure(1)
clf
subplot(211)
hold on
plot([0:len-1],x,'r');
plot([0:len-1],u');
%axis([1,10,-5,5])
%plot(a,'k');
h=legend('$x(k)$','$u_1(k)$','$u_2(k)$')%,'x(k+1)/x(k)');
set(h,'Interpreter','Latex');

subplot(212)
hold on
plot([0:len-1],theta')
%axis([1,10,-1.5,2])
l=legend('$\hat\theta_1^{(2)}$','$\hat\theta_2^{(1)}$');
set(l,'Interpreter','Latex');
xlabel('Time step k')