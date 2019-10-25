function R=thetatoR(theta,nu,N)
R=zeros(sum(nu),sum(nu));
c=1;
for i=1:N
    for j=c:c+nu(i)-1
        R(j,j)=theta(i);
    end
    c=j+1;
end

end