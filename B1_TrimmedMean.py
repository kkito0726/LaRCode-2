'''
URL: https://atcoder.jp/contests/abc291/tasks/abc291_b
AtCoder Beginner Contest 291（Sponsored by TOYOTA SYSTEMS）
B問題
'''

N = int(input())
tokuten = list(map(int, input().split()))

# print(N)
# print(tokuten)

tokuten.sort()

for i in range (N):
    tokuten.pop()

for i in range (N):
    tokuten.pop(0)

ave = sum(tokuten)/len(tokuten)

print(ave)
