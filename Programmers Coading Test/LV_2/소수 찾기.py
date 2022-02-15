import math, itertools


#수 하나의 소수 판별
def is_prime_number(x):
    #2부터 x의 제곱근까지의 모든 수를 확인하며
    for i in range(2, int(math.sqrt(x)) + 1):
        #x가 해당 수로 나누어떨어진다면
        if x % i == 0:
            return False #소수가 아님
    return True


def solution(numbers):
    answer = 0
    nums = []
    length = 1
    while length <= len(numbers):
        comb = itertools.permutations(numbers, length)
        for i in comb:
            a = int("".join(i))
            if a not in nums:
                nums.append(a)
        length+=1
    for i in nums:
        if is_prime_number(i) and i > 1:
            answer+=1
    return answer
numbers = "17"

print(solution(numbers))
