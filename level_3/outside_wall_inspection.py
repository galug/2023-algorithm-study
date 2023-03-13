# 외벽 점검
# N : dist 길이
# 시간복잡도: O(N!)
import itertools


def solution(n: int, weak: list, dist: list) -> int:
    dist_len = len(dist)
    weak = weak + [w + n for w in weak]
    len_weak = len(weak)
    for number_of_permutation in range(1, dist_len + 1):
        # 외벽 검사할 친구들 뽑기
        for friends in itertools.permutations(dist, number_of_permutation):
            # 외벽 검사를 시작할 위치 뽑기
            for start_count in range(len(weak) // 2):
                inspected_wall = set()
                # 친구 목록 가져오기
                for f in friends:
                    f_start = weak[start_count]
                    # 친구 시작 위치부터 검사할 수 있는 위치까지 검사
                    while start_count < len_weak and f_start <= weak[start_count] <= f_start + f:
                        inspected_wall.add(weak[start_count] % n)
                        start_count += 1
                    # start_count >= len_weak 일시 마지막 위치를 넘어간것이므로 통과
                    if start_count >= len_weak:
                        break
                # 검사한 외벽이 모든 weak 를 커버하면 반환
                if len(inspected_wall) == len_weak // 2:
                    return number_of_permutation
    # 모든 외벽 검사 결과가 실패할 경우
    return -1
