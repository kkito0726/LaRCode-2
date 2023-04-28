'''
URL: https://atcoder.jp/contests/abc292/tasks/abc292_b
AtCoder Beginner Contest 292
B問題
'''

N, Q = map(int, input().split())
events = [list(map(int, input().split())) for _ in range(Q)]

player = [0 for _ in range(N)]
yellow_c = [0 for _ in range(N)]

judge = [False for _ in range(N)]

for event in events:
    A, B = event
    
    if A == 1:
        if yellow_c[B-1] == 0:
            yellow_c[B-1] += 1
            
            continue

        else:
            judge[B-1] = True

    elif  A == 2:
        judge[B-1] = True
            
    else:
        if judge[B-1] == True:
            print("Yes")
        else:
            print("No")
