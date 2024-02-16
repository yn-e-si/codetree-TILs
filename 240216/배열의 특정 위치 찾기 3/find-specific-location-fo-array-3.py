arr = list(map(int, input().split()))
zero_idx = 3

for idx, num in enumerate(arr):
    if num == 0:
        zero_idx = idx
        break

print(sum(arr[zero_idx-3:zero_idx]))