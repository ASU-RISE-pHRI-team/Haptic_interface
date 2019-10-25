function u=noncoop(x,sys)
BPB=sys.B'*sys.P*sys.B;
for i=1:sum(sys.nu)
    H_1_list=[];
    H_1_list=[H_1_list;BPB(i,i)];
end
H_1=diag(H_1_list)+thetatoR(sys.theta,sys.nu,sys.N);
u=-inv(H_1)*sys.B'*sys.P*sys.A*x;
end