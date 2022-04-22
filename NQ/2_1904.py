import sys
sys.setrecursionlimit(9999999)

input_cnt = int(input())

permutation_cnt_lst = [0]*10000000
permutation_cnt_lst[1] = 1
permutation_cnt_lst[2] = 2



def find_permutation_cnt(n) : 
  if n == 1 : 
    return 1
  if n == 2 : 
    return 2

  if permutation_cnt_lst[n] != 0 : 
    return permutation_cnt_lst[n]
  permutation_cnt_lst[n] = find_permutation_cnt(n-1) + find_permutation_cnt(n-2)
  return permutation_cnt_lst[n]
print(find_permutation_cnt(input_cnt))