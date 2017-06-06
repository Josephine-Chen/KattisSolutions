check = []
for x in range(10):
  num = int(input())
  mod = num % 42
  if mod not in check:
    check.append(mod)
print(len(check))
