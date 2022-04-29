
import sys
input = sys.stdin.readline

input_cnt =int(input())

dp_t = [list(map(int,(input().strip().split()))) for _ in range(input_cnt)]

print(dp_t)