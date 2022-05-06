#---------- 정답 입력 코드 -----------------
import sys
NUM = 5
sys.stdin=open(f"/Users/gimdongmin/Desktop/파이썬 알고리즘 강의/섹션 8/1, 2. 네트워크 선 자르기/in{NUM}.txt","rt")
file = open(f"/Users/gimdongmin/Desktop/파이썬 알고리즘 강의/섹션 8/1, 2. 네트워크 선 자르기/out{NUM}.txt")
answer = file.read()
print(f"answer : \n{answer}")
print(f"{'-'*50}")
#----------------------------------------

import time
#------------ 내 풀이 코드 -----------------

# start = time.time()

# n = int(input())
# temp = 0
# n_list = [0]*(n+1)
# for i in range(1,n+1):
#     if i==1:
#         n_list[i] = 1
#     elif i==2:
#         n_list[i] = 2
#     else:
#         n_list[i] = n_list[i-1]+n_list[i-2]
# print(n_list[n])

# end = time.time()
# print(f"{end - start:.5f} sec")

#-----------영상 풀이 코드 -------------------

start = time.time()

n = int(input())

dy = [0]*(n+1)
dy[1] = 1
dy[2] = 2
for i in range(3,n+1):
    dy[i] = dy[i-1]+dy[i-2]


print(dy[n])
end = time.time()
print(f"{end - start:.5f} sec")