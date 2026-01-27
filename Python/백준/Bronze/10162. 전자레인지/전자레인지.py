import sys
input = sys.stdin.readline

button = [5 * 60, 60, 10]
count = [0, 0, 0]

T = int(input())

if T % button[2] != 0:
    print(-1)
else:
    for i in range(len(button)):
        count[i] = T // button[i]
        T -= button[i] * count[i]
    print(' '.join(list(map(str, count))))