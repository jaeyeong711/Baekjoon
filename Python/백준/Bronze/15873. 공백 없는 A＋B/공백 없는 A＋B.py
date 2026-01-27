import sys
input = sys.stdin.readline

nums = input()
if '10' in nums:
    if nums == '1010\n':
        print(20)
    else:
        nums = nums.replace('10', '')
        print(10 + int(nums))
else:
    print(int(nums[0]) + int(nums[1]))