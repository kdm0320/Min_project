
dirs = "ULURRDLLU"


def solution(dirs):
    answer = 0
    now = [0,0]
    trace = [[] for _ in range(len(dirs)+1)]
    has = {"R":1, "L":-1, "U":1,"D":-1}
    j=0
    for i in dirs:
        trace[j].append(tuple(now))
        if i == "R" or i=="L":
            check0 = now[0]+has[i]
            if 5<check0 or check0 < -5:
                continue
            else:
                now[0]+=has[i]
                trace[j].append(tuple(now))
        else:
            check1 = now[1]+has[i]
            if 5<check1 or check1 < -5:
                continue
            else:
                now[1]+=has[i]
                trace[j].append(tuple(now))
        print(now)
        print(trace)
        if j==0 or trace[j] not in trace[0:j-1]:
            answer+=1
        j+=1
        print(answer)
    return answer
         
    
print(solution(dirs))
