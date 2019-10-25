function thetahat_new = theta1_update(thetahat,x,u1,u2,sys)
    B=sys.B;
    P=sys.P;
    A=sys.A;
    u = [u1;u2];
    x_new = sys.A*x+sys.B*u;
    if norm(u1) >0
    thetahat_new= -(sys.B(:,1)*u1)'*sys.P*x_new/norm(u1)^2;
    thetahat_new = max([thetahat_new;-min(svds(sys.B(:,1)'*sys.P*sys.B(:,1)))]);
    else
    thetahat_new=thetahat(1);
    end
   thetahat_new;
end