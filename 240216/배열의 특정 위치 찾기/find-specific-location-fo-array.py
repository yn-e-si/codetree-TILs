arr = list(map(int, input().split()))
even_arr = arr[1::2]
thr_mul_arr = arr[2::3]

sum_even = sum(even_arr)
avg_thr_mul = round(sum(thr_mul_arr) / len(thr_mul_arr), 1)
print(sum_even, avg_thr_mul)