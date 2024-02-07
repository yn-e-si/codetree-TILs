three_cnt = five_cnt = 0

for _ in range(10):
    n = int(input())
    if not n % 3:
        three_cnt += 1
    if not n % 5:
        five_cnt += 1

print(three_cnt, five_cnt)