start, end = map(int, input().split())
ans = 0
for i in range(start, end+1):
    sum_val = 1
    limit_num = int(i // 2)
    check_num = 2

    while check_num < limit_num:
        if i  % check_num == 0:
            sum_val += check_num
            sum_val += i // check_num
        
        check_num += 1
    
    if sum_val == i:
        ans += 1


print(ans)