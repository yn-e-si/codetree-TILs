arr = list(map(int, input().split()))

for idx, val in enumerate(arr):
    if val % 3 == 0:
        thr_mul_idx = idx
        break
print(arr[thr_mul_idx-1])