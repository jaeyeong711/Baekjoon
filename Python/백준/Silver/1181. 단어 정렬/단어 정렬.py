N = int(input())
word = []
for i in range(N):
    word.append(input())

word = set(word)
word = list(word)

word.sort(key = lambda x: (len(x), x))

for i in range(len(word)):
    print(word[i])