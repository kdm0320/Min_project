import math
from collections import Counter

def solution(str1, str2):
    set1 = Counter([str1[i:i+2].upper() for i in range(0, len(str1)-1) if str1[i:i+2].isalpha()])
    set2 = Counter([str2[i:i+2].upper() for i in range(0, len(str2)-1) if str2[i:i+2].isalpha()])
    J = lambda A, B: 1 if len(A) == 0 and len(B) == 0 else sum((A & B).values()) / sum((A | B).values())
    return math.floor(J(set1, set2) * 65536)
	
	
	
	
	
	
print(solution(str1,str2))
