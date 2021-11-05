"""
N개의 동전들로 만들 수 없는 양의 정수 금액 중 최솟값을 출력하라
첫쨰 줄에 동전의 개수가 주어짐
N(1<=N<=1,000)
화폐 단위는 1,000,000 이하의 자연수
"""

n = int(input())

coins = list(map(int, input().split()))

coins.sort()

target = 1

for x in coins:
    if target < x:
        break
    target+=x

print(target)

