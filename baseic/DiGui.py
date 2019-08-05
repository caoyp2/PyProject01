total = 0
def count(n):
    global total
    total = total + n
    if n == 1:
        print(total)
        return
    n = n - 1;
    count(n)


count(10)


