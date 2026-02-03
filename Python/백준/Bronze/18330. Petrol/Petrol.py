n = int(input())
k = int(input())
money = n * 1500 if (k + 60) > n else (k + 60) * 1500 + (n - (k + 60)) * 3000
print(money)