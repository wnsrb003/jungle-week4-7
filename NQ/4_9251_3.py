
str_a = list(input())
str_b = list(input())

dp_t = [[0]*(len(str_b)+1) for _ in range(len(str_a)+1)]

for str_a_idx in range(1, len(str_a)+1) :
  for str_b_idx in range(1, len(str_b)+1) :
    if str_a[str_a_idx-1] == str_b[str_b_idx-1] : 
      dp_t[str_a_idx][str_b_idx] = dp_t[str_a_idx-1][str_b_idx-1] + 1
    else : 
      
      dp_t[str_a_idx][str_b_idx] = max(dp_t[str_a_idx-1][str_b_idx], dp_t[str_a_idx][str_b_idx-1])

print(dp_t[-1][-1])