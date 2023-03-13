# 보석 쇼핑 -> 투 포인터, 슬라이딩 윈도우
# N : len(gems )
# 시간 복잡도: O(N)
import sys
import collections


def solution(gems: list) -> list:
    gems_set = set(gems)
    # gems_set
    need = collections.Counter(gems_set)
    missing = len(gems_set)

    left = start = 0
    end = sys.maxsize

    for right, char in enumerate(gems):
        missing -= need[char] > 0
        need[char] -= 1

        if missing == 0:
            while left < right and need[gems[left]] < 0:
                need[gems[left]] += 1
                left += 1

            if right - left < end - start:
                start, end = left, right
                need[gems[left]] += 1
                missing += 1
                left += 1
    return [start + 1, end + 1]

    return answer