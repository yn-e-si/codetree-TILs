n = int(input())
cnt = 0

for i in range(n):
    for j in range(n):
        cnt += 1
        cnt = cnt % 10 if cnt % 10 else 1
        print(cnt, end="")
    print()