# 매출하락 최소화 -> dp + tree

import collections
import sys

ROOT = 1

def solution(sales: list, links: list) -> int:
    # dfs 를 통한 트리 열기
    def dfs(root: int, include: int) -> int:
        # dp 존재하면 반환
        if dp[include][root] != -1:
            return dp[include][root]
        # 본인 포함 경우
        if include == 1:
            answer = sales[root]
            for child in tree[root]:
                answer += min(dfs(child, 1), dfs(child, 0))
        # 본인 포함 x 경우
        else:
            answer = 0
            has_include_child = False
            max_dif = sys.maxsize
            for child in tree[root]:
                include_child, not_include_child = dfs(child, 1), dfs(child, 0)
                # child 가 참석을 한명이라도 하는 경우
                if include_child <= not_include_child:
                    has_include_child = True
                # child 가 참석을 안하는 경우
                else:
                    max_dif = min(include_child - not_include_child, max_dif)
                answer += min(include_child, not_include_child)
            # child 가 참석을 한 명도 안한 경우 최소 값을 더해준다.
            if not has_include_child:
                answer += max_dif
        dp[include][root] = answer
        return answer
    # 초기 세팅
    sales = [0] + sales
    tree = collections.defaultdict(list)
    for up, down in links:
        tree[up].append(down)
    dp = [[-1] * len(sales)  for _ in range(2)]
    # 리프노드 골라내기
    for node in range(len(sales)):
        if node not in tree:
            dp[0][node] = 0
            dp[1][node] = sales[node]
    # 자식이 없는 경우 중 최소값
    dfs(ROOT, 0)
    dfs(ROOT, 1)
    return min(dp[0][ROOT], dp[1][ROOT])
'''
def solution(sales: list, links: list) -> int:
    # dfs 를 통한 트리 열기
    def dfs(root: int, include: int) -> int:
        # dp 존재하면 반환
        if dp[include][root] != -1:
            return dp[include][root]
        answer = sys.maxsize
        # 자식 모두 포함 x 경우 고려
        if include == 1:
            temp = sales[root]
            # 자식 모두 포함 x 경우
            for child in tree[root]:
                temp += dfs(child, 0)
            if temp < answer:
                dp[include][root] = temp
                answer = temp
        # 자식으로 조합 짜기
        for combi_num in range(1, len(tree[root]) + 1):
            for c in itertools.combinations(tree[root], combi_num):
                temp = sales[root] if include == 1 else 0
                # 자식 포함 경우와 포함 x 경우를 모두 고려하여 더해줌
                for child in tree[root]:
                    if child in c:
                        temp += dfs(child, 1)
                        continue
                    temp += dfs(child, 0)
                if temp < answer:
                    dp[include][root] = temp
                    answer = temp
        return answer
    # 초기 세팅
    sales = [0] + sales
    tree = collections.defaultdict(list)
    for up, down in links:
        tree[up].append(down)
    dp = [[-1] * len(sales)  for _ in range(2)]
    # 리프노드 골라내기
    for node in range(len(sales)):
        if node not in tree:
            dp[0][node] = 0
            dp[1][node] = sales[node]
    # 자식이 없는 경우 중 최소값
    dfs(ROOT, 0)
    dfs(ROOT, 1)
    return min(dp[0][ROOT], dp[1][ROOT])
'''