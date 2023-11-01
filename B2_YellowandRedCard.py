'''
URL: https://atcoder.jp/contests/abc292/tasks/abc292_b
AtCoder Beginner Contest 292
B問題
'''

N, Q = map(int, input().split())
event = []
for i in range(Q):
    event.append(list(map(int, input().split())))

state = [0 for _ in range(N)]
for i in range(Q):
    if event[i][0] == 1:
        state[event[i][1] - 1] += 1
    elif event[i][0] == 2:
        state[event[i][1] - 1] += 2
    elif event[i][0] == 3:
        if state[event[i][1] - 1] >= 2:
            print('Yes')
        else:
            print('No')
