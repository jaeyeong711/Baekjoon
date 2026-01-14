import sys
input = sys.stdin.readline

while True:
    line = sorted(map(int, input().split()))
    if (line[0] == 0):
        break

    [a, b, c] = line

    if (a*a + b*b == c*c):
        print("right")
    else:
        print("wrong")