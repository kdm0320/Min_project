from bisect import bisect_left, bisect_right

'''
정렬된 배열에서 특정한 원소를 찾아야 할때 매우 효과적으로 사용
'''

# 특정 범위 안에 있는 원소의 개수 구하는 알고리즘
def count_by_range(a,left_value,right_value):
    right_index = bisect_right(a,right_value)
    left_index = bisect_left(a,left_value)
    return right_index-left_index

a = [1,2,3,3,3,3,3,4,4,8,9]

#값이 4인 데이터 출력
print(count_by_range(a,4,4))

#값이 [-1,3] 범위에 있는 데이터 개수 출력

print(count_by_range(a,-1,3))