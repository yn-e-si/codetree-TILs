n = int(input())
cnt = 0

for i in range(n):
    if i % 2:
        cnt += n
        for j in range(n):
            print(cnt-j, end=" ")
    else:
        for j in range(n):
            cnt += 1
            print(cnt, end=" ")
    print()