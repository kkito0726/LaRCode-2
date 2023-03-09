'''
URL: https://atcoder.jp/contests/abc291/tasks/abc291_b
AtCoder Beginner Contest 291（Sponsored by TOYOTA SYSTEMS）
B問題
'''

N = int(input())
points = list(map(int, input().split()))
 
points.sort()
 
sum = 0
for i in range(N, 5*N - N):
  sum += points[i]
  
ave = sum / (5*N - 2*N)
print(ave)