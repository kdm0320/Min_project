'''
두 자연수 A,B(A>B)에 대하여 A를 B로 나눈 나머지를 R이라고 했을때
A와 B의 최대공약수는 B와 R의 최대공약수와 같다
'''


def gcd(a,b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)

print(gcd(177,377))

def gcd_iter(a,b):
    temp_a  = max(a,b)
    temp_b = min(a,b)
    temp = 0
    while True:
        if temp_a % temp_b == 0:
            return temp_b
        else:
            temp = temp_a
            temp_a = temp_b
            temp_b = temp % temp_b


print(gcd_iter(177, 377))

