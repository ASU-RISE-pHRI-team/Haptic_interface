function u=agent_control(thetahat,x,sys,strategy)
if strategy==1
    u=blameme(thetahat,x,sys);
elseif strategy==2
    u=blameall(thetahat,x,sys);
else
    u=noncoop(x,sys);
end
end