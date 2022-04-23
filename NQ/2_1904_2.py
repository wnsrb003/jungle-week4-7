from collections import deque
input_cnt = int(input())
q = deque([1, 2])

if input_cnt == 1 : 
  print(1)
elif input_cnt == 2 :
  print(2)
else : 
  for idx in range(input_cnt+1) :  
    if idx > 2 : 
      first_value = q.popleft()
      second_value = q[0]
      new_value = (first_value + second_value)%10
      q.append(new_value)
      print(new_value)

  
    
  

  

