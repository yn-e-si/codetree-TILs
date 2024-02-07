a, b = map(int, input().split())

a, b = (a, b) if a < b else (b, a)

for i in range(b, a-1, -1):
    print(i, end=" ")