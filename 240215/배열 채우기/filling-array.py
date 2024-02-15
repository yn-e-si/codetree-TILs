arr = list(map(int, input().split()))
zero_idx = len(arr)
for idx, value in enumerate(arr):
    if value == 0:
        zero_idx = idx-1
        break
for i in arr[zero_idx::-1]:
    print(i, end=" ")