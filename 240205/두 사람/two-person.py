a_age, a_sex = input().split()
b_age, b_sex = input().split()

print(1) if (int(a_age) > 18 and a_sex == "M") or (int(b_age) > 18 and b_sex == "M") else print(0)