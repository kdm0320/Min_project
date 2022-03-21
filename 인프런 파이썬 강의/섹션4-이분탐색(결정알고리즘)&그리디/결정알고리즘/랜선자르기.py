
#---------- 정답 입력 코드 -----------------
import sys
NUM = 5
sys.stdin=open(f"/Users/gimdongmin/Desktop/파이썬 알고리즘 강의/섹션 4/2. 랜선자르기/in{NUM}.txt","rt")
file = open(f"/Users/gimdongmin/Desktop/파이썬 알고리즘 강의/섹션 4/2. 랜선자르기/out{NUM}.txt")
answer = file.read()
print(f"answer : \n{answer}")
print(f"{'-'*50}")
#----------------------------------------


#------------ 내 풀이 코드 -----------------

def solution():
    k,n = map(int,input().split())
    lines = [int(input()) for _ in range(k)]
    lines.sort()
    find = [x for x in range(lines[0],lines[-1]+1)] #비효율 원인 1
    start = 0
    end = len(find)-1
    max = -217600000
    while start <= end:
        mid = (start+end)//2
        a = [x//find[mid] for x in lines] # 비효율 원인 2
        if sum(a) >= n:
            if max <find[mid]:
                max = find[mid]
            start = mid+1
        else:
            end = mid -1
    return max
# print(solution())

#-----------영상 풀이 코드 -------------------
def count(len,line):
    cnt=0
    for x in line:
        cnt+=(x//len)
    return cnt

k, n = map(int, input().split())
lines = []
res = 0
largest=0
for i in range(k):
    tmp = int(input())
    lines.append(tmp)
    largest = max(largest,tmp)
lt=1
rt=largest
while lt<=rt:
    mid = (lt+rt)//2
    if count(mid,lines) >= n:
        res = mid
        lt = mid+1
    else:
        rt = mid-1
print(res)
