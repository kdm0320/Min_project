def getMaxBarrier(initialEnergy, th):
    b = [0]*len(initialEnergy)
    k=0
    while True:
       for i in range(len(initialEnergy)):
            tmp = initialEnergy[i]-k
            if tmp <= 0:
                tmp = 0
            b[i] = tmp
       if sum(b) == th:
            return k
       elif sum(b) < th:
           return k-1
       else:
            k+=1

initialEnergy = [5, 2, 13, 10]
th = 8

print(getMaxBarrier(initialEnergy,th))