import sys
input = sys.stdin.readline

def solve(w):
    w = w.upper()
    _list = list(set(w))
    cnt = [w.count(i) for i in _list]

    if cnt.count(max(cnt)) == 1:
        return _list[cnt.index(max(cnt))]
    else:
        return '?'

W = input().strip('\n')
print(solve(W))