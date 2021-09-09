#리스트 컴프리헨션
#리스트를 초기화 하는 방법 중 하나

#0부터 19까지의 수 중에서 홀수만 포함하는 리스트
array1 = [i for i in range(20)if i %2==1]
print("0부터 19까지의 수 중에서 홀수만 포함하는 리스트:",array1)

#1부터 9까지 제곱 값을 포함하는 리스트
array2 = [i*i for i in range(1,10)]
print("1부터 9까지 제곱 값을 포함하는 리스트:",array2)

#2차원 리스트 초기화 - 특정 크기의 2차원 리스트를 초기화할때는 반드시 리스트 컴프리헨션을 이용

#N X M 크기의 리스트 초기화
N = 4
M = 5
array3 = [[0]*M for _ in range(N)]
print("N X M 크기의 리스트 초기화:", array3)

#리스트에서 특정 값의 원소를 모두 제거하는 방법
a = [1,2,3,4,5,5,5,5]
remove_set = [1,2,3,4]
# 5 제거
result = [i for i in a if i in remove_set]
print(f"리스트 {a} 에서 '5'를 제거한 결과: {result}")