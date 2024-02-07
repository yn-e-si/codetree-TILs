n = int(input())

classroom_cnt = corridor_cnt = toilet_cnt = 0

toilet_cnt = n // 12
corridor_cnt = n // 3 - toilet_cnt
classroom_cnt = n // 2 - n // 6

print(classroom_cnt, corridor_cnt, toilet_cnt)