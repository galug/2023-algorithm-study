# 동굴 탐험 -> que 를 이용한 풀이
# 시간복잡도: O(N)

import collections

ROOT = 0


def solution(n: int, path: list, order: list) -> bool:
    # 그래프 초기화 
    graph = [[] for _ in range(n)]
    for v1, v2 in path:
        graph[v1].append(v2)
        graph[v2].append(v1)
    # 순서 dictionary 및 set 화 
    temp = {}
    starts = {}
    for s, e in order:
        temp[e] = s
        starts[s] = e
    order = temp
    # 시작위치는 무조건 0이어야한다.
    if 0 in order and order[0] != 0:
        return False
    # 큐를 이용한 풀이 
    que = collections.deque()
    que.append(ROOT)
    visited = [False] * (n)
    visited[0] = True
    will_visit = set()
    while que:
        parent = que.popleft()
        # 모든 자식을 검사 
        for child in graph[parent]:
            # 들른 곳 넘어가기 
            if visited[child]:
                continue
            # 키를 방문하지 않은 곳 will_visit 에 넣는다.
            if child in order and not visited[order[child]]:
                will_visit.add(child)
                continue
                # 키를 방문할 경우 will_visit 를 확인하고 풀어준다.
            if child in starts:
                if starts[child] in will_visit:
                    que.appendleft(starts[child])
                    visited[starts[child]] = True
            # 키거나 일반 노드이면 통과한다. 
            que.appendleft(child)
            visited[child] = True
    return False if False in visited else True


'''
def solution(n: int, path: list, order: list) -> bool:
    # 그래프 초기화 
    graph = [[] for _ in range(n)]
    for v1, v2 in path:
        graph[v1].append(v2)
        graph[v2].append(v1)
    # 순서 dictionary 및 set 화 
    temp = {}
    starts = set()
    for s, e in order:
        temp[e] = s
        starts.add(s)
    order = temp
    # 리프 노드 찾기
    leaf_nodes = set()
    for node in range(n):
        if len(graph[node]) == 1:
            leaf_nodes.add(node)
    # 함수 
    def dfs(cur_pos: int, parent: int, visited: set):
        # order ends 일 때 start를 들른 적이 없다면 반환 
        if cur_pos in order and order[cur_pos] not in visited:
            return 
        visited.add(cur_pos)
        # 리프노드면 반환
        if cur_pos in leaf_nodes:
            return
        # 자식들을 추가해나가기
        for related_node in graph[cur_pos]:
            # 부모를 다시 
            if related_node == parent:
                continue
            dfs(related_node, cur_pos, visited)
    visited = set()
    while True:
        temp = visited.copy()
        dfs(0, -1, visited)
        if temp == visited:
            return False
        if len(visited) == n:
            return True
'''