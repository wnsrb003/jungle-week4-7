import sys
input = sys.stdin.readline

n, k = map(int, input().split())
p_lst = [list(map(int, input().split())) for _ in range(n)]
dp_t = [[0]*(k+1) for _ in range(n+1)]

for n_idx in range(1, n+1) :
  for k_idx in range(1, k+1) :
    if k_idx >= p_lst[n_idx-1][0] :
      dp_t[n_idx][k_idx] = max(dp_t[n_idx-1][k_idx-p_lst[n_idx-1][0]]+p_lst[n_idx-1][1], dp_t[n_idx-1][k_idx])
    else : 
      dp_t[n_idx][k_idx] = dp_t[n_idx-1][k_idx]

print(dp_t[-1][-1])
