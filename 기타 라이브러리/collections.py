#deque
#큐를 구현할때 사용
#deque 자료형은 리스트와 달리 인슬싱, 슬라이싱 사용 불가
#연속적으로 나열된 데이터의 시작부분이나 끝부분에 데이터를 삽입하거나 삭제할때 효과적
#스택이나 큐의 대용으로 사용가능
#첫번째 원소 제거할때 popleft(), 끝 원소 제거할떄 pop()
#첫번째 인덱스에 원소 x를 삽입할때 appendleft(x), 마지막 인덱스에 삽일할때 append(x)
#deque를 큐로 이용할때 원소 삽입할때 append(),삭제할때는 poplef()

from collections import deque,Counter

data = deque([2,3,4])
data.appendleft(1)
data.append(5)

print(data)
print(list(data))

#Counter = Iterable한 객체 내부의 원소가 몇번씩 등장했는지 알려준다

counter = Counter(['red','blue','green','blue','blue'])
print(conter['blue'])
print(conter['green'])
print(counter)