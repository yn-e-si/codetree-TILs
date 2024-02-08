n = int(input())

for i in range(1, n+1):
    if not i % 2 or i % 10 == 5 or (not i % 3 and i % 9):
        continue
    print(i, end=" ")