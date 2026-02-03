gugudan = {i * j for i in range(1, 10) for j in range(1, 10)}

N = int(input())
print(1 if N in gugudan else 0)