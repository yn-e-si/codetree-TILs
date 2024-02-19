n, m = map(int, input().split())
an = [n, m]

for i in range(10):
    an.append(an[i+1] + 2 *an[i])
    print(an[i], end=" ")