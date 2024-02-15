start, end = map(int, input().split())
ans = 0

for i in range(start, end+1):
    cnt = 2
    limit_num = int(i ** 0.5) + 1
    check_num = 2

    while check_num < limit_num:
        if i % check_num == 0 and check_num**2 != i:
            break
        if i % check_num == 0 and check_num**2 == i:
            cnt += 1
        check_num += 1
    
    if cnt == 3:
        ans += 1
print(ans)