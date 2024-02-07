a, b = map(int, input().split())

ans="0."
a *= 10

for _ in range(20):
    ans += str(a//b)
    a = (a % b) * 10

print(ans)