'''
URL: https://atcoder.jp/contests/abc284/tasks/abc284_a
AtCoder Beginner Contest 284
A問題
'''
N = int(input())
str_list = [input() for _ in range(N)]

for i in range(N):
    print(str_list[N-1])
    N -= 1