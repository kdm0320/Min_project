from collections import Counter


call="AbCDEfgHiAbCDEfgHiAbCDEfgHiAbCDEfgk"


def solution(call):
    answer = ""
    l_c =call.lower()
    m_c = Counter(l_c).most_common()
    tmp = []
    m = m_c[0][1]
    for i in m_c:
        if i[1] < m:
            break
        else:
            tmp.append(i[0])
    for i in call:
        if i.lower() not in tmp:
            answer+=i
    return answer

print(solution(call))
