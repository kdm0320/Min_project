#---------- 정답 입력 코드 -----------------
import sys
NUM = 5
sys.stdin=open(f"/Users/gimdongmin/Desktop/파이썬 알고리즘 강의/섹션 3/5. 수들의 합/in{NUM}.txt","rt")
file = open(f"/Users/gimdongmin/Desktop/파이썬 알고리즘 강의/섹션 3/5. 수들의 합/out{NUM}.txt")
answer = file.read()
print(f"answer : \n{answer}")
print(f"{'-'*50}")
#-----------------------------------------

#------------ 내 풀이 코드 -----------------
from functools import reduce

n,m = map(int, input().split())
nums = list(map(int, input().split()))
cases = 0
start = 0
last = 1
while last <= n:
    if nums[start] < m or nums[last] < m:
        result = reduce(lambda x,y:x+y,nums[start:last])
        if result > m:
            start+=1
            continue
        if result == m:
            cases+=1
            start+=1
        last+=1
print(cases)