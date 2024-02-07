n = int(input())

for i in range(1, n+1):
    if i % 3 == 0 or any(c in str(i) for c in ["3", "6", "9"]):
        print("0", end=" ")
    else:
        print(i, end=" ")