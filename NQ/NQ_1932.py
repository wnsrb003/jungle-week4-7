
import sys
input = sys.stdin.readline

input_cnt =int((input().split())[0])

dp_t = [list(map(int,(input().split()))) for _ in range(input_cnt)]

for row_idx in range(1, input_cnt) : 
  for col_idx in range(row_idx+1) :

    if col_idx == 0 :
      dp_t[row_idx][col_idx] = dp_t[row_idx][col_idx] + dp_t[row_idx-1][col_idx]
    elif col_idx == row_idx :
      dp_t[row_idx][col_idx] = dp_t[row_idx][col_idx] + dp_t[row_idx-1][col_idx-1]
    else : 
      dp_t[row_idx][col_idx] = max(dp_t[row_idx][col_idx] + dp_t[row_idx-1][col_idx], dp_t[row_idx][col_idx] + dp_t[row_idx-1][col_idx-1])
print(max(dp_t[-1]))