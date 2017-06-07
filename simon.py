n = int(input())
for i in range(n):
    command = input()
    if command.startswith('simon says'):
        print(command[11:])
