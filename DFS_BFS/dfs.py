
def dfs(graph,v,visited):
    #현재노드 방문처리
    visited[v] = True
    print(v,end=' ')
    #현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph,i,visited)


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
dfs(graph,1,visited)