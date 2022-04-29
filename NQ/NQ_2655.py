
import sys
input = sys.stdin.readline

brick_cnt = int((input().split())[0])
dp_lst = [[0]*(brick_cnt) for _ in range(brick_cnt)]
brick_lst = []
bottom_area_lst = []
print(dp_lst)

for idx in range(brick_cnt) : 
  new_brick = list(map(int, input().split()))
  new_brick.append(idx+1)
  brick_lst.append(new_brick)

brick_lst.sort(reverse=True, key=lambda x:x[2])
max = 0
for start_idx in range(brick_cnt) :
  for brick_idx in range(start_idx, brick_cnt+1) :
    if start_idx > max :
      max
    dp_lst[start_idx][brick_idx] = 
  


print(brick_lst)

