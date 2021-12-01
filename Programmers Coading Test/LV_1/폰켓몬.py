

def solution(nums):
	return min(len(nums)/2, len(set(nums)))
    
    
nums = [1,2,3,4,5,6,7,8,9,10]
print(solution(nums))
