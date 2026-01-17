import sys
input = sys.stdin.readline

def is_group(w):
    _list = list(set(w))
    cnt = [0 for _ in range(len(_list))]

    for i in range(len(_list)):
        j = 0
        while w[w.index(_list[i]) + j] == _list[i] :
            cnt[i] += 1
            if w.index(_list[i]) + j + 1== len(w):
                break
            j += 1

    for i in range(len(_list)):
        if cnt[i] != w.count(_list[i]):
            return 0

    return 1


N = int(input())
total = 0
for _ in range(N):
    W = input().strip('\n')
    total += is_group(W)
print(total)