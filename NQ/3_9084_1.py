import sys
input = sys.stdin.readline

t = int(input())

for t_idx in range(t) : 
  n = int(input())
  coin_lst =  list(map(int, input().split()))
  p = int(input())
  dp_lst = [0 for _ in range(p+1)]
  dp_lst[0] = 1
  for coin_price in coin_lst : 
    for price in range(coin_price, p+1) :
        dp_lst[price] += dp_lst[price-coin_price]
  print(dp_lst[-1])
        
    
    
    
    
    
    
    
  