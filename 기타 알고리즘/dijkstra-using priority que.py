import heapq
import  sys
INF = int(1e9)
input = sys.stdin.readline

#노드의 개수, 간선의 개수
n,m = map(int,input().split())
#시작노드
start = int(input())

# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트
graph = [[] for i in range(n+1)]

#모든 간선 정보
for _ in range(m):
    a,b,c = map(int, input().split())
    #a번 노드에서 b번 노드로 가는 비용이 c
    graph[a].append((b,c))

#최단거리 테이블
distance = [INF]*(n+1)


def dijkstra(start):
    q=[]
    #시작노드로 가기 위한 최단 경로는 0으로 설정하여,q에 삽입
    heapq.heappush(q, (0,start))
    distance[start] = 0
    while q: #큐가 비어있지 않다면
        #가장 최단 거리가 짧은 노드를 꺼낸다 dis:최단거리, now:노드
        dist,now = heapq.heappop(q)
        if distance[now]<dist:
            continue
        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in graph[now]:
            cost = dist+i[1] # 현재 노드를 거쳐서 다른 노드로 이동 하는 거리
            #현재 노드를 거쳐서, 다른 노드로 이동하는 거리(cost) 가 더 짧은 경유
            if cost<distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))


dijkstra(start)

for i in range(1,n+1):
    #도달할 수 없는 경우 "INFINITY" 출력
    if distance[i] == INF:
        print("INFINITY")
    #도달할 수 있는 경우 거리를 출력
    else:
        print(distance[i])




