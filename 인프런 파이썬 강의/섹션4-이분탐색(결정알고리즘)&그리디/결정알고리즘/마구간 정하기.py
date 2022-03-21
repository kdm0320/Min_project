#---------- 정답 입력 코드 -----------------
import sys
NUM = 2
sys.stdin=open(f"/Users/gimdongmin/Desktop/파이썬 알고리즘 강의/섹션 4/4. 마구간 정하기/in{NUM}.txt","rt")
file = open(f"/Users/gimdongmin/Desktop/파이썬 알고리즘 강의/섹션 4/4. 마구간 정하기/out{NUM}.txt")
answer = file.read()
print(f"answer : \n{answer}")
print(f"{'-'*50}")
#----------------------------------------

#------------ 내 풀이 코드 ----------------- => 실패

def solution():
    n,c = map(int,input().split())
    cage = sorted([int(input()) for _ in range(n)])
    res=0


    return res

# print(solution())


#-----------영상 풀이 코드 -------------------
def count(n,length,cage):
    cnt=1
    ep = cage[0]
    for i in range(1,n):
        if cage[i]-ep >= length:
            cnt+=1
            ep = cage[i]
    return cnt

n, c = map(int, input().split())
cage = sorted([int(input()) for _ in range(n)])
start = 1
end = cage[-1]
res=0
while start <= end:
    mid = (start+end)//2
    if count(n,mid,cage) >= c:
        res=mid
        start = mid+1
    else:
        end = mid-1
print(res)