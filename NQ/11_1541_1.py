import sys
from collections import deque
input = sys.stdin.readline

input_formula_lst = list((input().split())[0])
input_len = len(input_formula_lst)
cnt_minus = 0
for value_idx in range(len(input_formula_lst)) :
  if input_formula_lst[value_idx] == '-' : 
    cnt_minus += 1
    if cnt_minus == 1 : 
      input_formula_lst[value_idx] = '-('
    else : 
      input_formula_lst[value_idx] = ')-('
  if (value_idx == (len(input_formula_lst)-1)) and(cnt_minus > 0 ): 
    input_formula_lst.append(")")

idx = 0
input_q = deque(list("".join(input_formula_lst)))
input_len = len(input_q)
parsed_input = []
while idx < input_len : 
  idx += 1
  new_input = input_q.popleft()
  if (new_input in ['+', '-', '(', ')']) or (len(parsed_input) == 0) or (parsed_input[-1] in ['+', '-', '(', ')']): 
    parsed_input.append(new_input)
  else : 
    parsed_input[-1] = parsed_input[-1]+ new_input
for idx in range(len(parsed_input)) :
  try : 
    parsed_input[idx] = str(int(parsed_input[idx]))
  except : 
    pass

print(eval("".join(parsed_input))) ## eval는 string을 계산해주는 함수 

    
    
  