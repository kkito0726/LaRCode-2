'''
URL: https://atcoder.jp/contests/abc292/tasks/abc292_b
AtCoder Beginner Contest 292
B問題
'''
N , Q = map(int, input().split())
a, b = [], []
for _ in range(Q):
    syurui , num = map(int, input().split())
    a.append(syurui)
    b.append(num)
score = []
for _ in range(N):
    score.append(0)
for i in range(Q):
    if a[i] == 1:
        score[b[i]-1] += 1
    if a[i] == 2:
        score[b[i]-1] += 2
    if a[i] == 3:
        if score[b[i]-1] <= 1:
            print("No")
        else:
            print("Yes")