'''
URL: https://atcoder.jp/contests/abc284/tasks/abc284_a
AtCoder Beginner Contest 284
A問題
'''
n = int(input())  # nは入力回数
str_list = [input() for _ in range(n)]

for i in range(n):
    print(str_list[n-i-1])
