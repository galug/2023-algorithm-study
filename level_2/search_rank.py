# 순위 검색
# N : len(info) M : len(query)
# 시간 복잡도 : O(N + M) 공간 복잡도 : O(N)
import collections
import itertools
from bisect import bisect_left

condition_selections = collections.defaultdict(list)


# 초기화
def init(information: list):
    for info in information:
        split = info.split()
        conditions = split[:4]
        score = int(split[4])
        # combinations 를 이용 모든 경우의 수를 구하고 value 에 score 를 집어넣음
        for num_of_combinations in range(5):
            for cb in itertools.combinations([0, 1, 2, 3], num_of_combinations):
                temp = conditions.copy()
                for ele in cb:
                    temp[ele] = '-'
                condition_selections[''.join(temp)].append(score)
    # value 를 이진 탐색하기 위한 정렬
    for k in condition_selections:
        condition_selections[k].sort()

# search 함수
def search(query: str) -> int:
    query_conditions = query.split(' and ')
    query_conditions[3], score = query_conditions[3].split()
    condition = ''.join(query_conditions)
    return len(condition_selections[condition]) - bisect_left(condition_selections[condition], int(score))


def solution(info: list, query: list) -> list:
    init(info)
    return [search(q) for q in query]


'''
초반 내 풀이 
효율성에서 떨어짐 
condition_selections = collections.defaultdict(set)
scores = []

# 초기화
def init(information: list):
    for idx, info in enumerate(information):
        conditions = info.split()
        for condition_idx, condition, in enumerate(conditions):
            if condition_idx == 4:
                scores.append((int(condition), idx))
                continue
            condition_selections[condition].add(idx)
    scores.sort()

# 바이너리 서치 구현 
def binary_score_search(min_condition: int, number_of_info: int) -> set:
    low, high = 0, number_of_info - 1
    while low <= high:
        mid = (low + high) // 2
        if scores[mid][0] < min_condition:
            low = mid + 1
        else:
            high = mid - 1
    return low


def search(query: str, number_of_info: int) -> int:
    conditions = query.split(' and ')
    conditions[3], score = conditions[3].split()
    score = int(score)
    meet_to_condition = set(map(lambda x: x[1], scores[binary_score_search(score, number_of_info):]))
    for condition in conditions:
        if condition != '-':
            meet_to_condition &= condition_selections[condition]
    return len(meet_to_condition)


def solution(info: list, query: list) -> list:
    answer = []
    init(info)
    number_of_info = len(info)
    for q in query:
        answer.append(search(q, number_of_info))
    return answer
'''
