m = int(input())

if m < 3 or 11 < m:
    print("Winter")
elif 3 <= m < 6:
    print("Spring")
elif 6 <= m < 9:
    print("Summer")
else:
    print("Fall")