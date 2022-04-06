#reduce

#reduce(function, iterable, initializer=None)
# example
from functools import  reduce
result = reduce(lambda x,y:x+y, [1,2,3,4,5])
#((((1+2)+3)+4)+5)
print(result)
#15

# 초기값 존재 예제
result1 = reduce(lambda x,y:x+y, [1,2,3,4,5],100)
print(result1)

#최댓값 구하기
func = lambda a,b: a if (a>b) else b
result2 = reduce(func,[1,100,20,30,40,50])
print(result2)