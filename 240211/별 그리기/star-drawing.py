n = int(input())

for i in range(n):
    print(" " * (2-i), end="")
    print("*" * (2*i+1))

for i in range(n-1):
    print(" " * (i+1), end="")
    print("*" * (3 - i*2))