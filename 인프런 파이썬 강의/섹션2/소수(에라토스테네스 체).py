#N보다 작거나 같은 모든 소수를 찾을 때 사용 가능

import math

#---------- 정답 입력 코드 -----------------
import sys
NUM = 5
sys.stdin=open(f"/Users/gimdongmin/Desktop/파이썬 알고리즘 강의/섹션 2/7. 소수(에라토스테네스 체)/in{NUM}.txt","rt")
file = open(f"/Users/gimdongmin/Desktop/파이썬 알고리즘 강의/섹션 2/7. 소수(에라토스테네스 체)/out{NUM}.txt")
answer = file.read()
print(f"answer : \n{answer}")
print(f"{'-'*50}")
#----------------------------------------

#------------ 내 풀이 코드 -----------------

def eratostenes(n):
    array = [True for i in range(n+1)] # 처음엔 모든 수가 소수(True)인 것으로 초기화(0,1은 제외)

    for i in range(2, int(math.sqrt(n)) + 1):  # 2부터 n의 제곱근까지의 모든 수를 판별
        if array[i] == True:  # i가 소수인 경우(남은 수인 경우)
            # i를 제외한 모든 배수를 지우기
            j = 2
            while i * j <= n:
                array[i * j] = False
                j += 1
    cnt = 0
    for i in range(2, n + 1):  # 모든 소수 출력
        if array[i]:
            cnt+=1
    print(cnt)


n = int(input())
eratostenes(n)

