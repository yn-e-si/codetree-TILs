n = int(input())

for i in range(2*n):
    if i % 2:
        print("* " * int((i+1)/2))
    else:
        print("* " * int((n-(i/2))))