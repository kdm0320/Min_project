from collections import Counter
from functools import reduce
def solution(clothes):
    cnt = Counter([kind for name, kind in clothes])
    answer = reduce(lambda x, y: x*(y+1), cnt.values(), 1) - 1
    return answer

clothes = [["crowmask", "face","a"], ["bluesunglasses", "face","a"], ["smoky_makeup", "face","a"]]
#print(solution(clothes))

cnt = [alpha for name, kind,alpha in clothes]
print(cnt)


