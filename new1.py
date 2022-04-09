tstring = "{a} {b} {c} {d} {i}"
variables = [["b","{c}"],["a","{b}"],["e","{f}"],["h","i"],["d","{e}"],["f","{d}"],["c","d"]]

def solution(tstring, variables):
    answer =""
    tmp = tstring
    v=""
    g=[tstring]
    h={}
    for i in variables:
        a,b=i
        h[a] = b
    ch=False
    while True:
        for i in tmp:
            if i=="{":
                ch=True
                continue
            elif i=="}":
                ch=False
                if v in h.keys():
                    answer+=h[v]
                    v=""

                else:
                    answer+="{"+v+"}"
                    v=""
            else:
                if ch:
                    v+=i
                else:
                    answer+=i
        if answer in g:
            return answer
        else:
            g.append(answer)
            tmp=answer
            answer = ""

print(solution(tstring,variables))