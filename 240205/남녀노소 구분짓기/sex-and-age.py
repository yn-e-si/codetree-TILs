sex = int(input())
age = int(input())

if sex == 0:
    if age > 18:
        print("MAN")
    else:
        print("BOY")
else:
    if age > 18:
        print("WOMAN")
    else:
        print("GIRL")