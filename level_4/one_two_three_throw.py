# 1,2 ,3 떨구기
# 시간복잡도: O(N)

import collections

# 3의 개수를 최대한으로 늘려 1의 개수를 최소한으로 줄인다.
def dfs(target: int, counter: int) -> list:
    redundance = target - counter
    div, mod = divmod(redundance, 2)
    if mod == 0:
        return [3] * div + [1] * (counter - div)
    if mod == 1:
        return [3] * div + [2] * mod + [1] * (counter - div - mod)


def find_ways(past_ways: list, target: dict, past_ways_counter: dict) -> list:
    # 이번 경우에서 만족이 가능한지 확인
    for k in target:
        if not (past_ways_counter[k] <= target[k] <= past_ways_counter[k] * 3):
            return []
    # 떨어지는 순서를 정한다.
    answer = []
    past_way_orders = collections.defaultdict(list)
    # k 리프노드가 떨어지는 경우의 수 중 가장 사전순으로 느린 경우를 반환
    for k in past_ways_counter:
        past_way_orders[k] = dfs(target[k], past_ways_counter[k])
    # 답을 만든다.
    for p in past_ways:
        answer.append(past_way_orders[p].pop())
    return answer


def possible(past_ways: list, target: dict, past_ways_counter: dict) -> bool:
    new_target = [0] * len(target)

    for k in target:
        if target[k] < past_ways_counter[k]:
            return False
    return True


def solution(edges: list, target: list) -> list:
    answer = []
    # 타겟의 편의성을 위해 맨 앞에 [0] 을 추가
    target_dic = collections.defaultdict(int)
    for idx, t in enumerate(target):
        if t != 0:
            target_dic[idx + 1] = t
    total_node = len(target)
    # 그래프 생성
    graph = collections.defaultdict(list)
    for parent, child in edges:
        graph[parent].append(child)
    # 지나갈 길을 정리하고 graph를 정렬시킨다.
    ways = collections.defaultdict(int)
    max_ways = collections.defaultdict(int)
    for parent in graph:
        graph[parent].sort()
        ways[parent] = 0
        max_ways[parent] = len(graph[parent])
    # 과거의 길들을 기록하면서 나아간다
    past_ways = []
    past_ways_counter = collections.defaultdict(int)
    while possible(past_ways_counter, target_dic, past_ways_counter):
        # 길을 따라서 한 번 간다.
        parent = 1
        while parent in graph:
            going_way = ways[parent]
            ways[parent] = (going_way + 1) % max_ways[parent]
            parent = graph[parent][going_way]
        # parent 는 리프노드가 될 것이다.
        past_ways.append(parent)
        past_ways_counter[parent] += 1
        answer = find_ways(past_ways, target_dic, past_ways_counter)
        if answer:
            return answer
    return [-1]