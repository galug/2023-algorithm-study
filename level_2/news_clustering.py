# 뉴스 클러스터링 -> dictionary 이용
# N: 가장 긴 문자열의 길이
# 시간 복잡도 : O(N)
import collections

MULTIPLY_NUMBER = 65536
str1_set, str2_set = collections.defaultdict(int), collections.defaultdict(int)
total_keys = set()

# 각각의 집합을 초기화
def init(str1: str, str2: str):
    global total_keys
    for idx in range(len(str1) - 1):
        if str1[idx].isalpha() and str1[idx + 1].isalpha():
            str1_set[str1[idx: idx + 2].lower()] += 1
    for idx in range(len(str2) - 1):
        if str2[idx].isalpha() and str2[idx + 1].isalpha():
            str2_set[str2[idx: idx + 2].lower()] += 1
    total_keys = set(str1_set.keys()) | set(str2_set.keys())


def solution(str1: str, str2: str) -> int:
    init(str1, str2)
    if len(total_keys) == 0:
        return MULTIPLY_NUMBER
    total_union, total_intersection = 0, 0
    # 합집합, 교집합 구하기
    for k in total_keys:
        total_union += max(str1_set[k], str2_set[k])
        total_intersection += min(str1_set[k], str2_set[k])
    return int(MULTIPLY_NUMBER * (total_intersection / total_union))
