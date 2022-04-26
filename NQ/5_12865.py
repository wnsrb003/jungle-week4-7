import sys
input = sys.stdin.readline
w_v_lst = []

n, k = map(int, input().split())
dp_lst = [[0]*(k+1) for _ in range(n+1)]

w_v_lst = [list(map(int, input().split())) for _ in range(n)]
for n_idx in range(1, n+1) : 
  for k_idx in range(1, k+1) : 
    if k_idx >= w_v_lst[n_idx-1][0] : 
      dp_lst[n_idx][k_idx] = max(dp_lst[n_idx-1][k_idx], (dp_lst[n_idx-1][k_idx-w_v_lst[n_idx-1][0]]+ w_v_lst[n_idx-1][1]))
    else : 
      dp_lst[n_idx][k_idx] = dp_lst[n_idx-1][k_idx]

print(dp_lst[-1][-1])
