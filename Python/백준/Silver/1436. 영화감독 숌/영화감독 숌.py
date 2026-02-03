N = int(input())
title = []
for n in range(N):
    if '6666' in str(n * 1000 + 666):
        if '66666' in str(n * 1000 + 666):
            if '666666' in str(n * 1000 + 666):
                for i in range(1000):
                    title = title + [n * 1000 + i]
                continue
            for i in range(100):
                title = title + [n * 1000 + 600 + i]
            continue
        for i in range(10):
            title = title + [n * 1000 + 660 + i]
        continue
    title = title + [n * 1000 + 666]
print(title[N-1])