n = int(input())
char = "A"

for i in range(n):
    for j in range(n):
        if i <= j:
            print(char, end=" ")
            char = chr(ord(char) + 1) if ord(char) < 90 else "A"
        else:
            print(" ", end=" ")

    print()