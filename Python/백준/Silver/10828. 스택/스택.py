def do(command):
    if 'push' in command:
        command = command.split()
        X = command[-1]
        stack.append(X)
        return
    if 'pop' in command:
        if stack:
            print(stack.pop())
        else:
            print(-1)
        return
    if 'size' in command:
        print(len(stack))
        return
    if 'empty' in command:
        if stack:
            print(0)
        else:
            print(1)
        return
    if 'top' in command:
        if stack:
            print(stack[-1])
        else:
            print(-1)

stack = []
N = int(input())
for _ in range(N):
    do(input())