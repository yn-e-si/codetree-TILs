a, b, c = map(int, input().split())

if a < b < c:
    print(b)
elif b < c < a:
    print(c)
else:
    print(a)