import math


#수 하나의 소수 판별
def is_prime_number(x):
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

#여러개의 수가 소수인지 아닌지를 판별 - 에라토스테네스의 체
#N보다 작거나 같은 모든 소수를 찾을 때 사용 가능

def eratostenes(n):
    array = [True for i in range(n+1)]

    for i in range(2, int(math.sqrt(n))+1):
        if array[i] == True:

            j = 2
            while i*j <= n:
                array[i*j] = False
                j += 1

    for i in range(2,n+1):
        if array[i]:
            print(i,end=' ')