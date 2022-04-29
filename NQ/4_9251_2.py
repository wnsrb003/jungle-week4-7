import sys
input = sys.stdin.readline

a_str = list((input().split())[0])
b_str = list((input().split())[0])
dp = [[0]*(len(a_str)+1) for _ in range(len(b_str)+1)]

for b_idx in range(1, len(b_str)+1) : 
  for a_idx in range(1, len(a_str)+1) :
    if b_str[b_idx-1] == a_str[a_idx-1] : 
      dp[b_idx][a_idx] = dp[b_idx-1][a_idx-1] + 1
    else : 
      dp[b_idx][a_idx] = max(dp[b_idx-1][a_idx], dp[b_idx][a_idx-1])

print(dp[-1][-1])
      
    
    

