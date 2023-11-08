'''
URL: https://atcoder.jp/contests/abc291/tasks/abc291_b
AtCoder Beginner Contest 291（Sponsored by TOYOTA SYSTEMS）
B問題
'''
#入力
N = int(input())
S =list(map(int, input(). split()))
#出力
for i in range(N):
    S.remove(max(S))
for n in range(N):
    S.remove(min(S))
S_sum = sum(S)
print(S_sum/len(S))