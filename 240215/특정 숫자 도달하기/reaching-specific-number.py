arr = list(map(int, input().split()))
sum_val = 0
total_cnt = 0
for i in arr:
    if i >= 250:
        break
    sum_val += i
    total_cnt += 1
print(f"{sum_val} {sum_val/total_cnt:.1f}")