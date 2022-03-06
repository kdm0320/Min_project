from itertools import combinations


#https://codlingual.tistory.com/161
def solution(relation):
    # key의 개수
    N = len(relation[0])
    key_idx = list(range(N))
    candidate_keys = []

    for i in range(1, N + 1):
        for comb in combinations(key_idx, i):
            hist = []
            for rel in relation:
                current_key = [rel[c] for c in comb]
                # 하나라도 중복되는 경우: 식별 불가능
                if current_key in hist:
                    break
                else:
                    hist.append(current_key)
            # 하나도 중복 안 된 경우: 식별 가능
            else:
                for ck in candidate_keys:
                    # 최소성 확인
                    if set(ck).issubset(set(comb)):
                        break
                else:
                    candidate_keys.append(comb)

    return len(candidate_keys)

def solution2(relation):
    row = len(relation)
    col = len(relation[0])

    #전체 조합
    candidates = []
    for i in range(1, col+1):
        candidates.extend(combinations(range(col),i))

    #유일성
    unique = []
    for candi in candidates:
        tmp = [tuple([item[i] for i in candi]) for item in relation]
        if len(set(tmp)) == row:
            unique.append(candi)

    #최소성
    answer = set(unique)
    for i in range(len(unique)):
        for j in range(i+1, len(unique)):
            if len(unique[i]) == len(set(unique[i]) & set(unique[j])):
                answer.discard(unique[j])
    return len(answer)


relation = [["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],
            ["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]

print(solution2(relation))