"""투 포인터 알고리즘 이용"""

#투 포인터 알고리즘으로 반복문을 통해 비교

#ai(A의 포인터), bi(B의 포인터)를 사용하여 A와 B의 값을 각각 비교하는데, 두 가지 경우로 나눈다.

#1. A[ai] > B[bi]: A의 원소 값이 B의 원소값보다 크므로 B의 다음 원소를 A의 원소와 비교.

#2. A[ai] < B[bi]: B의 원소 값이 A의 원소값보다 크므로 승점이 1올라가고, A와 B 모두의 다음 원소를 서로 비교.

A = [5,1,3,7]
B = [2,2,6,8]


def solution(A, B):
    answer = 0

    A.sort()  # 1단계
    B.sort()

    ai, bi = 0, 0  # 2단계
    while ai != len(A) and bi != len(B):
        if B[bi] > A[ai]:
            answer += 1
            ai += 1
            bi += 1
        else:
            bi += 1

    return answer

print(solution(A,B))