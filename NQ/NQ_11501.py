
import sys
input = sys.stdin.readline

tc_cnt = int((input().split())[0])

for idx in range(tc_cnt) : 
  stock_cnt = int((input().split())[0])
  stock_lst = list(map(int, input().split()))
  total_profit = 0
  f = True
  while f : 
    max_price = max(stock_lst)
    for stock_idx in range(len(stock_lst)) :
      if stock_lst[stock_idx] == max_price : 
        if stock_idx + 1 == len(stock_lst) : 
          f = False
        else : 
          stock_lst = stock_lst[stock_idx+1:]
          break
      else : 
        total_profit += (max_price - stock_lst[stock_idx])
  print(total_profit)
      
  