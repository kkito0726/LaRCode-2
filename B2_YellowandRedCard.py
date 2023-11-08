'''
URL: https://atcoder.jp/contests/abc292/tasks/abc292_b
AtCoder Beginner Contest 292
B問題
'''
#入力
N,Q = map(int,input().split())
event = []
for i in range(Q):
    event.append(list(map(int,input().split())))
#出力
#空のリスト作り
j =[0 for _ in range(N)]
#空のリストにそれぞれYellow,Redを入れてる
for q in range(Q):
    for p in range(N):
        if event[q][1] == p+1:
            if event[q][0] == 1:
                j[p] += 1
            if event[q][0] == 2:
                j[p] += 2    
    if event[q][0] == 3:
            if j[event[q][1]-1] >= 2:
                print('Yes')
            else :
                print('No')
