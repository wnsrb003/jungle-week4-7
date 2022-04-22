import sys
input = sys.stdin.readline

n, k= map(int, input().split())
a = list(reversed([int(input()) for _ in range(n)]))
coin_cnt_lst = []

for coin_value in a : 
  if k//coin_value == 0 : 
    pass 
  else : 
    coin_cnt = k//coin_value
    k = k % coin_value 
    coin_cnt_lst.append(coin_cnt)

print(sum(coin_cnt_lst))