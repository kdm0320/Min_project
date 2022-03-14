
#---------- 정답 입력 코드 -----------------
import sys
NUM = 1
sys.stdin=open(f"/Users/gimdongmin/Desktop/파이썬 알고리즘 강의/섹션 2/9. 주사위 게임/in{NUM}.txt","rt")
file = open(f"/Users/gimdongmin/Desktop/파이썬 알고리즘 강의/섹션 2/9. 주사위 게임/out{NUM}.txt")
answer = file.read()
print(f"answer : \n{answer}")
print(f"{'-'*50}")
#----------------------------------------

#------------ 내 풀이 코드 -----------------
# from collections import Counter
# n = int(input())
# prizes = []
# for _ in range(n):
#     nums = list(map(int,input().split()))
#     tmp = Counter(nums).most_common()
#     if len(nums) - len(tmp) == 2:
#         prizes.append(10000+tmp[0][0]*1000)
#     elif len(nums) - len(tmp) == 1:
#         prizes.append(1000+tmp[0][0]*100)
#     else:
#         prizes.sort()
#         prizes.append(1000+tmp[0][0]*100)
# print(max(prizes))
#------------ 답 풀이 코드 -----------------
n = int(input())
res = 0
for _ in range(n):
    tmp = sorted(input().split())
    a,b,c = map(int, tmp)
    if a==b and b==c:
        money = 10000+a*1000
    elif a==b or a==c:
        money = 1000+a*100
    elif b==c:
        money = 1000+a*100
    else:
        money = c*100
    if money > res:
        res = money
print(res)

