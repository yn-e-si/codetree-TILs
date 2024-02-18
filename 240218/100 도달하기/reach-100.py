first_num = 1
next_num = int(input())
ans = 0
print(first_num, next_num, end=" ")

while ans < 100:
    ans = first_num + next_num
    first_num, next_num = next_num, ans
    print(ans, end=" ")