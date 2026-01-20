import sys
input = sys.stdin.readline

N = int(input())
p_list = [tuple(input().split()) for _ in range(N)]
p_list.sort(key = lambda x: int(x[0]))

for i in range(N):
    print(p_list[i][0], p_list[i][1])