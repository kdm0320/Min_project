t = int(input())

stairs = []
A = []
for _ in range(t):
    num = list(map(int, input().split()))
    num1 = num
    stairs.append(num)
    A.append(tuple(num))

for i in range(1,t):
    a = i
    for j in range(i+1):
        b = j
        if j == 0:
            up_left = 0
        else:
            up_left = stairs[i-1][j-1]
        if j==i:
            up = 0
        else:
            up = stairs[i-1][j]
        stairs[i][j] = stairs[i][j] + max(up_left,up)
print(max(stairs[t-1]))