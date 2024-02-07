a, b = map(int, input().split())

ans=""

for idx in range(21):
    ans += str(a//b)
    a = (a % b) * 10
    
    if idx == 0:
        ans += "."

print(ans)