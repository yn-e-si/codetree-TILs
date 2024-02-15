arr = list(map(int, input().split()))

sum_val = 0
total_cnt = 0

for i in arr:
    if i == 0:
        break
    elif not i % 2:
        sum_val += i
        total_cnt += 1

print(total_cnt, sum_val)