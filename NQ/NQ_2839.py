

w = int(input())

bag_lst = [3, 5]
dp = [0 for _ in range(w+1)]
dp[0] = 1


for bag in bag_lst : 
  for w_idx in range(bag, w+1) : 
    dp[w_idx] += dp[w_idx-bag]
if dp[-1] == 0 : 
  print(-1)
else : 
  max_five_bag = w//bag_lst[1]
  while True : 
    left_w = w - max_five_bag*bag_lst[1]
    if left_w % bag_lst[0] == 0 :
      print(max_five_bag + (left_w//bag_lst[0]))
      break
    else : 
      max_five_bag -= 1
      
      
      
      
    
    
    
    
  
  
    
    
    
    
  