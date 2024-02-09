n = int(input())

for i in range(2, n):
    if not n % i:
        print("C")
        break
else:
    print("N")