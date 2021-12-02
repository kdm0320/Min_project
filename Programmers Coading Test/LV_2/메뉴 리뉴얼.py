

import collections
from itertools import combinations

def solution(orders, course):
    result = []

    for course_size in course:
        order_combinations = []
        for order in orders:
            order_combinations += combinations(sorted(order), course_size)
        most_ordered = collections.Counter(order_combinations).most_common()
        result += [ k for k, v in most_ordered if v > 1 and v == most_ordered[0][1] ]
    return [ ''.join(v) for v in sorted(result) ]


# def solution(orders,course): #내 풀이
#
# 	temp_orders = [sorted(list(i)) for i in orders]
# 	temp_re = {}
# 	answer = []
# 	for order in temp_orders:
# 		for c in course:
# 			if len(order) < c:
# 				break
# 			else:
# 				combs = ["".join(i) for i in list(combinations(order,c))]
# 				for comb in combs:
# 					if comb in temp_re.keys():
# 						temp_re[comb]+=1
# 					else:
# 						temp_re[comb] = 1
# 	for c in course:
# 		a = [i for i in temp_re if len(i)==c]
# 		m = [0, ""]
# 		for j in a:
# 			if temp_re[j] > m[0]:
# 				m = [0,""]
# 				m[1] = j
# 				m[0] = temp_re[j]
# 			elif temp_re[j] == m[0]:
# 				m.append(j)
# 		if m[0] >= 2:
# 			for k in range(1,len(m)):
# 				answer.append(m[k])
# 	return sorted(answer)

orders =["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"]
course = [2,3,5]

print(solution(orders,course))





	
				

#print(sorted(answer))

		
