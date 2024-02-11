n = int(input())

for i in range(2*n):
    if i % 2:
        print("* " * int((n - (i-1) / 2)))
    else:
        print("* " * int((1 + (i / 2))))