import sys
input = sys.stdin.readline

t = int(input())

for t_idx in range(t) :
    n = int(input())
    coin_lst = list(map(int, input().split()))
    m = int(input())
    dp = [0 for _ in range(m+1)]
    dp[0] = 1
    
    for coin in coin_lst :
        for m_idx in range(coin, m+1) : 
            dp[m_idx] += dp[m_idx - coin] 
    print(dp[-1])
    
            
            
            
        
            
            
    





