arr = list(map(int, input().split()))
count_arr = [ 0 for i in range(7)]

for elem in arr:
    count_arr[elem] += 1

for i in range(6):
    print(f"{i+1} - {count_arr[i+1]}")