
import math
input_num = int(input())
dp_lst = [0, 0, 1, 1, 2]


for idx in range(5, input_num+1) : 
  a, b, c = math.inf, math.inf, dp_lst[idx-1]
  
  if idx%3 == 0 : 
    a = dp_lst[idx//3]
  if idx%2 == 0 : 
    b = dp_lst[idx//2]
  dp_lst.append(min(a,b,c)+1)

print(dp_lst[input_num])


  
  
  
  


