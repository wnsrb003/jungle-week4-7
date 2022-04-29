tc_cnt = int(input())

for _ in range(tc_cnt) : 
  input_num = int(input())
  if input_num == 1 or input_num == 0 : 
    dp_table = [[1, 0], [0, 1]]
  elif input_num > 1 : 
    dp_table = [[0,0]for _ in range(input_num+1)]
    dp_table[0] = [1, 0]
    dp_table[1] = [0, 1]
    for fibo_num in range(2, input_num+1) : 
      dp_table[fibo_num] = [dp_table[fibo_num-1][0]+dp_table[fibo_num-2][0], dp_table[fibo_num-1][1]+dp_table[fibo_num-2][1]]
  print(dp_table[input_num][0], dp_table[input_num][1])
    
  