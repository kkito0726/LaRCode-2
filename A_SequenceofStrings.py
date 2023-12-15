'''
URL: https://atcoder.jp/contests/abc284/tasks/abc284_a
AtCoder Beginner Contest 284
A問題
'''
n = int(input())  # nはint型
str_list = [input() for _ in range(n)]


for i in range(n-1, -1, -1) :
    print(str_list[i])
