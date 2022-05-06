#---------- 정답 입력 코드 -----------------
import sys
NUM = 2
sys.stdin=open(f"/Users/gimdongmin/Desktop/파이썬 알고리즘 강의/섹션 8/1, 2. 네트워크 선 자르기/in{NUM}.txt","rt")
file = open(f"/Users/gimdongmin/Desktop/파이썬 알고리즘 강의/섹션 8/1, 2. 네트워크 선 자르기/out{NUM}.txt")
answer = file.read()
print(f"answer : \n{answer}")
print(f"{'-'*50}")
#----------------------------------------

import time
#------------ 내 풀이 코드 -----------------

# start = time.time()


# print(f"{end - start:.5f} sec")

#-----------영상 풀이 코드 -------------------
start = time.time()

def dfs(len):
    if dy[len] >0:
        return dy[len]
    if len==1 or len==2:
        return len
    else:
        dy[len] = dfs(len-1)+dfs(len-2)
        return dy[len]


n = int(input())
dy=[0]*(n+1)
print(dfs(n))

end = time.time()
print(f"{end - start:.5f} sec")