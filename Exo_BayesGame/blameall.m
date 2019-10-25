function u=blameall(thetahat,x,sys)
u=zeros(sum(sys.nu),1);
B=sys.B;
P=sys.P;
A=sys.A;
H_1_list=[];
BPB=B'*P*B;
for i=1:sum(sys.nu)
H_1_list=[H_1_list;BPB(i,i)];
end
H_2=B'*P*B-diag(H_1_list);
H_1=diag(H_1_list)+thetatoR(sys.theta,sys.nu,sys.N);

Rhat= thetatoR(thetahat,sys.nu,sys.N);
Uhat=-inv(Rhat+B'*P*B)*B'*P*A*x;
u=-inv(H_1)*B'*P*A*x-inv(H_1)*H_2*Uhat;

end