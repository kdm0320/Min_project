
s = "aabbaccc"

def solution(s):
    result = []
    if len(s)==1:
        return 1
    for slicing in range(1,len(s)//2+2):
        res = ''
        cnt = 1
        tmp = s[:slicing]

        for i in range(slicing,len(s),slicing):
            if tmp == s[i:i+slicing]:
                cnt+=1
            else:
                if cnt == 1:
                    res+=tmp
                else:
                    res = res+str(cnt)+tmp
                tmp = s[i:i+slicing]
                cnt=1
        if cnt == 1:
            res+=tmp
        else:
            res = res+str(cnt)+tmp

        result.append(len(res))
    return min(result)


print(solution(s))