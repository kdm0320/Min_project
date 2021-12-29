from math import pow

def solution(n):
    rev_base = ''
    q=3
    while n > 0:
        n, mod = divmod(n, q)
        rev_base += str(mod)


    return int(rev_base,3)

n=45
print(solution(n))