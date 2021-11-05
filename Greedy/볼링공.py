"""
N개의 공의 무게가 각각 주어질때, 두사람이 볼링공을 고르는 경우의 수를 구하라
N = 볼링공의 개수
M = 공의 최대 무게
K = 각 볼링공의 무게
1<=N<=1,000, 1<=M<=10
1<=K<=M
"""
import itertools

n,m = input().split()
k = list(map(int, input().split()))
answer = 0

for i in itertools.combinations(k,2):
    if i[0] != i[1]:
        answer+=1

# for i in range(len(k)-1):
#     for j in range(i+1,len(k)):
#         if k[i] != k[j]:
#             answer+=1

print(answer)
