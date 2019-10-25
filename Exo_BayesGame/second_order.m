%clc
%clear
%close all
%parameters
n_step=3000;
T=0.01;
n_iteration=2;%20

load('DanST.mat')
iotest = iddata(AccST(1:13,3),Tst(1:13,3));
vdata = (AngleST(1:13,3) - AngleST(2:14,3))/0.01;
iotest.InputName = 'Knee Torque';
iotest.OutputName = 'Knee Acceleration';
%ze_iotest = iotest(5:75);
%{
figure
plot(iotest);
figure 
plot(AccST(1:13,3))
figure
plot(Tst(1:13,3))

%sys = ssest(iotest,2) 
%sys_ss = ss(sys)
%}
% system identification and things
nn = tf2.Numerator
aa = tf2.Denominator(1);
bb = tf2.Denominator(2);
cc = tf2.Denominator(3);
M = aa/nn; % thetadd
b = bb/nn; % thetad
k = cc/nn; % theta
%state model
A=[0 1;-k/M -b/M];
B=[0;1/M];
%initial cost function weights
% Qsum=[1000 0; 0 10];
Qsum=[100 0; 0 0];
lambda=1;
QR=Qsum;
QH=Qsum;
QH_hat=[0 0; 0 0];
QH_hat_prev=QH_hat;

%initial gain
LR=zeros(1,2);
LH_hat=[0,0];
LR_hat=[0,0];
PH_hat=[0 0;0 0];
PR_hat=[0 0;0 0];
% PH_hat_prev=PH_hat;

xd=0.1;
uR=0;
uH=0;
for j=1:n_iteration

%
    x = 0; %position
    dot_x=0;    %velocity
    ddot_x=0;   %acceleration
    e=0;    % position error
    xi=[e;dot_x];   %state matrix
    xi_hat=xi;      %estimate of state matrix
    xi_hatR=xi;     %estimate of robot state matrix
    xi_hatH=xi;
    xd = 10;
    for i=1:n_step
    %Q = [100,0; 0,1];%Initial Q matix
    %R = 1;
    %N = [0;0];
    %[K_lqr,S_lqr,e_lqr] = lqr(A,B,Q,R)
    
    
        AH_hat=A-B*(LR_hat);%+1*[0,50] to simulate biased estimation
        PH = care(AH_hat,B,QH,1);
        LH=B'*PH; 
        uH=-LH*xi

        %%%%%%%%robot
        AR_hat=A-B*(LH_hat);%+1*[0,50] to simulate biased estimation
        PR = care(AR_hat,B,QR,1);
        LR=B'*PR;
        uR=-LR*xi
        
        Gamma=[10,0;0,1];
        uH_hat=-LH_hat*xi;
        xi_tilde=xi_hat-xi;        
        xi_hat=xi_hat+T*(A*xi_hat+B*uR+B*uH_hat-Gamma*xi_tilde);

        %%%%%%%%%%robot's update law
        alpha=[0,0;0,10000];
        A_RH_hat=A-B*LH_hat-B*LR;
        PH_hat=PH_hat+T*alpha*(xi_tilde*xi');
        PH_hat(1,2)=PH_hat(2,1);%since PH_hat is symmetric;
        LH_hat=B'*PH_hat;%0* simulating that the robot doesn't consider human's input 

        AH=A-B*LR;
        QH_hat=-(AH'*PH_hat+PH_hat*AH-PH_hat*B*B'*PH_hat);
        QH_hat(1,2)=0;
        QH_hat(2,1)=0;
        
        %%%%%%%human's observer
        GammaH=[10,0;0,1];
        uR_hat=-LR_hat*xi;
        xi_tildeH=xi_hatH-xi;        
        xi_hatH=xi_hatH+T*(A*xi_hatH+B*uR_hat+B*uH-GammaH*xi_tildeH);

        %%%%%%%%%%human's update law
        alphaH=[0,0;0,10000];
        A_HR_hat=A-B*LH-B*LR_hat;
        PR_hat=PR_hat+T*alphaH*(xi_tildeH*xi');
        PR_hat(1,2)=PR_hat(2,1);
        LR_hat=B'*PR_hat;%0* simulating that the human doesn't consider robot's input

        AR=A-B*LH;
        QR_hat=-(AR'*PR_hat+PR_hat*AR-PR_hat*B*B'*PR_hat);
        QR_hat(1,2)=0;
        QR_hat(2,1)=0;

        %state update
        xi=xi+T*(A*xi+B*uR+B*uH);
        x=xi(1)+xd;
        dot_x=xi(2);
    end
end   
