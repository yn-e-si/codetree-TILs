y = int(input())

print("true") if (y % 4 == 0 and y % 100 != 0) or (y % 4 == 0 and y % 100 == 0 and y % 400 == 0) else print("false")