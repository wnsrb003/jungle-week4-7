#220426 다시 풀어보기 

input_num  = int(input())
dp = [0]*(input_num+1)

def fibo(input_num) : 
  if input_num == 1 or input_num == 2 : 
    return 1 
  if dp[input_num] != 0 :
    return dp[input_num]
  dp[input_num] =  fibo(input_num - 1) + fibo(input_num -2) 
  return dp[input_num]
print(fibo(input_num))
    
