from bisect import bisect_left,bisect_right

n,x = map(int, input().split())

num = list(map(int, input().split()))

def count_by_range(a, left_value, right_value):
	right_index = bisect_right(a,right_value)
	left_index = bisect_left(a,left_value)
	if right_index - left_index == 0:
		return -1
	else:
		return right_index-left_index
	

print(count_by_range(num,x,x))

