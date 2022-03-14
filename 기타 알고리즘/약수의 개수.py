n = int(input())


def count(x):
    num = 0
    for i in range(1,x+1):
        if x%i == 0:
            num+=1
    return num

print(count(n))