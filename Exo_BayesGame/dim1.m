B_1=[1;0];
B_2=[0;1];
B=[B_1 B_2];
P=[1 0.9;0.9 1];
R=[1 0; 0 1];
K=inv(R+B'*P*B)*B'*P;
%K_2=[0 1]*inv(R+B'*P*B)*B'*P;
K_1=inv(B_1'*B_1)*B_1';
K_2=inv(B_2'*B_2)*B_2';
D=R+B'*P*B;
H_1=[D(1,1) 0; 0 D(2,2)];
H_2=D-H_1;
Delta=inv(H_2)*(H_1)
A=eye(2);%[0.9 1; 0 0.9];
%Acl=(eye(2)-B*K)*A
%Acl=(eye(2)-B_1*K_1-B_2*K_2)*A
Acl=eye(2)-[B_1 [0;0]]*inv(H_2)*B'*P-B_2*K_2
%A=eye(2)-B*K
lambda=eig(Acl)
sigma=svd(Acl)
%svd(B_1*K_1*A)
%svd(B_2*K_2*A)