a, b, c = map(int, input().split())

print("YES") if all(i % c != 0 for i in range(a, b+1)) else print("NO")