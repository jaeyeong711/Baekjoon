import sys
input = sys.stdin.readline

def is_palindrome(n):
    n = str(n)
    if n == n[::-1]:
        return 'yes'
    return 'no'

while True:
    N = int(input())
    if N == 0:
        break

    print(is_palindrome(N))