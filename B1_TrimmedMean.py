'''
URL: https://atcoder.jp/contests/abc291/tasks/abc291_b
AtCoder Beginner Contest 291（Sponsored by TOYOTA SYSTEMS）
B問題
'''
N = int(input())
X = list(map(int, input().split()))

X.sort()

ans = 0

for i in range(N, 5*N-N):
    ans += X[i]

ave = ans/(3*N)
print(ave)

