n = int(input())

for i in range(n):
    print("*" * (n-i), end="")
    print(" " * i, end="")
    print(" " * i, end="")
    print("*" * (n-i), end="")
    print()