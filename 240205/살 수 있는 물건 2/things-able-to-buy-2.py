n = int(input())

if 3000 <= n:
    print("book")
elif 1000 <= n < 3000:
    print("mask")
elif 500 <= n < 1000:
    print("pen")
else:
    print("no")