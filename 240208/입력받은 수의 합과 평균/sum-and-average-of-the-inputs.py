n = int(input())
sum_val = 0

for _ in range(n):
    number = int(input())
    sum_val += number

print(f"{sum_val} {sum_val/n:.1f}")