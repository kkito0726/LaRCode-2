'''
URL: https://atcoder.jp/contests/abc284/tasks/abc284_a
AtCoder Beginner Contest 284
A問題
'''
#入力
N = int(input())
name = [input() for _ in range(N)]
#出力
for i in range(N):
    print(name[(N-1)-i])
