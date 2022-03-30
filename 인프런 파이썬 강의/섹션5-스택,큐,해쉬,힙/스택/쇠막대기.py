#---------- 정답 입력 코드 -----------------
import sys
NUM = 4
sys.stdin=open(f"/Users/gimdongmin/Desktop/파이썬 알고리즘 강의/섹션 5/2. 쇠막대기/in{NUM}.txt","rt")
file = open(f"/Users/gimdongmin/Desktop/파이썬 알고리즘 강의/섹션 5/2. 쇠막대기/out{NUM}.txt")
answer = file.read()
print(f"answer : \n{answer}")
print(f"{'-'*50}")
#----------------------------------------

#------------ 내 풀이 코드 -----------------  => 설명 들어도 실패 => 두번째 설명듣고 성공

def solution():
    k = input()
    stack = []
    res = 0
    for index,i in enumerate(k):
        if i =="(":
            stack.append(i)
        else:
            stack.pop()
            if k[index-1] == "(":
                res+=len(stack)
            else:
                res+=1
    return res







print(solution())


#-----------영상 풀이 코드 -------------------

