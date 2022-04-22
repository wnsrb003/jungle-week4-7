import sys
import re
from collections import deque
input = sys.stdin.readline

input_formula = deque(list((input().split())[0]))
input_len = len(input_formula)
parsed_input = []####
idx = 0

while idx < input_len : 
  idx += 1
  new_input = input_formula.popleft()
  if (new_input in ['+', '-']) or (len(parsed_input) == 0) or (parsed_input[-1] in ['+', '-']): 
    parsed_input.append(new_input)
  else : 
    parsed_input[-1] = parsed_input[-1]+ new_input
    
print(parsed_input)