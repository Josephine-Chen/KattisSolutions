l = int(input())
d = int(input())
x = int(input())
while sum(map(int, str(l))) != x:
  l += 1
print(l)
while sum(map(int, str(d))) != x:
  d -= 1
  if d == l:
    break
print(d)
