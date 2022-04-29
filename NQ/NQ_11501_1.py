import sys
input = sys.stdin.readline

tc_cnt = int((input().split())[0])

for idx in range(tc_cnt) : 
  stock_cnt = int((input().split())[0])
  stock_lst = list(map(int, input().split()))
  total_profit = 0
  max_price = 0
  
  for stock_idx in range(len(stock_lst)-1, -1, -1) : 
    if max_price < stock_lst[stock_idx] : 
      max_price = stock_lst[stock_idx]
    else : 
      total_profit += (max_price - stock_lst[stock_idx])
  print(total_profit)
    
  