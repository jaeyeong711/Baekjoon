_list = list(map(int, input().split()))
double = [x ** 2 for x in _list]
result = sum(double) % 10
print(result)