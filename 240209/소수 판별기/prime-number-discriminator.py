n = int(input())

print("P") if all(n % i for i in range(2, n)) else print("C")