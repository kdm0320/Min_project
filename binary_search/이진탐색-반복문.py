

"""
리스트 전체
리스트 길이 = n
start = 0
end = n-1
"""


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