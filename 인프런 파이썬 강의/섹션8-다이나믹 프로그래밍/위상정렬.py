
import time

# ------------ 내 풀이 코드 -----------------
answer = [1,6,2,5,4,3]
for i in answer:
    print(i, end=" ")
print()
# -----------영상 풀이 코드 -------------------
from collections import deque
start = time.time()
n = 6
m = 6
input_graph = [[1,4],[5,4],[4,3], [2,5], [2,3], [6,2]]
graph = [[0]*(n+1) for _ in range(n+1)]
degree =[0]*(n+1)
dq = deque()

for i in range(m):
    a,b = input_graph[i]
    graph[a][b] = 1
    degree[b]+=1
for i in range(1,n+1):
    if degree[i]==0:
        dq.append(i)

while dq:
    x = dq.popleft()
    print(x,end=" ")
    for i in range(1,n+1):
        if graph[x][i]==1:
            degree[i]-=1
            if degree[i]==0:
                dq.append(i)

print()
end = time.time()
print(f"{end - start:.5f} sec")