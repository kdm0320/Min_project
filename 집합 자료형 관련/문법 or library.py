#집합 자료형 초기화 방법 1

data1 = set([1,1,2,3,4,4,5])
print(data1)

#집합 자료형 초기화 방법 2

data2 = {1,1,2,3,4,4,5}
print(data2)

#집합 자료형 연산

#합집합 = (a|b)
#교집합 = (a&b)
#차집합 = (a-b)

#함수들
data = set([1,2,3])
print(data)
#원소 하나 추가
data.add(4)
print(data)
#원소 여러개 추가
data.update([5,6])
print(data)
#특정 원소 삭제
data.remove(3)
print(data)
