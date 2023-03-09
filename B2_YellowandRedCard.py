'''
URL: https://atcoder.jp/contests/abc292/tasks/abc292_b
AtCoder Beginner Contest 292
B問題
'''

N, Q = map(int, input().split())
events = [list(map(int, input().split())) for _ in range(Q)]

players = [0 for _ in range(N)]

for event in events:
    idx = event[1] - 1
    if event[0] == 1:
        players[idx] += 1
    if event[0] == 2:
        players[idx] += 2
    if event[0] == 3:
        if players[idx] < 2:
            print("No")
        else:
            print("Yes")
