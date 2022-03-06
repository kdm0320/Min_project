n = int(input())
lis=[]
for _ in range(n):
    lis.append(input().split())

lis.sort(key=lambda x : (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for i in lis:
    print(i[0])
