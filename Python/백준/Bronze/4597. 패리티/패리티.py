def solve(bit):
    cnt = 0
    if bit[-1] == 'e':
        for bin in bit:
            if bin == '1':
                cnt += 1
        if cnt % 2 == 0:
            return bit.replace('e', '0')
        else:
            return bit.replace('e', '1')
    elif bit[-1] == 'o':
        for bin in bit:
            if bin == '1':
                cnt += 1
        if cnt % 2 == 1:
            return bit.replace('o', '0')
        else:
            return bit.replace('o', '1')


while True:
    bit = input()
    if bit == '#':
        break
    print(solve(bit))