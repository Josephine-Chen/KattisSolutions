def sortNames(n):
  top = []
  bottom = []
  for i in range(n):
    name = input()
    if i % 2 == 0:
      top.append(name)
    else:
      bottom.append(name)
  print("\n".join(top))
  print("\n".join(bottom[::-1]))
setNum = 1
while True:
  n = int(input())
  if n == 0:
    break
  print("SET", setNum)
  sortNames(n)
  setNum += 1
