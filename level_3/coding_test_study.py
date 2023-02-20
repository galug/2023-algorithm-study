# 코딩 테스트 공부 -> dp 풀이
# n : alp 길이, m : cop 길이, p: problems 의 길이( 6 이하라 무시해도 무방할듯?)
# 시간 복잡도:O( n * m * p)
import sys


def solution(alp: int, cop: int, problems: list) -> int:
    max_alp, max_cop = 0, 0

    for problem in problems:
        max_alp, max_cop = max(max_alp, problem[0]), max(max_cop, problem[1])

    if alp >= max_alp and cop >= max_cop:
        return 0
    # alp, cop 를 max_alp, max_cop 값을 넘을 경우 값을 조정 -> 이 부분에서 애 먹음
    alp, cop = min(alp, max_alp), min(cop, max_cop)
    # dp 를
    dp = [[float('inf')] * (max_cop + 1) for _ in range(max_alp + 1)]
    dp[alp][cop] = 0
    for cur_alp in range(alp, max_alp + 1):
        for cur_cop in range(cop, max_cop + 1):
            if cur_alp < max_alp:
                dp[cur_alp + 1][cur_cop] = min(dp[cur_alp + 1][cur_cop], dp[cur_alp][cur_cop] + 1)
            if cur_cop < max_cop:
                dp[cur_alp][cur_cop + 1] = min(dp[cur_alp][cur_cop + 1], dp[cur_alp][cur_cop] + 1)
            for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
                if cur_alp >= alp_req and cur_cop >= cop_req:
                    new_alp_rwd = min(cur_alp + alp_rwd, max_alp)
                    new_cop_rwd = min(cur_cop + cop_rwd, max_cop)
                    dp[new_alp_rwd][new_cop_rwd] = min(dp[new_alp_rwd][new_cop_rwd], dp[cur_alp][cur_cop] + cost)

    return dp[max_alp][max_cop]
