nums = [1]
for i in range(2, 10):
    for j in range(10):
        nums.append(i * j)
nums = set(nums)

N = int(input())
if N in nums:
    print(1)
else:
    print(0)