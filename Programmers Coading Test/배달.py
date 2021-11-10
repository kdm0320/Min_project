import heapq
N = 5
road = [[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]]
K = 3



def solution(N, road, K):
    answer = 0
    graph = [[] for i in range(N + 1)]
    INF = int(1e9)
    road.sort()
    distance = [INF] * (N + 1)
    for i in road:
        graph[i[0]].append((i[1], i[2]))
        graph[i[1]].append((i[0],i[2]))

    q = []
    heapq.heappush(q, (0, 1))
    distance[1] = 0

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

    for i in range(1, N + 1):
        if distance[i] <= K:
            answer += 1
    return answer

print(solution(N,road,K))