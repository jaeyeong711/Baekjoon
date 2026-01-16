N = int(input())

# int(a) + int(a[0]) + ... + int(a[-1]) = N

result = 0

for i in range(1, 1000001):
    num = i
    i = str(i)

    for j in i:
        num += int(j)

    if (num == N):
        result = i
        break

print(result)