a, b = map(int, input().split())

def even_check(num):
    if num % 2 == 0:
        print("even")
    else:
        print("odd")

even_check(a)
even_check(b)