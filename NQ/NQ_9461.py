

tc_cnt = int(input())
dp_t = [1,1,1]

for tc_idx in range(tc_cnt) :
  input_num = int(input())
  dp_t = [1,1,1] 
  for idx in range(3, input_num) : 
    dp_t.append(dp_t[idx-2] + dp_t[idx-3])

  print(dp_t[input_num-1])

  
  
  