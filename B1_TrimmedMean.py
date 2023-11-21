'''
URL: https://atcoder.jp/contests/abc291/tasks/abc291_b
AtCoder Beginner Contest 291（Sponsored by TOYOTA SYSTEMS）
B問題
'''
import numpy as np
N = int(input())
num_list = list(map(int, input().split()))
list_2 = sorted(num_list)
del list_2[0:N]
del list_2[-N:] 
ave = np.mean(list_2)
print(ave)