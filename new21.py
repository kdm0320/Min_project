






def solution(abilities, k):
    answer = 0
    p =sorted(abilities,reverse=True)
    max = 0
    c = k
    t = 0
    for i in range(k):
        for j in range(0,len(abilities),2):
            c-=1

    return answer


abilities = [7, 6, 8, 9, 10]
k = 2

print(solution(abilities,k))