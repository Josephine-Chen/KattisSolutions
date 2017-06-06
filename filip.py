n = input()
a = int(n.split()[0][::-1])
b = int(n.split()[1][::-1])
if a > b:
  print(a)
else:
  print(b)
