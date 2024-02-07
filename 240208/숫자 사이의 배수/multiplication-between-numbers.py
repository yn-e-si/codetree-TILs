a, b = map(int, input().split())
sum_val = cnt = 0
for i in range(a, b+1):
    if not i % 5 or not i % 7:
        sum_val += i
        cnt += 1
print(f"{sum_val} {sum_val/cnt:.1f}")