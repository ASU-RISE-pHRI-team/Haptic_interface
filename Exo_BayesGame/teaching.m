function u1=teaching(thetahat,F2,sys,x)

B=sys.B;
P=sys.P;
A=sys.A;
theta = sys.theta;
u0 = F2(1);
u2 = F2(2);
fun = @(u1) norm(theta1_update(thetahat,x,u1,u2,sys)-theta(1));
u1 = fminunc(fun,u0);
end                                                                                                                                                                                                                                   