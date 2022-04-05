def getMaxBarrier(initialEnergy, th):
    b = [0]*len(initialEnergy)
    s = []
    for i in range(th-2,th+1):
        for j in range(len(initialEnergy)):
            tmp = initialEnergy[j]-i
            if tmp <= 0:
                tmp = 0
                b[j] = tmp
        s.append(sum(b))
    answer = 0
    for i in s:
        if i >= th:
            pass
        else:
            answer = max(answer,i)
    return answer
initialEnergy = [5,2,13,10]
th = 8
print(getMaxBarrier(initialEnergy,th))