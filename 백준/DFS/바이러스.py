import sys
#여러줄 입력할때 input() 대신  sys.stdin.readline() 사용
from collections import deque

def bfs(graph,start,visited):
    queue = deque([start])
    #현재 노드 방문 처리
    visited[start] = True
    #큐가 빌때까지 반복
    while queue:
        # 큐에서 하나의 원소를 뽑아 출력
        v = queue.popleft()
        # print(v, end=' ')
        # 해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

def dfs(graph,n,visited):
    visited[n] = 1
    for i in graph[n]:
        if not visited[i]:
            dfs(graph,i,visited)


c = int(input())
c_pair = int(input())
visited = [0]*(c+1)
graph = [[] for _ in range(c+1)]
for _ in range(c_pair):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
bfs(graph,1,visited)
print(sum(visited)-1)