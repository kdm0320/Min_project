
#---------- 정답 입력 코드 -----------------
import sys
NUM = 1
sys.stdin=open(f"/Users/gimdongmin/Desktop/파이썬 알고리즘 강의/섹션 4/1. 이분검색/in{NUM}.txt","rt")
file = open(f"/Users/gimdongmin/Desktop/파이썬 알고리즘 강의/섹션 4/1. 이분검색/out{NUM}.txt")
answer = file.read()
print(f"answer : \n{answer}")
print(f"{'-'*50}")
#----------------------------------------


#------------ 내 풀이 코드 -----------------
from bisect import  bisect_left
def binary_search(array,target,start,end):
    while start<=end:
        mid = (start+end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid -1
        else:
            start = mid+1
    return "찾고자 하는 수가 없습니다."

def solution():
    n,m = map(int, input().split())
    nums = list(map(int, input().split()))
    nums.sort()
    print(bisect_left(nums,m)+1)
    return binary_search(nums,m,0,n-1)+1

print(solution())
#-----------영상 풀이 코드 -------------------






