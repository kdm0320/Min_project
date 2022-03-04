
def check(number):
    if number%2==0:
        num = number //2
        return num
    else:
        num = (number+1)//2
        return num


def solution(n,a,b):
    answer = 1
    while True:
        if abs(a-b) == 1 and max(a,b)%2==0:
            return answer
        else:
            a = check(a)
            b = check(b)
            answer+=1


n=8
a=4
b=5

print(solution(n,a,b))