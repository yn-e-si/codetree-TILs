n = int(input())
cnt = 10

for _ in range(n):
    for _ in range(n):
        cnt -= 1
        cnt = cnt if cnt != 0 else 9
        print(cnt, end="")
    print()