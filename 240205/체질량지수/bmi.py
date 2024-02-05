h, w = map(int, input().split())

bmi = int((w * (100 ** 2)) / (h**2))
print(bmi)

if bmi >= 25:
    print("Obesity")