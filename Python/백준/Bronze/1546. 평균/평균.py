import sys
input = sys.stdin.readline

N = int(input())
scores = list(map(int, input().split()))
max_score = max(scores)

scores = [x / max_score * 100 for x in scores]
print(sum(scores) / len(scores))