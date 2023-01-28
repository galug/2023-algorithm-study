# 실패율
# M : 사용자의 수(len(stages))
# 시간 복잡도 : O(M log M) 공간 복잡도 : O(M)
import collections


def solution(N: int, stages: list) -> list:
    # stages 에서 사용자가 도전중인 각 스태이지의 개수를 세준다.
    counter = collections.Counter(stages)
    number_of_user = len(stages)
    # 스태이지 별로 사용자의 실패율을 기록한다.
    failure_rate = []
    for stage in range(1, N + 1):
        if stage in counter:
            failure_rate.append((stage, counter[stage] / number_of_user))
            number_of_user -= counter[stage]
        else:
            failure_rate.append((stage, 0))
    # 실패율을 내림 차순으로 정렬한다. 실패율이 같을 시 stage 의 오름차순은 stable sort 이므로 확보된다.
    failure_rate.sort(key=lambda x: x[1], reverse=True)
    # lambda 식을 이용 stage 의 값만 뽑아낸다.
    return list(map(lambda x: x[0], failure_rate))


