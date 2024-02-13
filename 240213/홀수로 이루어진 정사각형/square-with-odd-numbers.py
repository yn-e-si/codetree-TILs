n = int(input())
start_odd_num = 11

for i in range(0, n*2, 2):
    for j in range(0, n*2, 2):
        print(start_odd_num+i+j, end=" ")
    print()