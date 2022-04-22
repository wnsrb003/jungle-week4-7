#용량초과

input_cnt = int(input())

permutation_cnt_lst = [0]*1000001
permutation_cnt_lst[1] = 1
permutation_cnt_lst[2] = 2
for idx in range(input_cnt+1) :
  if idx > 2 : 
    permutation_cnt_lst[idx] = (permutation_cnt_lst[idx-1] + permutation_cnt_lst[idx-2])%15746

print(permutation_cnt_lst)

