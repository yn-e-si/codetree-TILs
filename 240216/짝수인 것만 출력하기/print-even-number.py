n = int(input())
arr = list(map(int, input().split()))
even_arr = arr[1::2]

for i in even_arr:
    print(i, end=" ")