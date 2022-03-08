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
        for index,i in enumerate(graph[v]):
            if not visited[index]:
                if i:
                    queue.append(index)
                    visited[index] = True

def solution(n, computers):
    visited = [False]*n
    answer=0
    for i in range(len(computers)):
        if not visited[i]:
            bfs(computers,i,visited)
            answer+=1
    return answer


n = 3
computers =[[1, 1, 0], [1, 1, 1], [0, 1, 1]]

print(solution(n,computers))