function u=blameme(thetahat,x,sys)
u=zeros(sum(sys.nu),1);
B=sys.B;
P=sys.P;
A=sys.A;
for j=1:sys.N
    jindex=sum(sys.nu(1:j-1))+1:sum(sys.nu(1:j));
    thetahat_j=thetahat(:);
    thetahat_j(j)=sys.theta(j);
    Rhat_j= thetatoR(thetahat_j,sys.nu,sys.N);
    if det(Rhat_j+B'*P*B)==0
        u(jindex)=zeros(1,length(jindex));
    else
    Uhat_j=-inv(Rhat_j+B'*P*B)*B'*P*A;
    u(jindex)=Uhat_j(jindex);
    if norm(u(jindex))>0
        u(jindex)=min([norm(u(jindex)),5])*u(jindex)/norm(u(jindex));
    end
    end
end
end