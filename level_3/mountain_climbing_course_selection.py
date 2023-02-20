# 등산 코스 정하기 -> 다익스트라 알고리즘
# 시간 복잡도 : O(n log n )
import heapq
import collections

MAX_DISTANCE = 10_000_001

graph = collections.defaultdict(list)
visited = []


def init(paths: list, n: int):
    global visited
    for v1, v2, w in paths:
        graph[v1].append([v2, w])
        graph[v2].append([v1, w])
    visited = [MAX_DISTANCE] * (n + 1)


def dijkstra(gates: list, summits: list) -> int:
    summits.sort()
    summits_set = set(summits)
    heap = []

    for gate in gates:
        heapq.heappush(heap, [0, gate])
        visited[gate] = 0

    while heap:
        weight, destination = heapq.heappop(heap)

        if destination in summits_set or visited[destination] < weight:
            continue

        for new_destination, distance in graph[destination]:
            new_intensity = max(distance, weight)

            if new_intensity < visited[new_destination]:
                heapq.heappush(heap, [new_intensity, new_destination])
                visited[new_destination] = new_intensity
    answer = [0, MAX_DISTANCE]

    for summit in summits:
        if answer[1] > visited[summit]:
            answer[0], answer[1] = summit, visited[summit]
    return answer

def solution(n: int, paths: list, gates: list, summits: list) -> list:
    init(paths, n)
    return dijkstra(gates, summits)


'''
# 등산 코스 정하기
import heapq
import collections
import sys

graph = collections.defaultdict(list)


def init(paths: list, n: int):
    for v1, v2, w in paths:
        graph[v1].append([v2, w])
        graph[v2].append([v1, w])


def solution(n: int, paths: list, gates: list, summits: list) -> list:
    answer = [sys.maxsize, sys.maxsize]
    init(paths, n)
    gates = set(gates)
    summits = set(summits)
    heap = []
    max_weight = 0
    visited = set()
    for gate in gates:
        heapq.heappush(heap, [0, gate])

    # 가장 시간이 적게 소요되는 지점으로 향한다.
    while heap:
        weight, destination = heapq.heappop(heap)
        max_weight = max(weight, max_weight)
        visited.add(destination)
        if max_weight > answer[1]:
            break
        # intensity 가 최소가 되는 destination
        if destination in summits:
            if answer[1] > max_weight or (answer[1] == max_weight and answer[0] > destination):
                answer[0], answer[1] = destination, max_weight
            continue
        for nd, w in graph[destination]:
            # gate 가 아니고 방문한 적도 없으면 heap 에 추가
            if nd not in visited:
                heapq.heappush(heap, [w, nd])
    return answer
'''
