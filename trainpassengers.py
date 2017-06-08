c, n = map(int, input().split())
record = []
passenger = 0
impossible = False
for i in range(n):
  trainStop = list(map(int, input().split()))
  record.append(trainStop)
  passenger += trainStop[1]
  passenger -= trainStop[0]
  if trainStop[2] > 0 and passenger < c:
    impossible = True
    break
  if passenger < 0 or passenger > c:
    impossible = True
    break
if impossible == True or record[0][0] > 0 or record[-1][2] > 0 or record[-1][1] > 0 or passenger != 0:
  print('impossible')
else:
  print('possible')
