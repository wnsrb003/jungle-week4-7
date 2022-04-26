import sys
input = sys.stdin.readline

first_input = list(input())[:-1]
second_input = list(input())[:-1]

dp = [[0]*(len(first_input)+1) for idx in range(len(second_input)+1)]


for second_idx in range(len(second_input)) : 
  for first_idx in range(len(first_input)) : 
    if second_input[second_idx] == first_input[first_idx]: 
      dp[second_idx+1][first_idx+1] = dp[second_idx][first_idx] + 1
    else : 
      dp[second_idx+1][first_idx+1] = max(dp[second_idx+1][first_idx], dp[second_idx][first_idx+1])

print(dp[-1][-1])
      
      
