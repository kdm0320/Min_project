#---------- 정답 입력 코드 -----------------
import sys
NUM = 4
sys.stdin=open(f"/Users/gimdongmin/Desktop/파이썬 알고리즘 강의/섹션 3/4. 두 리스트 합치기/in{NUM}.txt","rt")
file = open(f"/Users/gimdongmin/Desktop/파이썬 알고리즘 강의/섹션 3/4. 두 리스트 합치기/out{NUM}.txt")
answer = file.read()
print(f"answer : \n{answer}")
print(f"{'-'*50}")
#-----------------------------------------

#------------ 내 풀이 코드 -----------------
n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))
for i in sorted(a+b):
    print(i, end=" ")
