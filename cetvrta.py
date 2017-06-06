xcoords = []
ycoords = []
for i in range(3):
  x, y = map(int, input().split())
  if x not in xcoords:
    xcoords.append(x)
  elif x in xcoords:
    xcoords.remove(x)
  if y not in ycoords:
    ycoords.append(y)
  elif y in ycoords:
    ycoords.remove(y)
print(xcoords[0], ycoords[0])
