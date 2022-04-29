
#f(n, k) = f(n-1, k) + f(n, k-D(n))

from lib2to3.pgen2.pgen import DFAState
import sys
input = sys.stdin.readline

tc_cnt = int(input())

for _ in range(tc_cnt) : 
  coin_cnt = int(input())
  coin_lst = list(map(int, input().split()))
  total_price = int(input())
  dp_t = [0 for _ in range(total_price+1)]
  dp_t[0] = 1
  
  for coin_price in coin_lst :
    for price_idx in range(coin_price, total_price+1) : 
      dp_t[price_idx] += dp_t[price_idx-coin_price]

  print(dp_t[-1])
  