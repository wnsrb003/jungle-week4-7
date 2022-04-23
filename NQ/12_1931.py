


import sys
input = sys.stdin.readline
schedule_lst = []
schedule_finishing_time_lst = []
schedule_dict = {}


def find_next_finishing_time (pre_endtime) : 
  try : 
    next_finishing_time_idx = schedule_finishing_time_lst[schedule_finishing_time_lst.index(pre_endtime) + 1]
  except : 
    return "finish"
  while True : 
    try : 
      print("debug1")
      print("schedule_dict[next_finishing_time_idx] :", schedule_dict[next_finishing_time_idx])
      for starting_time in schedule_dict[next_finishing_time_idx] :
        if starting_time >= pre_endtime : 
          print("debug2")
          return next_finishing_time_idx
        else : 
          next_finishing_time_idx += 1
    except : 
      return "finish"
          
schedule_cnt = int(input())
for idx in range(schedule_cnt) :
  # 전체 일정 list를 만든다. 
  schedule = list(map(int, input().split()))
  schedule_lst.append(schedule)
  schedule_finishing_time_lst.append(schedule[1])
  # 끝나는 시간을 기준으로 dict를 만든다. 
  if schedule[1] in schedule_dict.keys() : 
    schedule_dict[schedule[1]].append(schedule[0]) 
  else : 
    schedule_dict[schedule[1]] = [schedule[0]]
  # 시작하는 시간을 구한다. 
  if idx == 0 : 
    starting_schedule = schedule
  elif starting_schedule[1] > schedule[1] : 
    starting_schedule = schedule

cnt = 0
schedule_finishing_time_lst = sorted(schedule_finishing_time_lst)
end_time = starting_schedule[1]

print("schedule_lst :", schedule_lst)
print("schedule_dict:", schedule_dict)
print("starting_schedule :", starting_schedule)
print("schedule_finishing_time_lst :", schedule_finishing_time_lst)


while True : 
  if end_time == "finish" : 
    break
  else : 
    print(end_time)
    end_time = find_next_finishing_time(end_time)
    cnt += 1

print(cnt)





# print(find_next_starting_time(end_time))#  == "finish": 
  

# 무한루프 생김
# 7
# 3 10 
# 2 2 
# 1 3 
# 2 2 
# 9 10 
# 4 9 
# 2 2
  




    
  
    
