n, m = map(int, input().split())

for i in range(10):
    print(n, end=" ")
    n, m = m, (n+m) % 10