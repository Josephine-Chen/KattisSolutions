x, y, n = map(int, input().split())
for num in range(1, n + 1):
  if (num % x == 0) and (num % y == 0):
    print('FizzBuzz')
  elif num % x == 0:
    print('Fizz')
  elif num % y == 0:
    print('Buzz')
  else: 
    print(num)
