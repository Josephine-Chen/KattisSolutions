n = int(input())
temps = [int(nums) for nums in input().split()] 
# Can also use map but slower by .01 s
# temps = map(int, input().split())
count = 0
for temp in temps:
    if temp < 0:
        count += 1
print(count)
