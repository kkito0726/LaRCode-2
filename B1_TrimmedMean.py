'''
URL: https://atcoder.jp/contests/abc291/tasks/abc291_b
AtCoder Beginner Contest 291（Sponsored by TOYOTA SYSTEMS）
B問題
'''

N = int(input())
X = list(map(int, input().split()))

score_list = sorted(X)
for i in range(N):
    del score_list[0]
    del score_list[-1]
total = 0
a = 3*N
for i in range(a):
    total += score_list[i]
average = total / a
print(average)