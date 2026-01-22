seat_info = list(map(int, input().split()))
total = seat_info[0] * seat_info[1] + seat_info[2] * seat_info[3]
print(total)