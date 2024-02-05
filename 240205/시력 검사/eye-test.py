a = float(input())
b = float(input())

print("High") if 1 <= a and 1 <= b else (print("Middle") if 0.5 <= a and 0.5 <= b else print("Low"))