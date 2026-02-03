import sys
input = sys.stdin.readline

def search(nums, find):
    exists = set(nums) & set(find)
    unexists = set(find) - set(nums)
    
    if len(exists) >= len(unexists):
        _list = ['0' if n in unexists else '1' for n in find]
    else:
        _list = ['1' if n in exists else '0' for n in find]
    print('\n'.join(_list))



N = int(input())
nums = list(map(int, input().split()))
M = int(input())
find_nums = list(map(int, input().split()))

search(nums, find_nums)