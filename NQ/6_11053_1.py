
input_cnt = int(input())
num_lst = list(map(int, input().split()))
dp_t = [1 for _ in range(input_cnt)]

for num_idx in range(1, len(num_lst)) :
  for num_cycle in range(num_idx) :
    if num_lst[num_idx] >  num_lst[num_cycle] :
      dp_t[num_idx] = max(dp_t[num_idx], dp_t[num_cycle]+1)
print(max(dp_t))
      
    