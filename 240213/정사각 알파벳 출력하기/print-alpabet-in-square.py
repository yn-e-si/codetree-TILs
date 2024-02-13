n = int(input())
char = "A"

for _ in range(n):
    for _ in range(n):
        print(char, end="")
        char = chr(ord(char) + 1)
    print()