n = int(input())
ans = 0
cnt = 1
while n > 1:
    n //= cnt
    cnt += 1
    ans += 1
print(ans)