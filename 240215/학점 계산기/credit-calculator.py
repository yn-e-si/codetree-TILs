n = int(input())
arr = list(map(float, input().split()))
avg_grade = round(sum(arr) / len(arr), 1)

print(f"{avg_grade}")

if avg_grade >= 4.0:
    print("Perfect")
elif avg_grade >= 3.0:
    print("Good")
else:
    print("Poor")