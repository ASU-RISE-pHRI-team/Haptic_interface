ds=[1,-1];
figure(1);clf;hold on
axis equal
axis([-1.5 4 0 11])
for i=1:len-1
plot(x(1,i)+ds.*cos(x(5,i)),x(2,i)+ds.*sin(x(5,i)),'k','MarkerSize',50);
pause(0.1)
end
plot(x(1,:),x(2,:))


xlabel('x');
ylabel('y')