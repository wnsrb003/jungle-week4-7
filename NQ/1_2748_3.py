


input_num = int(input())
fibo_lst = [0, 1]

for idx in range(2,input_num+1) : 
  fibo_lst.append(fibo_lst[idx-1] + fibo_lst[idx-2])
print(fibo_lst[-1])
  

