
#---------- 정답 입력 코드 -----------------
import sys
NUM = 5
sys.stdin=open(f"/Users/gimdongmin/Desktop/파이썬 알고리즘 강의/섹션 2/8. 뒤집은 소수/in{NUM}.txt","rt")
file = open(f"/Users/gimdongmin/Desktop/파이썬 알고리즘 강의/섹션 2/8. 뒤집은 소수/out{NUM}.txt")
answer = file.read()
print(f"answer : \n{answer}")
print(f"{'-'*50}")
#----------------------------------------

#------------ 내 풀이 코드 -----------------
import math


#수 하나의 소수 판별
def isPrime(x):
    #2부터 x의 제곱근까지의 모든 수를 확인하며
    for i in range(2, int(math.sqrt(x)) + 1):
        #x가 해당 수로 나누어떨어진다면
        if x % i == 0:
            return False #소수가 아님
    return True

def reverse(x):
    new = ""
    for i in reversed(x):
        new+=i
    return int(new)

n = int(input())
nums = input().split()
for num in nums:
    new = reverse(num)
    if new != 1:
        if isPrime(new):
            print(new, end=" ")

#------------ 숫자 이용 풀이 코드 -----------------
def reverse(x):
    res = 0
    while x > 0:
        t = x%10
        res = res*10+t
        x = x//10
    return res
