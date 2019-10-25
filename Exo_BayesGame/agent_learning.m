function thetahat_new=agent_learning(thetahat,u,x,x_new,sys,strategy)
B=sys.B;
P=sys.P;
A=sys.A;
if strategy==1
    
    for j=1:sys.N
        jindex=sum(sys.nu(1:j-1))+1:sum(sys.nu(1:j));
        if norm(u(jindex))>0
            thetahat_new(j)=-(sys.B(:,jindex)*u(jindex))'*sys.P*x_new/norm(u(jindex))^2;
            thetahat_new(j)=max([thetahat_new(j);-min(svds(sys.B(:,jindex)'*sys.P*sys.B(:,jindex)))]);
        else
            thetahat_new(j)=thetahat(j);
        end
    end
elseif strategy==2
    for j=1:sys.N
        jindex=sum(sys.nu(1:j-1))+1:sum(sys.nu(1:j));
        if norm(u(jindex))>0
            Rhat= thetatoR(thetahat,sys.nu,sys.N);
            Uhat=-inv(Rhat+B'*P*B)*B'*P*A*x;
            xhat(:,j)=A*x+B*Uhat+B(:,jindex)*(u(jindex)-Uhat(jindex));
            thetahat_new(j)=-(sys.B(:,jindex)*u(jindex))'*sys.P*xhat(:,j)/norm(u(jindex))^2;
            thetahat_new(j)=max([thetahat_new(j);-max(svds(sys.B(:,jindex)'*sys.P*sys.B(:,jindex)))]);
        else
            thetahat_new(j)=thetahat(j);
        end
    end
else
    thetahat_new=thetahat;
end
end