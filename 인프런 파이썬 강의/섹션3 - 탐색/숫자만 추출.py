


#---------- 정답 입력 코드 -----------------
import sys
NUM = 1
sys.stdin=open(f"/Users/gimdongmin/Desktop/파이썬 알고리즘 강의/섹션 3/2. 숫자만 추출/in{NUM}.txt","rt")
file = open(f"/Users/gimdongmin/Desktop/파이썬 알고리즘 강의/섹션 3/2. 숫자만 추출/out{NUM}.txt")
answer = file.read()
print(f"answer : \n{answer}")
print(f"{'-'*50}")
#-----------------------------------------

#------------ 내 풀이 코드 -----------------

def count(x):
    num = 0
    for i in range(1,x+1):
        if x%i == 0:
            num+=1
    return num

st = input()
x = ""
for i in st:
    if i.isdigit():
        x+=i
print(int(x))
print(count(int(x)))
