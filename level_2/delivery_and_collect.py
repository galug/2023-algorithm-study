# 택배 배달과 수거하기 -> 스택을 이용한 풀이
# n: 집의 숫자
# 시간 복잡도 : O(n) 공간 복잡도 : O(n)

deliveries_stack = []
pickups_stack = []

# 초기화를 위한 함수
def init(n: int, deliveries: list, pickups: list):
    for distance in range(n):
        if deliveries[distance] != 0:
            deliveries_stack.append([distance + 1, deliveries[distance]])
        if pickups[distance] != 0:
            pickups_stack.append([distance + 1, pickups[distance]])

# 이동 거리를 찾기 위한 함수
def find_max_distance() -> int:
    if deliveries_stack and pickups_stack:
        return max(deliveries_stack[-1][0], pickups_stack[-1][0])
    if deliveries_stack:
        return deliveries_stack[-1][0]
    return pickups_stack[-1][0]

# 배달을 위한 함수
def delivery(cap: int):
    # 배달할 곳이 없으면 return
    if not deliveries_stack:
        return
    # 배달할 곳에 배달할 물건이 수용량보다 많은 경우
    if deliveries_stack[-1][1] > cap:
        deliveries_stack[-1][1] -= cap
        return
    # 배달 완료, 다음 집으로
    delivery(cap - deliveries_stack.pop()[1])

# 수거를 위한 함수
def pickup(cap: int):
    # 수거할 곳이 없으면 return
    if not pickups_stack:
        return
    # 수거할 곳에 수거할 물건이 수용량보다 많은 경우
    if pickups_stack[-1][1] > cap:
        pickups_stack[-1][1] -= cap
        return
    # 수거 완료, 다음 집으로
    pickup(cap - pickups_stack.pop()[1])


def solution(cap: int, n: int, deliveries: list, pickups: list):
    answer = 0
    init(n, deliveries, pickups)
    while deliveries_stack or pickups_stack:
        # 최대 거리만큼 왔다 갔다하므로 2배
        answer += (2 * find_max_distance())
        delivery(cap)
        pickup(cap)
    return answer


