# 후보키 문제
# N : columns 의 수 M : rows 의 수
# 시간 복잡도 : O(2 ** N * M)

import itertools


# 유일성 조건 확인 함수
def is_candidate_key(relations: list, columns: list) -> bool:
    total_candidate_keys = set()
    for relation in relations:
        temp = tuple([relation[column] for column in columns])
        # 칼럼 값이 동일한 릴레이션이 있는지 확인
        if temp in total_candidate_keys:
            return False
        total_candidate_keys.add(temp)
    return True


# 최소성 조건 확인 함수
def has_minimum_condition(answer: set, key: tuple) -> bool:
    for a in answer:
        if set(a) == set(a) & set(key):
            return True
    return False


def solution(relation: list) -> int:
    answer = set()
    number_of_columns = len(relation[0])
    columns = list(range(number_of_columns))
    # 모든 칼럼의 조합을 반복
    for number_of_combination in range(1, number_of_columns + 1):
        for combination in itertools.combinations(columns, number_of_combination):
            # 최소성 조건 확인
            if has_minimum_condition(answer, combination):
                continue
            # 유일성 조건 확인
            if is_candidate_key(relation, combination):
                answer.add(combination)
    return len(answer)

