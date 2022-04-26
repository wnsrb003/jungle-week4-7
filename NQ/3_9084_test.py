import sys
input = sys.stdin.readline


tc_count = int(input())

for tc_idx in range(tc_count) : 
  n = int(input()) 
  coin_lst = list(map(int, input().split()))
  m = int(input())
  price_lst = [0 for _ in range(m+1)]
  price_lst[0] = 1
  
  for coin in coin_lst :
    for m_idx in range(coin, m+1) : 
      price_lst[m_idx] += price_lst[m_idx-coin]
    
  print(price_lst[-1])
  


  
