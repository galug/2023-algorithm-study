# 양궁 대회 문제 -> 완전 탐색 알고리즘(재귀 함수)
# k = 352716(완전 탐색에 걸리는 상수)
# 시간 복잡도 O(k) 공간 복잡도 O(10k)
import collections

info_scores = collections.defaultdict(int)
answer = []
max_score = 0


# 초기화
def init(info: list) -> int:
    total_info_score = 0
    for info_idx, number_of_hit in enumerate(info):
        info_scores[10 - info_idx] = number_of_hit
        total_info_score += (10 - info_idx) if number_of_hit > 0 else 0
    return total_info_score


def dfs(n: int, peach_score: int, my_score: int, target_score, result: list):
    global answer
    global max_score
    # 0 점 미만의 점수는 쏠수 없다.
    if target_score < 0:
        return
    # 0점인 상태에서 쏠 화살이 남아 있는 경우 화살을 소비해야함.
    if target_score == 0 and n > 0:
        result[10] = n
        #
        if max_score < my_score - peach_score:
            answer = result[::]
            max_score = my_score - peach_score
        if max_score == (my_score - peach_score) and tuple(reversed(answer)) < tuple(reversed(result)):
            answer = result[::]
        result[10] = 0
        return
    # peach 의 점수를 이겼고 모든 화살을 소비했을 때
    if n == 0 and peach_score < my_score:
        if max_score < my_score - peach_score:
            answer = result[::]
            max_score = my_score - peach_score
            return
        if max_score == (my_score - peach_score) and tuple(reversed(answer)) < tuple(reversed(result)):
            answer = result[::]
            return
    # 자신의 점수보다 낮은 점수에 대해서 탐색
    for next_target in range(target_score, 0, -1):
        # 점수를 얻기 위한 최소 화살 수 조건 (어피치 보다 한 발을 더 쏴야한다.)을 만족 시
        if n - info_scores[next_target] - 1 >= 0:
            # 피치의 화살이 점수를 맞힌 경우
            if info_scores[next_target] > 0:
                result[10 - next_target] = info_scores[next_target] + 1
                dfs(n - info_scores[next_target] - 1, peach_score - next_target, my_score + next_target,
                    next_target - 1, result)
                result[10 - next_target] = 0
            # 피치의 화살이 점수를 맞히지 않은 경우
            if info_scores[next_target] == 0:
                result[10 - next_target] = 1
                dfs(n - 1, peach_score, my_score + next_target, next_target - 1, result)
                result[10 - next_target] = 0
        dfs(n, peach_score, my_score, next_target - 1, result)


def solution(n: int, info: list) -> list:
    # 초기화
    info_score = init(info)
    result = [0] * 11
    dfs(n, info_score, 0, 10, result)
    # 라이언이 우승할 수 없는 경우
    if max_score == 0:
        return [-1]
    return answer

