#---------- 정답 입력 코드 -----------------
import sys
NUM = 2
sys.stdin=open(f"/Users/gimdongmin/Desktop/파이썬 알고리즘 강의/섹션 5/4. 후위식 연산/in{NUM}.txt","rt")
file = open(f"/Users/gimdongmin/Desktop/파이썬 알고리즘 강의/섹션 5/4. 후위식 연산/out{NUM}.txt")
answer = file.read()
print(f"answer : \n{answer}")
print(f"{'-'*50}")
#----------------------------------------

#------------ 내 풀이 코드 -----------------  => 설명듣고 품

def solution():
    k = input()
    stack = []
    for i in k:
        if i.isdecimal():
            stack.append(i)
        else:
            tmp1 = stack.pop()
            tmp2 = stack.pop()
            stack.append(str(eval(tmp2+i+tmp1)))

    return stack.pop()







# print(solution())


#-----------영상 풀이 코드 -------------------

f = input()
stack = []
for i in f:
    if i.isdecimal():
        stack.append(int(i))
    else:
        n1=stack.pop()
        n2=stack.pop()
        if i == "+":
            stack.append(n2+n1)
        elif i == "-":
            stack.append(n2-n1)
        elif i == "/":
            stack.append(n2/n1)
        else:
            stack.append(n2*n1)
print(stack[0])

