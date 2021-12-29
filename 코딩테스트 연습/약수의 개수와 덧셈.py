<<<<<<< HEAD
=======
from math import sqrt
>>>>>>> origin/master


def solution(left, right):
    answer = 0
    for i in range(left,right+1):
        if int(i**0.5)==i**0.5:
            answer -= i
        else:
            answer += i
    return answer

left = 24
right = 27

<<<<<<< HEAD
print(solution(left,right))
=======
print(solution(left,right))
>>>>>>> origin/master
