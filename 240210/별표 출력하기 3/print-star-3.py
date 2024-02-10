n = int(input())

for i in range(n):
    print(" " * i*2, end="")
    for j in range(2*(n-i)-1):
        print("*", end=" ")
    print()