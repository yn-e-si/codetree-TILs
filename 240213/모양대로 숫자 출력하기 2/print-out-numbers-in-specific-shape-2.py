n = int(input())
cnt = 0

for _ in range(n):
    for _ in range(n):
        cnt += 2
        cnt = cnt % 10 if cnt % 10 else 2
        print(cnt, end=" ")
    print()