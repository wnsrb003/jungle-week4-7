import sys
input = sys.stdin.readline
schedule_cnt = int(input())
schedule_lst =[]
for idx in range(schedule_cnt) :
  schedule = list(map(int, input().split()))
  schedule_lst.append(schedule)

schedule_lst.sort(key=lambda x:(x[1], x[0]))

cnt = 1
finishing_time = schedule_lst[0][1]
for schecule_idx in range(1, len(schedule_lst)) : 
  if schedule_lst[schecule_idx][0] >= finishing_time :
    cnt += 1
    finishing_time = schedule_lst[schecule_idx][1]
    

print(cnt)
    