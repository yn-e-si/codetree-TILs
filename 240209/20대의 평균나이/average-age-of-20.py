sum_age = 0
cnt = 0

while True:
    age = int(input())
    
    if age >= 30 or age < 20:
        print(f"{sum_age/cnt:.2f}")
        break

    sum_age += age
    cnt += 1