a, b = map(int, input().split())

if any(1920 % i == 0 and 2880 % i == 0 for i in range(a, b+1)):
    print(1)
else:
    print(0)