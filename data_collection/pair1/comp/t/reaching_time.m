a1(:,1) = getdata("1\action_h1.csv");
a1(:,2) = getdata("1\action_h2.csv");
a2(:,1) = getdata("2\action_h1.csv");
a2(:,2) = getdata("2\action_h2.csv");
a3(:,1) = getdata("3\action_h1.csv");
a3(:,2) = getdata("3\action_h2.csv");
a4(:,1) = getdata("4\action_h1.csv");
a4(:,2) = getdata("4\action_h2.csv");
a5(:,1) = getdata("5\action_h1.csv");
a5(:,2) = getdata("5\action_h2.csv");
a6(:,1) = getdata("6\action_h1.csv");
a6(:,2) = getdata("6\action_h2.csv");
a7(:,1) = getdata("7\action_h1.csv");
a7(:,2) = getdata("7\action_h2.csv");
a8(:,1) = getdata("8\action_h1.csv");
a8(:,2) = getdata("8\action_h2.csv");
a9(:,1) = getdata("9\action_h1.csv");
a9(:,2) = getdata("9\action_h2.csv");
a10(:,1) = getdata("10\action_h1.csv");
a10(:,2) = getdata("10\action_h2.csv");
[L1, L2] = size(a1);
temp = [];
for i = L1:-1:1
    if a1(i,1) ~= 0 || a1(i,2) ~= 0
        temp(1,1) = i;
        break;
    end
end
for i = L1:-1:1
    if a2(i,1) ~= 0 || a2(i,2) ~= 0
        temp(2,1) = i;
        break;
    end
end
for i = L1:-1:1
    if a3(i,1) ~= 0 || a3(i,2) ~= 0
        temp(3,1) = i;
        break;
    end
end
for i = L1:-1:1
    if a4(i,1) ~= 0 || a4(i,2) ~= 0
        temp(4,1) = i;
        break;
    end
end
for i = L1:-1:1
    if a5(i,1) ~= 0 || a5(i,2) ~= 0
        temp(5,1) = i;
        break;
    end
end
for i = L1:-1:1
    if a6(i,1) ~= 0 || a6(i,2) ~= 0
        temp(6,1) = i;
        break;
    end
end
for i = L1:-1:1
    if a7(i,1) ~= 0 || a7(i,2) ~= 0
        temp(7,1) = i;
        break;
    end
end
for i = L1:-1:1
    if a8(i,1) ~= 0 || a8(i,2) ~= 0
        temp(8,1) = i;
        break;
    end
end
for i = L1:-1:1
    if a9(i,1) ~= 0 || a9(i,2) ~= 0
        temp(9,1) = i;
        break;
    end
end
for i = L1:-1:1
    if a10(i,1) ~= 0 || a10(i,2) ~= 0
        temp(10,1) = i;
        break;
    end
end
plot(temp, '*')
reach = mean(temp);
disp(reach)