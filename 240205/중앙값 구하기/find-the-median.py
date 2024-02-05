a, b, c = map(int, input().split())

if a < b < c or c < b < a:
    print(b)
elif b < c < a or a < c < b:
    print(c)
else:
    print(a)