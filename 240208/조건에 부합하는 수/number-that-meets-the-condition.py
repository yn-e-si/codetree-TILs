a = int(input())

for i in range(1, a+1):
    if (not i % 2 and i % 4) or not (i // 8) % 2 or i % 7 < 4:
        continue
    print(i, end=" ")