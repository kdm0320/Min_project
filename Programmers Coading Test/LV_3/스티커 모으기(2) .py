

sticker = [14, 6, 5, 11, 3, 9, 2, 10]

#메모이제이션 사용
#DP
def solution(sticker):
    # table[i] = i번째 스티커를 떼는 경우 최댓값
    # 맨 앞 스티커를 떼는지 아닌지 -> 맨 뒤 스티커에 영향을 준다
    if len(sticker) == 1:
        return sticker[0]
    # 1. 맨 앞 스티커를 떼는 경우
    table1 = [0 for _ in range(len(sticker))]
    table1[0] = sticker[0]
    table1[1] = table1[0]
    for i in range(2, len(sticker) - 1):
        table1[i] = max(table1[i - 1], table1[i - 2] + sticker[i])
    value = max(table1)

    # 2. 맨 앞 스티커를 떼지 않는 경우
    table1 = [0 for _ in range(len(sticker))]
    table1[0] = 0
    table1[1] = sticker[1]
    for i in range(2, len(sticker)):
        table1[i] = max(table1[i - 1], table1[i - 2] + sticker[i])
    return max(value, max(table1))

print(solution(sticker))



