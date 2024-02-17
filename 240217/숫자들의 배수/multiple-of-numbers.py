n = int(input())
cnt = 0
ans = 0

while cnt < 2:
    ans += n
    if ans % 5 == 0:
        cnt += 1
    print(ans, end=" ")