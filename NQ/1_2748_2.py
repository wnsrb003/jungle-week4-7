
input_num = int(input())
dp = [0,1]

for idx  in range(input_num+1) : 
  if idx >= 2 :
    dp.append(dp[idx-1] + dp[idx-2])
print(dp[-1])
    