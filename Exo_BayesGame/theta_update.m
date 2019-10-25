function thetahat_new = theta_update(thetahat,u,sys)
    B=sys.B;
    P=sys.P;
    A=sys.A;
    x_new = sys.A+sys.B*u;
    for j=1:sys.N
        jindex=sum(sys.nu(1:j-1))+1:sum(sys.nu(1:j));
        if norm(u(jindex))>0
            thetahat_new(j)=-(sys.B(:,jindex)*u(jindex))'*sys.P*x_new/norm(u(jindex))^2;
            thetahat_new(j)=max([thetahat_new(j);-min(svds(sys.B(:,jindex)'*sys.P*sys.B(:,jindex)))]);
        else
            thetahat_new(j)=thetahat(j);
        end
    end

end
