#메모리 초과나서 안됨 -> dp 같은경우, 재귀 보다는 for문이 깔끔하고 좋은 것 같음.
import sys
sys.setrecursionlimit(10**6)

input_num = int(input())
dp = [0]*(input_num + 1)

def tile (input_num) : 
  if input_num == 1 : 
    return 1 
  elif input_num == 2 : 
    return 2
  elif dp[input_num] != 0 :
    return dp[input_num]
  dp[input_num] = (tile(input_num-1) + tile(input_num-2))%15746
  return dp[input_num] ##### 여기다가 dp[input_num]을 넣는게 중요하다고!!!!!!


print(tile(input_num))
     
