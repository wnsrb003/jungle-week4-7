import sys
input = sys.stdin.readline


tc_cnt = int(input())
for tc_int in range(tc_cnt) : 
  num_cnt = int(input())
  cnt = 1
  input_lst = []
  for _ in range(num_cnt) : 
    input_lst.append(list(map(int, input().split())))
  input_lst.sort()
  comparing_num = input_lst[0][1]
  for input_idx in range(len(input_lst)) :
    if comparing_num > input_lst[input_idx][1] : 
      cnt +=1
      comparing_num = input_lst[input_idx][1]
  print(cnt)
      
    
