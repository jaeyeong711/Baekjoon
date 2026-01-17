import sys
input = sys.stdin.readline

def is_leap(Y):
    if (Y % 4 == 0) and (Y % 100 != 0):
        return 1
    elif (Y % 400 == 0):
        return 1
    else:
        return 0

Y = int(input())
print(is_leap(Y))