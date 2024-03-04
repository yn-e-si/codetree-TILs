arr = list(map(int, input().split(" ")))
count_arr = [0 for _ in range(9)]

for i in arr:
    if i == 0:
        break
    elif i < 10:
        continue
    else:
        n = i // 10
        count_arr[n-1] += 1

for idx, num in enumerate(count_arr):
    print(f"{idx+1} - {num}")