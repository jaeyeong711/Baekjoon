import sys
input = sys.stdin.readline

N = int(input())
p_list = [tuple(input().split()) for _ in range(N)]
p_list.sort(key = lambda x: int(x[0]))

for age, name in p_list:
    print(age, name)