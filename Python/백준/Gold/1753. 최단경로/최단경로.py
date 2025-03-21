import sys
import heapq

input = sys.stdin.readline
INF = float("inf")

V, E = map(int, input().split())
start = int(input().strip())

# 인접 리스트를 이용한 그래프 구현
graph = [[] for _ in range(V + 1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

# 최단 거리를 저장할 배열 초기화
distance = [INF] * (V + 1)
distance[start] = 0

pq = []
heapq.heappush(pq, (0, start))

while pq:
    dist, cur = heapq.heappop(pq)
    # 이미 더 짧은 경로가 존재하면 무시
    if distance[cur] < dist:
        continue
    for next_node, weight in graph[cur]:
        new_dist = dist + weight
        if new_dist < distance[next_node]:
            distance[next_node] = new_dist
            heapq.heappush(pq, (new_dist, next_node))

# 결과 출력 (도달할 수 없는 경우 "INF" 출력)
for i in range(1, V + 1):
    print("INF" if distance[i] == INF else distance[i])
