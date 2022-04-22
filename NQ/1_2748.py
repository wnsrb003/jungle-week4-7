

input_num = int(input())
fibo_result_lst = [0, 1]


for idx in range(input_num+1) : 
  if idx > 1 : 
    fibo_result_lst.append(fibo_result_lst[idx-1] + fibo_result_lst[idx-2])

print(fibo_result_lst[-1])
    
    

 