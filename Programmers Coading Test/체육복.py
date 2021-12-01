def solution(n, lost, reserve):
    set_reserve=set(reserve)-set(lost)
    set_lost = set(lost)-set(reserve)
    for i in set_reserve:
        if i-1 in set_lost:
            set_lost.remove(i-1)
        elif i+1 in set_lost:
            set_lost.remove(i+1)
    return n-len(set_lost)


    

n=3
lost = [3]
reserve = [1]

print(solution(n,lost,reserve))	
