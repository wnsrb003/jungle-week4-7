import sys
input = sys.stdin.readline

first_input = list(input())
second_input = list(input())

cnt = 0
second_str_int = 0
for first_single_str in first_input : 
  for second_single_str_int in range(second_str_int, len(second_input)) : 
    if first_single_str == second_input[second_single_str_int] :
      second_str_int = second_input.index(first_single_str)
      print(first_single_str)
      cnt +=1
      break
    
print(cnt)

