n = int(input())
arr = list(map(int, input().split()))

for i in arr[::-1]:
    if not i % 2:
        print(i, end=" ")