n = int(input())
sum_val = 1

for i in range(2, int(n**0.5) + 1):
    if not n % i:
        sum_val += i
        sum_val += n // i

print("P") if sum_val == n else print("N")