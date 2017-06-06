x = int(input())
n = int(input())
total = (n + 1) * x
for num in range(n):
  p = int(input())
  total -= p
print(total)
