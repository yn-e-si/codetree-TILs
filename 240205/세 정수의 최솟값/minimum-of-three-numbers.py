a, b, c = map(int, input().split())

if a < b:
    if b < c or a < c:
        print(a)
    else:
        print(c)
else:
    if b < c or a <c:
        print(b)
    else:
        print(c)