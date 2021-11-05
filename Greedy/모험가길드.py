"""
N명의 모험가가 존재, 각 모험가는 X만큼의 공포도를 각각 가지고 있음
공포도가 X인 모험가는 반드시 X명 이상으로 구성된 그룹에 참여해야만 한다
N명의 모험가가 주어졌을때 여행을 떠날 수 있는 그룹 수의 최댓값을 구하는 프로그램을 작성하라

첫째줄에 모험가 수 N이 주어진다(1<=N<=100,000)
둘째줄에 각 모험가의 공포의 값이 N 이하의 자연수로 주어지며 각 자연수는 공백으로 구분
여행을 떠날 수 있는 그룹 수의 최댓값을 출력하라
"""
n = int(input())

scare = list(map(int, input().split()))

scare.sort()

group = 0
count = 0
for i in scare:
    count+=1
    if count >= i:
        group+=1
        count = 0
print(group)

