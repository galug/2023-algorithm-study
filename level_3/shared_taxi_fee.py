# 합승 택시 요금 -> 플루이드 - 워셜 알고리즘
# N : 모든 노드의 개수
# 시간 복잡도 : O(N ** 3)


def init(n: int, fares: list) -> list:
    graph = [[float('inf')] * (n + 1) for _ in range(n + 1)]
    # 자기 자신에게서 자기 자신에게 가는 경우
    for i in range(n + 1):
        graph[i][i] = 0
    # c, d 까지의 거리 f
    for c, d, f in fares:
        graph[c][d] = f
        graph[d][c] = f
    return graph


# s : 출발 지점 , a : A의 도착 지점, b: B 의 도착 지점
def solution(n: int, s: int, a: int, b: int, fares: list) -> int:
    answer = float('inf')
    graph = init(n, fares)
    # 플루이드 - 워셜 알고리즘 통해서 모든 노드의 최소 길이를 구한다.
    for middle_v in range(1, n + 1):
        for start_v in range(1, n + 1):
            for end_v in range(1, n + 1):
                graph[start_v][end_v] = min(graph[start_v][end_v], graph[start_v][middle_v] + graph[middle_v][end_v])
    # 중간 까지 합승 후 각자의 목적지 까지 다시 타고 갈때 최솟값을 구한다.
    for middle_v in range(1, n + 1):
        answer = min(answer, graph[s][middle_v] + graph[middle_v][a] + graph[middle_v][b])

    return answer
