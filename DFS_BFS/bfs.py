from collections import deque

def bfs(graph,start,visited):
    queue = deque([start])
    #현재 노드 방문 처리
    visited[start] = True
    #큐가 빌때까지 반복
    while queue:
        # 큐에서 하나의 원소를 뽑아 출력
        v = queue.popleft()
        print(v, end=' ')
        # 해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


graph = [
    [],
    [1,2],
    [2,3],
    [1,5],
    [5,2],
    [5,6],
    [4,7]


]
visited = [False]*8

bfs(graph,1,visited)