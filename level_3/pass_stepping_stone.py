# 징검 다리 건너기 -> 이분 탐색 통한 풀이
# O(N)

STONE_LENGTH = 0


# 지나갈 수 있는지 판단하기
def can_pass(stones: list, k: int, stone: int) -> bool:
    count = 0
    for i in range(STONE_LENGTH):
        if stones[i] <= stone:
            count += 1
        else:
            count = 0
        # count 의 개수가 k 개가 되면
        if count == k:
            return False
    return True


def solution(stones: list, k: int) -> int:
    global STONE_LENGTH
    STONE_LENGTH = len(stones)
    start, end = 1, 200_000_000
    # 이분 탐색
    while start <= end:
        mid = (start + end) // 2
        if can_pass(stones, k, mid):
            start = mid + 1
        else:
            end = mid - 1
    return start
