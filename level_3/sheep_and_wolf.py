# 양과 늑대 -> bfs + 메모제이션 기법 이용한 풀이
# n: len(info)
# 시간복잡도 : O(2 ** n)
import collections

graph = []


# 그래프를 초기화
def init(info: list, edges: list):
    global graph
    graph_size = len(info)
    graph = [[] for _ in range(graph_size)]
    for v1, v2 in edges:
        graph[v1].append(v2)
        graph[v2].append(v1)


def bfs(info: list):
    # que 에는 그동안 방문한 곳, 양의 수, 늑대의 수가 들어간다.
    que = collections.deque([({0}, 1, 0, 1)])
    answer = 0
    # 같은 visited 를 두 번 반복하지 않기 위한 dp
    dp = [False for _ in range(1 << len(info))]
    dp[1] = True
    while que:
        visited, sheep, wolf, bit = que.popleft()
        answer = max(answer, sheep)
        # 방문한 곳을 모두 다시 탐색해야한다.
        for v in visited:
            for nv in graph[v]:
                new_bit = bit | (1 << nv)
                if info[nv] == 0 and nv not in visited and not dp[new_bit]:
                    dp[new_bit] = True
                    que.append((visited | {nv}, sheep + 1, wolf, new_bit))
                if info[nv] == 1 and nv not in visited and sheep > wolf + 1 and not dp[new_bit]:
                    dp[new_bit] = True
                    que.append((visited | {nv}, sheep, wolf + 1, new_bit))
    return answer


def solution(info: list, edges: list) -> int:
    init(info, edges)
    return bfs(info)
