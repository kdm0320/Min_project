"""
N명의 학생의 수학점수가 주어집니다. N명의 학생들의 평균(소수 첫째자리 반올림)을 구하고,
N명의 학생 중 평균에 가장 가까운 학생은 몇 번째 학생인지 출력하는 프로그램을 작성하세 요.
평균과 가장 가까운 점수가 여러 개일 경우 먼저 점수가 높은 학생의 번호를 답으로 하고,
높 은 점수를 가진 학생이 여러 명일 경우 그 중 학생번호가 빠른 학생의 번호를 답으로 합니다.

▣ 입력설명
첫줄에 자연수 N(5<=N<=100)이 주어지고, 두 번째 줄에는 각 학생의 수학점수인 N개의 자연 수가 주어집니다.
학생의 번호는 앞에서부터 1로 시작해서 N까지이다.

▣ 출력설명
첫줄에 평균과 평균에 가장 가까운 학생의 번호를 출력한다. 평균은 소수 첫째 자리에서 반올림합니다.

입력예제 1
10
45 73 66 87 92 67 75 79 75 80
출력예제 1
7
"""


import sys
NUM = 3
sys.stdin=open(f"/Users/gimdongmin/Desktop/파이썬 알고리즘 강의/섹션 2/4. 대표값/in{NUM}.txt","rt")
file = open(f"/Users/gimdongmin/Desktop/파이썬 알고리즘 강의/섹션 2/4. 대표값/out{NUM}.txt")
answer = file.read()
print(f"answer : \n{answer}")
print(f"{'-'*50}")


n = int(input())
scores = list(map(int, input().split()))
average = int(sum(scores) / n + 0.5)
min = 999999
# for index,score in enumerate(scores):
#      temp = abs(average - score)
#      if temp < min:
#          min = temp
#          stu = []
#          stu.append((score,index))
#      elif temp == min:
#          stu.append((score,index))
#
# stu.sort(key= lambda x : (x[0],x[1]), reverse=True)
# stu.sort(key= lambda x : (x[1],x[0]))
# score = 0
# res = 0
for index,x in enumerate(scores):
    temp = abs(average-x)
    if temp < min:
        min = temp
        score= x
        res = index
    elif temp == min:
        if x > score:
            score=x
            res = index

print(average, res+1)



