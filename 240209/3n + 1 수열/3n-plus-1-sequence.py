n = int(input())
cnt = 0
while n != 1:
    n = n / 2 if not n % 2 else n * 3 + 1
    cnt += 1
    
print(cnt)