n = int(input())
space = [1,1]

roots = list(input().split())
for root in roots:
    plan = {'L': space[1] - 1, 'R': space[1] + 1, 'U': space[0] - 1, 'D': space[0] + 1}
    if plan[root] <= 0 or plan[root] > n:
        pass
    elif root=='L' or root=='R':
        space[1] = plan[root]
    elif root=='U' or root=='D':
        space[0] = plan[root]
for i in space:
    print(i,end = ' ')

