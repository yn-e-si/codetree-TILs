n = int(input())
iter_num = 2 * n -1

for i in range(n):
    print("  " * i, end="")
    print("* " * (iter_num - 2*i))

for i in range(n-1):
    print("  " * (n - i - 2), end="")
    print("* " * (2*i+3))