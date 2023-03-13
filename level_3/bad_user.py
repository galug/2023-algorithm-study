# 불량 사용자
# N: len(user_id)
# 시간 복잡도: O(N!)
import itertools


def check(user: str, ban: str):
    if len(user) != len(ban):
        return False

    for u, b in zip(user, ban):
        if b == '*':
            continue
        if u != b:
            return False
    return True


def solution(user_id: list, banned_id: list) -> int:
    answer = []
    banned_length = len(banned_id)
    for c in itertools.permutations(user_id, banned_length):
        count = 0
        for u, b in zip(c, banned_id):
            if check(u, b):
                count += 1

        if count == banned_length:
            sc = set(c)
            if sc not in answer:
                answer.append(sc)
    return len(answer)
