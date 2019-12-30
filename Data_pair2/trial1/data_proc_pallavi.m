action_1 = loadaction("action_h1.csv");
action_2 = loadaction("action_h2.csv");
[L1, L2] = size(action_1);
[M1, M2] = size(action_2);

for i=1:L1
    if action_1(i)< 1.5 && action_1(i)> -1.5
        action_1(i) = 0;
    end
    if action_1(i)< 3.0 && action_1(i)> 1.5
        action_1(i) = 2.0;
    end
    if action_1(i)< 4.5 && action_1(i)> 3.0
        action_1(i) = 2.0;
    end
    if action_1(i)> 4.5
        action_1(i) = 5.0;
    end
    
    if action_1(i)< -1.5 && action_1(i)> -3.0
        action_1(i) = -2.0;
    end
    if action_1(i)< -3.0 && action_1(i)> -4.5
        action_1(i) = -2.0;
    end
    if action_1(i)< -4.5
        action_1(i) = -5.0;
    end
        
end

for i=1:M1
    if action_2(i)< 1.5 && action_2(i)> -1.5
        action_2(i) = 0;
    end
    if action_2(i)< 3.0 && action_2(i)> 1.5
        action_2(i) = 2.0;
    end
    if action_2(i)< 4.5 && action_2(i)> 3.0
        action_2(i) = 2.0;
    end
    if action_2(i)> 4.5
        action_2(i) = 5.0;
    end
    
    if action_2(i)< -1.5 && action_2(i)> -3.0
        action_2(i) = -2.0;
    end
    if action_2(i)< -3.0 && action_2(i)> -4.5
        action_2(i) = -2.0;
    end
    if action_2(i)< -4.5
        action_2(i) = -5.0;
    end
        
end
csvwrite('new_action_h1.csv', action_1)
csvwrite('new_action_h2.csv', action_2)
