# 광고 삽입
# N : playtime
# 시간복잡도: O(N)

def convert_time_to_int(time: str) -> int:
    h, m, s = map(int, time.split(':'))
    return h * 3600 + m * 60 + s


def convert_int_to_time(num: int) -> str:
    h, num = divmod(num, 3600)
    m, s = divmod(num, 60)
    return '%02d:%02d:%02d' % (h, m, s)


def init(logs: list, play_time: int) -> list:
    result = [0] * (play_time + 1)
    for log in logs:
        start, end = map(convert_time_to_int, log.split('-'))
        result[start] += 1
        result[end] -= 1
    # 시간별 시청 사람
    for i in range(1, play_time + 1):
        result[i] += result[i - 1]
    # 시간까지의 시청자의 누적합
    for i in range(1, play_time + 1):
        result[i] += result[i - 1]
    return result


def solution(play_time: str, adv_time: str, logs: list) -> str:
    play_time = convert_time_to_int(play_time)
    adv_time = convert_time_to_int(adv_time)

    dp = init(logs, play_time)
    # 시간, 광고 효과
    answer = [0, dp[adv_time - 1]]

    for k in range(adv_time, play_time):
        if dp[k] - dp[k - adv_time] > answer[1]:
            answer[0], answer[1] = k - adv_time + 1, dp[k] - dp[k - adv_time]
    return convert_int_to_time(answer[0])
