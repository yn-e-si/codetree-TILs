n = int(input())

for i in range(2, n+1):
    limit_num = int(i**0.5)+1
    check_num = 2
    for num in range(check_num, limit_num+1):
        if not i % num and i != 2:
            break
    else:
        print(i, end=" ")