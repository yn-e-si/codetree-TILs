n = int(input())
pass_cnt = 0

for i in range(n):
    arr = list(map(int, input().split()))
    avg_score = round(sum(arr)/len(arr))
    if avg_score >= 60:
        pass_cnt += 1
        print("pass")
    else:
        print("fail")
print(pass_cnt)