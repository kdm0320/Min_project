"""
두 개의 정 N면체와 정 M면체의 두 개의 주사위를 던져서 나올 수 있는 눈의 합 중 가장 확 률이 높은 숫자를 출력하는 프로그램을 작성하세요.
정답이 여러 개일 경우 오름차순으로 출력합니다.

▣ 입력설명
첫 번째 줄에는 자연수 N과 M이 주어집니다. N과 M은 4, 6, 8, 12, 20 중의 하나입니다.

▣ 출력설명
첫 번째 줄에 답을 출력합니다.

▣ 입력예제 1
46
▣ 출력예제 1
567
"""


import sys
from collections import  Counter
NUM = 4
sys.stdin=open(f"/Users/gimdongmin/Desktop/파이썬 알고리즘 강의/섹션 2/5. 정다면체/in{NUM}.txt","rt")
file = open(f"/Users/gimdongmin/Desktop/파이썬 알고리즘 강의/섹션 2/5. 정다면체/out{NUM}.txt")
answer = file.read()
print(f"answer : \n{answer}")
print(f"{'-'*50}")

n,m = map(int, input().split())
# n_num = [x for x in range(1,n+1)]
# m_num = [x for x in range(1,m+1)]
#
# all_sum = []
# for i in n_num:
#     for j in m_num:
#         all_sum.append(i+j)
# most_pers = Counter(all_sum).most_common()
# most_per =[]
# for per in most_pers:
#     if per[1] == most_pers[0][1]:
#         most_per.append(per[0])
# for i in most_per:
#     print(i, end=" ")
# print(" ".join(map(str,most_per)))
cnt = [0]*(n+m+3)
for i in range(1,n+1):
    for j in range(1, m+1):
        cnt[i+j] += 1
max_per = max(cnt)
for index,i in enumerate(cnt):
    if i == max_per:
        print(index,end=" ")

