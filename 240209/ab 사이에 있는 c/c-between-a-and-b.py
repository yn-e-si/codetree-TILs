a, b, c = map(int, input().split())

for i in range(a, b+1):
    if not i % c:
        print("YES")
        break
else:
    print("NO")