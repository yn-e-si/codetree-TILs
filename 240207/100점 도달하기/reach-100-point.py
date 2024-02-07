n = int(input())

for score in range(n, 101):
    if 90 <= score:
        print("A", end=" ")
    elif 80 <= score:
        print("B", end=" ")
    elif 70 <= score:
        print("C", end=" ")
    elif 60 <= score:
        print("D", end=" ")
    else:
        print("E", end=" ")