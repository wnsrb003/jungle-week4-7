import sys
input = sys.stdin.readline

input_num_cnt = int(input())
input_num =list(map(int, input().split()))

cnt = 0
comparing_num = input_num[0]
for idx in range(1, input_num_cnt+1) :
  if comparing_num < input_num[idx] : 
    comparing_num = in