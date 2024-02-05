a, b, c = map(int, input().split())

total_sum = a + b + c
total_avg = int(total_sum / 3)

print(total_sum, total_avg, total_sum - total_avg, sep="\n")