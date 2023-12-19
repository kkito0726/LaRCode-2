'''
URL: https://atcoder.jp/contests/abc291/tasks/abc291_b
AtCoder Beginner Contest 291（Sponsored by TOYOTA SYSTEMS）
B問題
'''
n = int(input())  # nはint型
num_list = list(map(int, input().split()))  # n個の数字がリストに格納される

for i in range(n) :


  num_list.remove(max(num_list))
  num_list.remove(min(num_list))


score = sum(num_list) / len(num_list)

print(score)