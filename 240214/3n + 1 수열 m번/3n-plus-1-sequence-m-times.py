n = int(input())

for _ in range(n):
    m = int(input())
    cnt = 0
    while m != 1:
        m = m * 3 + 1 if m % 2 else m / 2
        cnt += 1
    print(cnt)