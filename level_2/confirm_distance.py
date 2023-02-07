# 거리 두기 확인하기 -> bfs 탐색 알고리즘
# k : 상수
# 시간 복잡도 O(k) 공간 복잡도 O(k)
import collections

ROOM_LENGTH = 5

# 갈수 있는지 없는지를 판단한다.
def can_go(y: int, x: int, place: list) -> bool:
    if 0 <= y < ROOM_LENGTH and 0 <= x < ROOM_LENGTH and place[y][x] != 'X':
        return True
    return False

# 파티션이 거리 두기를 지키는지 확인하는 함수
def obey_rule(y: int, x: int, place: list):
    que = collections.deque([[y, x, 0]])
    visited = set()
    visited.add((y, x))
    move = [[0, 1], [1, 0], [-1, 0], [0, -1]]
    # bfs 활용
    while que:
        _y, _x, distance = que.popleft()
        # 4방향으로 움직였을 때
        for my, mx in move:
            ny = _y + my
            nx = _x + mx
            if distance + 1 <= 2 and can_go(ny, nx, place) and (ny, nx) not in visited:
                if place[ny][nx] == 'P':
                    return False
                que.append([ny, nx, distance + 1])
                visited.add((ny, nx))
    return True

# place 에서 거리 두기를 지키는지 확인하는 함수
def confirm(place: list) -> int:
    for y in range(ROOM_LENGTH):
        for x in range(ROOM_LENGTH):
            # Partition 이 거리두기를 지키지 않고 있을 시
            if place[y][x] == 'P' and not obey_rule(y, x, place):
                return 0
    return 1


def solution(places: list) -> list:
    answer = []
    for place in places:
        answer.append(confirm(place))
    return answer
