#연속으로 출력된 세 개의 문자열 중 하나는 반드시 Fizz가 포함되어 있음
FizzBuzz = [input() for _ in range(3)]
index_F = -1
index_FB = -1
if 'Fizz' in FizzBuzz:
    index_F = FizzBuzz.index('Fizz')
else:
    index_FB = FizzBuzz.index('FizzBuzz')

if index_FB == 0:
    print('Fizz')
else:
    for i, _str in enumerate(FizzBuzz):
        if i == index_F or i == index_FB:
            continue
        if _str != 'Buzz':
            n = int(_str)
            index_N = i
            break
    n = n + (3 - index_N)
    if n % 3 == 0 and n % 5 == 0:
        print("FizzBuzz")
    elif n % 3 == 0:
        print("Fizz")
    elif n % 5 == 0:
        print("Buzz")
    else:
        print(n)