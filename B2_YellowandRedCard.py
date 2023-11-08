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
j =[[] for _ in range(N)]
#空のリストにそれぞれYellow,Redを入れてる
for q in range(Q):
    for p in range(N):
        if event[q][1] == p+1:
            if event[q][0] == 1:
                j[p].append('Yellow')
            if event[q][0] == 2:
                j[p].append('Red')    
    if event[q][0] == 3:
            if len(j[event[q][1]-1]) == 2 or j[event[q][1]-1] == ['Red']:
                print('Yes')
            else:
                print('No')
print(j)

