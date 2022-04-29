input_num = int(input())
dp = [1,2]

if input_num == 1 or input_num == 2 :
  print(dp[input_num-1])
else :
  for idx in range(input_num) : 
    if idx >= 2 : 
      dp.append((dp[idx-1] + dp[idx-2])%15746)
  print(dp[-1])