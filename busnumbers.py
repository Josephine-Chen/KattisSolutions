n = int(input())
buses = sorted(list(map(int, input().split())))
shortest = list()
curr = 0
while curr < n:
  look = curr
  while look < n - 1 and buses[look + 1] - buses[look] == 1:
    look += 1
  if curr < look - 1:
    shortest.append('{}-{}'.format(buses[curr], buses[look]))
    curr = look + 1
  else:
    shortest.append(str(buses[curr]))
    curr += 1
print(' '.join(shortest))
