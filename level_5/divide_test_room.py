import collections


def dfs(dp: list, graph: list, parent: int, num: list) -> int:
    if not graph[parent]:
        dp[parent] = num[parent]
        return num[parent]
    cur_sum = num[parent]
    for child in graph[parent]:
        cur_sum += dfs(dp, graph, child, num)
    dp[parent] = cur_sum
    return cur_sum


def parametric_search(dp: list, graph: list, root: int, search_num: int, k: int) -> bool:
    que = [root, dp[root]]
    while k > 0:
        root, total_tree = que.popleft()
        if total_tree > search_num:

    return True


def solution(k: int, num: list, links: list):
    answer = 0
    number_of_tester = len(num)
    graph = [[] for _ in range(number_of_tester)]
    childs = set()
    # 그룹이 한 개 인 경우 total 반환
    total_tree = sum(num)
    if k == 1:
        return total_tree
    # 그래프 초기화
    for parent, link in enumerate(links):
        if link[0] != -1:
            graph[parent].append(link[0])
            childs.add(link[0])
        if link[1] != -1:
            graph[parent].append(link[1])
            childs.add(link[1])
    # 루트 노드 찾기
    root = -1
    for i in range(number_of_tester):
        if i not in childs:
            root = i
            break
    # dp 에 기록
    dp = [0 for _ in range(number_of_tester)]
    dfs(dp, graph, root, num)
    # 이진 탐색 과 parametric search를 사용
    low, high = 1, total_tree
    while low < high:
        middle = (low + high) // 2
        if parametric_search(dp, graph, root, middle, k):
            high = middle - 1
        else:
            low = middle + 1
    return low