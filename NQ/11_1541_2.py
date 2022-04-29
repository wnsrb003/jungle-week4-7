import re
from collections import deque
input_expression = input()

int_lst = deque(re.split(r'[+, -]', input_expression))
sign_lst = [ list_object for list_object in list(input_expression) if (list_object == "+") or (list_object == "-")]
sum_int = int(int_lst[0])
int_lst.popleft()
cnt = 0
while sign_lst[cnt] == "+" : 
  sum_int += int(int_lst.popleft())
  cnt += 1

left_lst = list(map(int, int_lst))
sum_int -= sum(list(map(int, int_lst)))
print(sum_int)

