'''
URL: https://atcoder.jp/contests/abc291/tasks/abc291_b
AtCoder Beginner Contest 291（Sponsored by TOYOTA SYSTEMS）
B問題
'''

n = int(input())  # nは入力回数
num_list = [int(i) for i in input().split()]

list_sort = sorted(num_list)
all = len(num_list)

average = sum(list_sort[n:all-n])/len(list_sort[n:all-n])
print(average)

