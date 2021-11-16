"""
리스트에 순차적으로 접근해야 할 때 2개의 점의 위치를 기록하면서 처리하는 알고리즘
리스트 부분합 찾기에 유용
정렬되어 있는 두 리스트의 합집합 같은 문제에 효과적
2개 점의 위치 기록 => 두개의 포인터를 만든다
"""


n = 5  # 데이터의 개수 N
m = 5  # 찾고자 하는 부분합 M
data = [1, 2, 3, 2, 5]  # 전체 수열

count = 0
interval_sum = 0
end = 0

# start를 차례대로 증가시키며 반복
for start in range(n):
    # end를 가능한 만큼 이동시키기
    while interval_sum < m and end < n:
        interval_sum += data[end]
        end += 1
    # 부분합이 m일 때 카운트 증가
    if interval_sum == m:
        count += 1
    interval_sum -= data[start]

print(count)