#---------- 정답 입력 코드 -----------------
import sys
NUM = 5
sys.stdin=open(f"/Users/gimdongmin/Desktop/파이썬 알고리즘 강의/섹션 4/5. 회의실 배정/in{NUM}.txt","rt")
file = open(f"/Users/gimdongmin/Desktop/파이썬 알고리즘 강의/섹션 4/5. 회의실 배정/out{NUM}.txt")
answer = file.read()
print(f"answer : \n{answer}")
print(f"{'-'*50}")
#----------------------------------------

#------------ 내 풀이 코드 ----------------- => 강의 설명 듣고 품

def solution():
    n = int(input())
    con = [tuple(map(int,input().split())) for _ in range(n)]
    con.sort(key= lambda x: (x[1],x[0]))
    end = 0
    res = 0
    for c in con:
        if c[0] >= end:
            res+=1
            end = c[1]


    return res

print(solution())


#-----------영상 풀이 코드 -------------------