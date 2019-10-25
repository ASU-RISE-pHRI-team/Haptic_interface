function sys=loadsys(scenario)
switch scenario
    case 1
        sys.N=2;
        sys.nx=2;
        for i=1:sys.N
            sys.nu(i)=1;
        end
        sys.theta=[0.3;0.5];
        sys.A=[1;1];
        sys.B=[0 0;1 1];
        sys.P=[4 0.3;0.3 1];
    case 2
        sys.N=2;
        sys.nx=6;
        for i=1:sys.N
            sys.nu(i)=2;
        end
        sys.theta=[0.3;0.9];
        sys.A=[1;1;1;1;1;1];
        sys.B=[0 0 0 0;
               0 0 0 0;
               1 0 1 0;
               0 1 0 1;
               0 0 0 0;
               1 -1 -1 1];
        sys.P=[4    0   0.3    0.1   0   0;
               0    4     0.1  0.3   0   0;
               0.3  0.1     1    0.1   0   0;
               0.1  0.3     0.1    1   0   0;
               0    0     0    0   9  0.3;
               0    0     0    0 0.3   1] ;
    case 3
        sys.N=3;
        sys.nx=1;
        for i=1:sys.N
            sys.nu(i)=1;
        end
        sys.theta=[0.1;2;0.5];
        
        sys.A=1;
        sys.B=[1 0.2 2];
        sys.P=1;
    case 4
        sys.N=4;
        sys.nx=1;
        for i=1:sys.N
            sys.nu(i)=1;
        end
        sys.theta=[0.1;2;0.5;0.3];
        
        sys.A=1;
        sys.B=[1 1 3 2];
        sys.P=1;
    case 5
        sys.N=2;
        sys.nx=2;
        for i=1:sys.N
            sys.nu(i)=1;
        end
        sys.theta=[.6;.9];
%         sys.A=[0.999231164278398,0.037683139459564;-0.037683139459564,0.886181745899708];
        sys.A = [0.983518120878556,0.149401431590646;-0.149401431590646,0.535313826106619];
        %sys.B=[0.000768835721601651,0.000768835721601651;0.0376831394595636,0.0376831394595636];
        sys.B = [0,0;1,1];
        sys.P=[1 0;0 1] ;
end
end