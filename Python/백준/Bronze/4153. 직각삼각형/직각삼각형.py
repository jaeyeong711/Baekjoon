while 1:
    line = list(map(int, input().split()))
    if (line[0] == 0):
        break

    # 주어진 변의 길이가 삼각형이 될 수 없다면? 30000보다 작은 양수
    line.sort()
    if (line[0] + line[1] < line[2]):
        print("wrong")
        continue

    [a, b, c] = line


    # 세개 중 어느게 빗변이 되는지 모르는 상태가 아닌가?
    if (a*a + b*b == c*c):
        print("right")
    elif (b*b + c*c == a*a):
        print("right")
    elif (c*c + a*a == b*b):
        print("right")
    else:
        print("wrong")