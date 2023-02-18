# 미로 탈출 명령어 -> 재귀 탐색
import sys
# 주의: 파이썬은 재귀 탐색의 limit 가 제한 되어 있기 때문에 이런식으로 제한을 풀지 않을 시 런타임 에러 발생가능
sys.setrecursionlimit(10 ** 5)

MIN_VERTICAL, MAX_VERTICAL = 1, sys.maxsize
MIN_HORIZONTAL, MAX_HORIZONTAL = 1, sys.maxsize
MOVING_DISTANCE = 0
DESTINATION_X, DESTINATION_Y = 0, 0

moving = [(1, 0, 'd'), (0, -1, 'l'), (0, 1, 'r'), (-1, 0, 'u')]
answer = ''

# 초기화
def init(n: int, m: int, r: int, c: int, k: int):
    global MAX_VERTICAL, MAX_HORIZONTAL, MOVING_DISTANCE, DESTINATION_X, DESTINATION_Y
    MAX_VERTICAL = n
    MAX_HORIZONTAL = m
    MOVING_DISTANCE = k
    DESTINATION_X = r
    DESTINATION_Y = c

# 미궁 안의 위치인지 확인하는 함수
def is_in_maze(y: int, x: int):
    if y < 1 or y > MAX_VERTICAL or x < 1 or x > MAX_HORIZONTAL:
        return False
    return True

def dfs(x: int, y: int, k: int, route: str) -> bool:
    if k > MOVING_DISTANCE:
        return False
    # 더 이상 움직이는
    if abs(x - DESTINATION_X) + abs(y - DESTINATION_Y) + k == MOVING_DISTANCE:
        global answer
        if DESTINATION_X - x > 0:
            route += ('d' * (DESTINATION_X - x))
        if y - DESTINATION_Y > 0:
            route += ('l' * (y - DESTINATION_Y))
        if y - DESTINATION_Y < 0:
            route += ('r' * (DESTINATION_Y - y))
        if DESTINATION_X - x < 0:
            route += ('u' * (x - DESTINATION_X))
        answer = route
        return True
    # d, l, r, u 로 사전 순으로 탐색
    for mx, my, direction in moving:
        nx, ny = x + mx, y + my
        if is_in_maze(nx, ny):
            if dfs(nx, ny, k + 1, route + direction):
                return True


def solution(n: int, m: int, x: int, y: int, r: int, c: int, k: int) -> str:
    global answer
    init(n, m, r, c, k)
    min_length = abs(x - r) + abs(y - c)
    # 도착이 불가능한 경우
    if min_length > k or min_length % 2 != k % 2:
        return 'impossible'
    dfs(x, y, 0, '')
    return answer


'''
시간 초과 풀이 O(4 ** k)
def solution(n: int, m: int, x: int, y: int, r: int, c: int, k: int) -> str:
    answer = ''
    init(n, m)
    min_length = abs(x - r) + abs(y - c)
    if min_length > k or min_length % 2 != k % 2:
        return 'impossible'

    moving = [[1, 0, 'd'], [0, -1, 'l'], [0, 1, 'r'], [-1, 0, 'u']]
    que = collections.deque([[x, y, 0, '']])
    # d l r u 순으로 탐색
    while que:
        x_, y_, k_, routes = que.popleft()
        if x_ == r and y_ == c and k_ == k:
            answer = routes
            break
        for mx, my, mr in moving:
            nx, ny = x_ + mx, y_ + my
            if nx < 1 or nx > MAX_VERTICAL or ny < 1 or ny > MAX_HORIZONTAL:
                continue
            que.append([nx, ny, k_ + 1, routes + mr])
    return answer
'''
