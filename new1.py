

import decimal

def solution(n, clockwise):
    answer = [[]]
    start = 0  # 숫자 1, 2, 3, ...
    step = 1  # 증가/감소 크기: 1, -1
    y = 0  # 줄 위치
    x = -1  # 칸 위치 (배열 선두보다 한칸 앞)
    arr = [[0] * n for i in range(n)]  # 2차원 배열 구조
    cnt = 1
    while cnt < round(n/2):
        for i in range(n-cnt):  # 몇 칸 진행할까
            start += 1
            x += step
            arr[y][x] = start
        cnt += 1
        for i in range(n-cnt):  # 몇 줄 진행할까
            start += 1
            y += step
            arr[y][x] = start
        cnt += 1
        step = -step  # 증감 방향을 반대로

    # 2차원 리스트 출력하기
    for line in arr:
        for n in line:
            print('%3d' % n, end='')
        print()

    return answer


n = 5
clockwise =True

print(solution(n,clockwise))