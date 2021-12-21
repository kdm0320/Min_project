from itertools import combinations
import operator

orders =["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
course = [2,3,4]

temp_orders = [sorted(list(i)) for i in orders]
new_orders = ["".join(i) for i in temp_orders]

temp_re = {}
print(temp_re)
for i in temp_re:
	print(id(i))
answer = []
m= 0

for order in temp_orders:
	for c in course:
		if len(order) < c:
			break
		else:
			combs = ["".join(i) for i in list(combinations(order,c))]
			print(combs)
			for comb in combs:
				if comb in temp_re.keys():
					temp_re[comb]+=1
				else:
					temp_re[comb] = 1

for c in course:
	for re in =temp_re:
		if c==len(re):
			break
				
			

print(temp_re)
				

	
				

#print(sorted(answer))

		
