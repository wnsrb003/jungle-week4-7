import sys
input = sys.stdin.readline

n, k = map(int, input().split())
input_lst = [list(map(int, input().split())) for _ in range(n)]
dp = [[0]*(k+1) for _ in range(n+1)]

for n_idx in range(1, n+1) : 
  for k_idx in range(1, k+1) : 
    if k_idx >= input_lst[n_idx-1][0] : 
      dp[n_idx][k_idx] = max(dp[n_idx-1][k_idx], dp[n_idx-1][k_idx-input_lst[n_idx-1][0]]+input_lst[n_idx-1][1])
    else : 
      dp[n_idx][k_idx] = dp[n_idx-1][k_idx]
print(dp[-1][-1])