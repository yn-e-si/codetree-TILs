s1, t1 = input().split()
s2, t2 = input().split()
s3, t3 = input().split()

A = 0

def covid_manual(s, t):
    if s == "Y" and int(t) >= 37:
        return 1
    else:
        return 0

A += covid_manual(s1, t1)
A += covid_manual(s2, t2)
A += covid_manual(s3, t3)

print("E") if A >= 2 else print("N")