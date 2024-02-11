n = int(input())

for i in range(2*n+1):
    for j in range(2*n+1):
        if not i % 2 or not j % 2:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()