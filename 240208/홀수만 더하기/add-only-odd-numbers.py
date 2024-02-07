n = int(input())
sum_val = 0

for _ in range(n):
    number = int(input())
    if number % 2 and not number % 3:
        sum_val += number

print(sum_val)