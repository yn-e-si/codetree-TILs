n = int(input())
cnt = 0

for i in range(1, n+1):
    if i % 4 or (not i % 100 and i % 400):
        cnt += 1
print(n-cnt)