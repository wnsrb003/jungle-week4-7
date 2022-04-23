import sys
sys.stdin = open('input.txt')

T = int(sys.stdin.readline().strip())
for _ in range(T):
    N = int(sys.stdin.readline().strip())
    test = []
    for _ in range(N):
        x, y = map(int, sys.stdin.readline().strip().split())
        
        test.append((x, y))
    
    cnt = 1
    test.sort()
    max_b = test[0][1]
    for j in range(1, len(test)):
        if test[j][1] < max_b:
            max_b = test[j][1]
            cnt += 1
    
    
    print(cnt)
    