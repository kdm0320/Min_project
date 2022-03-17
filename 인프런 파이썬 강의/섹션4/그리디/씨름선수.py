#---------- 정답 입력 코드 -----------------
import sys
NUM = 5
sys.stdin=open(f"/Users/gimdongmin/Desktop/파이썬 알고리즘 강의/섹션 4/6. 씨름선수/in{NUM}.txt","rt")
file = open(f"/Users/gimdongmin/Desktop/파이썬 알고리즘 강의/섹션 4/6. 씨름선수/out{NUM}.txt")
answer = file.read()
print(f"answer : \n{answer}")
print(f"{'-'*50}")
#----------------------------------------

#------------ 내 풀이 코드 ----------------- => 이중 for문 -> 비효율적

def solution():
    n = int(input())
    ap = [tuple(map(int,input().split())) for _ in range(n)]
    ap.sort()
    res = 0
    for i in range(n):
        for j in range(i+1,n):
            if ap[i][1] < ap[j][1]:
                break
        else:
            res+=1

    return res

# print(solution())


#-----------영상 풀이 코드 -------------------
n = int(input())
ap = [tuple(map(int, input().split())) for _ in range(n)]
ap.sort(reverse=True)
cnt = 0
max = 0
for a in ap:
    if a[1] >= max:
        max = a[1]
        cnt+=1
print(cnt)