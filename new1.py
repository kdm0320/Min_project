

import decimal

def solution(sentences, n):
    answer =0
    s_set = set()
    for sen in sentences:
        in_alpha = False
        f_set = set()
        n_set = 0
        for s in sen:
            if s.isupper():
                in_alpha=True
            s.lower()
            if s.isspace():
                continue
            f_set.add(s.lower())
        if in_alpha:
            n_set+=1
        n_set+=len(f_set)
        if n_set > n:
            continue
        else:
            tmp =0
            for s in sen:
                tmp+=1
                if s.isupper():
                    tmp+=1
            if s_set & f_set == f_set:
                answer+=tmp
            else:
                if answer < tmp:
                    s_set.clear()
                    s_set=s_set.union(f_set)
                    answer = tmp


    return answer

sentences =["ABcD", "bdbc", "a", "Line neWs"]
n = 5
print(solution(sentences,n))