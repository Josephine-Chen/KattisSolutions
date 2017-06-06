while True:
    n = int(input())
    if n == -1:
        break
    else:
        total = 0
        ti = 0
        for i in range(n):
            speed, tf = map(int, input().split())
            tf -= ti
            ti += tf
            total += speed * tf
        print(total, "miles")
