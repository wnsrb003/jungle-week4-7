
import sys
input = sys.stdin.readline

n, k = list(map(int, input().split()))
coin_lst = [int(input()) for _ in range(n)]

coin_cnt = 0
for coin_price in reversed(coin_lst) :
  if k // coin_price > 0:
    coin_cnt += k // coin_price
    k = k % coin_price 
  if k == 0 : 
    print(coin_cnt)
    break
    
    