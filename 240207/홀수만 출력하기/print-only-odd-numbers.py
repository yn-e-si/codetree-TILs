n = int(input())

for _ in range(n):
    number = int(input())
    if number % 2 and not number % 3:
        print(number)