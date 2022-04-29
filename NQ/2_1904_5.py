

## 4 : 30 
input_num = int(input())
tile_cnt_lst = [1, 2]

if input_num >= 2 :
  for idx in range(2, input_num) :
    tile_cnt_lst.append((tile_cnt_lst[idx-1] + tile_cnt_lst[idx-2])%15746)

print(tile_cnt_lst[input_num-1]) 



