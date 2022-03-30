#---------- 정답 입력 코드 -----------------
import sys
NUM = 5
sys.stdin=open(f"/Users/gimdongmin/Desktop/파이썬 알고리즘 강의/섹션 5/3. 후위표기식 만들기/in{NUM}.txt","rt")
file = open(f"/Users/gimdongmin/Desktop/파이썬 알고리즘 강의/섹션 5/3. 후위표기식 만들기/out{NUM}.txt")
answer = file.read()
print(f"answer : \n{answer}")
print(f"{'-'*50}")
#----------------------------------------

#------------ 내 풀이 코드 -----------------  => 설명 들어도 실패

def solution():
    res = "실패"
    return res







# print(solution())


#-----------영상 풀이 코드 -------------------

k = input()
stack=[]
res = ""
for x in k:
    if x.isdecimal():
        res+=x
    else:
        if x=="(":
            stack.append(x)
        elif x=="*" or x=="/":
            while stack and (stack[-1]=="*" or stack[-1]=="/"):
                res+=stack.pop()
            stack.append(x)
        elif x == "+" or x == "-":
            while stack and stack[-1]!="(":
                res+=stack.pop()
            stack.append(x)
        elif x == ")":
            while stack and stack[-1]!="(":
                res+=stack.pop()
            stack.pop()
while stack:
    res+=stack.pop()
print(res)