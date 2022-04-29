import sys
input = sys.stdin.readline

input_num_cnt = int(input())

dp_lst = [1 for _ in range(input_num_cnt)]
input_num =list(map(int, input().split()))

cnt = 0
for num_idx in range(input_num_cnt) :
  for comparing_num_idx in range(num_idx) : 
    if input_num[num_idx] > input_num[comparing_num_idx] : 
      dp_lst[num_idx] = max(dp_lst[num_idx], dp_lst[comparing_num_idx]+1)

print(max(dp_lst))