
input_num = int(input())

cnt = 0 
while True : 
  print(input_num, end=" ")
  if input_num % 3 == 0 : 
    input_num //= 3 
    cnt +=1
  elif ((input_num-1)//3 > 0) and ((input_num-1) % 3 == 0) : 
    input_num -=1
    input_num //= 3 
    cnt +=2
  elif input_num % 2 == 0 : 
    input_num //= 2
    cnt +=1
  elif input_num == 1 : 
    print("cnt :", cnt)
    break
  else : 
    input_num -= 1 
    cnt +=1
    
    

