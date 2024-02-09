user = {
    1: "John",
    2: "Tom",
    3: "Paul",
    4: "Sam",
}

while True:
    n = int(input())

    ans = user.get(n, 0)

    if ans == 0:
        print("Vacancy")
        break
    print(ans)