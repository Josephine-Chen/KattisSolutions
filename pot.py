n = int(input())
x = 0
for num in range(n):
    p = input()
    
    x += int(p[:-1]) ** int(p[-1])
print(x)
