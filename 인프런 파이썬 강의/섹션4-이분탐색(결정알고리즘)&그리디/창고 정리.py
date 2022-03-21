#---------- 정답 입력 코드 -----------------
import sys
NUM = 5
sys.stdin=open(f"/Users/gimdongmin/Desktop/파이썬 알고리즘 강의/섹션 4/7. 창고 정리/in{NUM}.txt","rt")
file = open(f"/Users/gimdongmin/Desktop/파이썬 알고리즘 강의/섹션 4/7. 창고 정리/out{NUM}.txt")
answer = file.read()
print(f"answer : \n{answer}")
print(f"{'-'*50}")
#----------------------------------------

#------------ 내 풀이 코드 -----------------
def solution():
    l = int(input())
    boxes = list(map(int,input().split()))
    m = int(input())
    boxes.sort()
    for _ in range(m):
        boxes[l-1]-=1
        boxes[0]+=1
        if boxes[l-2] > boxes[l-1] or boxes[0] > boxes[1]:
            boxes.sort()
    res = boxes[l-1] - boxes[0]
    return res


print(solution())


#-----------영상 풀이 코드 -------------------
