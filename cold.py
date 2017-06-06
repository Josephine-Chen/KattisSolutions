n = int(input())
temps = [int(nums) for nums in input().split()]
count = 0
for temp in temps:
    if temp < 0:
        count += 1
print(count)
