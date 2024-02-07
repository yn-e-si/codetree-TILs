a, b = map(int, input().split())
sum_val = 0
a, b = (a, b) if a < b else (b, a)

for i in range(a, b+1):
    if not i % 5:
        sum_val += i
print(sum_val)