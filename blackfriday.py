n = int(input())
p = list(map(int, input().split()))
index = -1
for i in range(6, 0, -1):
  if p.count(i) == 1:
    index = p.index(i) + 1
    print(index)
    break
if index == -1:
  print('none')
