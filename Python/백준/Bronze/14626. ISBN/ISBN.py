def solve(isbn):
    index = isbn.find('*')

    isbn = isbn.replace('*', '0')
    isbn = [int(isbn[i]) if i % 2 == 0 else int(isbn[i]) * 3 for i in range(len(isbn))]

    if sum(isbn) % 10 == 0:
        return 0

    if index % 2 == 0:
        return 10 - (sum(isbn) % 10)
    else:
        for i in range(1, 10):
            if (i * 3 + sum(isbn)) % 10 == 0:
                return i


ISBN = input()
print(solve(ISBN))