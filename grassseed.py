c = float(input())
l = int(input())
sum = 0
for lawns in range(l):
  width, length = map(float, input().split())
  sum += width * length * c
print(float(sum))
