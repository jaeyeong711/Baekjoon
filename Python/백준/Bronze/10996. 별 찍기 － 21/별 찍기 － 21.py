N = int(input())

if N == 1:
    print("*")
elif (N % 2 == 0):
    for i in range(N):
        print("* " * (N // 2))
        print(" *" * (N // 2))
else:
    for i in range(N):
        print("* " * (N // 2 + 1))
        print(" *" * (N // 2))