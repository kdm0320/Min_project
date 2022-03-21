#---------- 정답 입력 코드 -----------------
import sys
NUM = 5
sys.stdin=open(f"/Users/gimdongmin/Desktop/파이썬 알고리즘 강의/섹션 4/3. 뮤직비디오/in{NUM}.txt","rt")
file = open(f"/Users/gimdongmin/Desktop/파이썬 알고리즘 강의/섹션 4/3. 뮤직비디오/out{NUM}.txt")
answer = file.read()
print(f"answer : \n{answer}")
print(f"{'-'*50}")
#----------------------------------------


#------------ 내 풀이 코드 -----------------  => 실패

def solution():                             # => 실패
    n,m = map(int,input().split())
    songs = list(map(int, input().split()))
    start = 1
    end = sum(songs)
    res=0
    cnt = 0
    while start <= end:
        mid= (start+end)//2
        tmp=0
        for song in songs:
            tmp+=song
            if tmp >= mid:
                tmp=0
                cnt+=1
                continue

        if cnt <= m:
            if res > mid:
                res = mid
            else:
                return res
            end = mid+1
        else:
            start = mid-1

    return res
# print(solution())

#-----------영상 풀이 코드 -------------------

def count(capacity,song):
    cnt=1
    sum=0
    for x in song:
        if sum + x > capacity:
            cnt+=1
            sum=x
        else:
            sum+=x
    return cnt


n,m = map(int,input().split())
songs = list(map(int, input().split()))
maxx = max(songs)
lt=1
rt=sum(songs)
res = 0
while lt <= rt:
    mid=(lt+rt)//2
    if mid>=maxx and count(mid,songs) <= m:
        res=mid
        rt=mid-1
    else:
        lt=mid+1
print(res)