# 사라지는 발판
# 시간복잡도: O( 4** n) ?

import sys

sys.setrecursionlimit(100000000)

VERTICAL, HORIZONTAL = 0, 0

moving = [[0, 1], [0, -1], [1, 0], [-1, 0]]


# 가로, 세로 크기 초기화
def init(board: list):
    global VERTICAL, HORIZONTAL
    VERTICAL, HORIZONTAL = len(board), len(board[0])


def dfs(board: list, my_y: int, my_x: int, your_y: int, your_x: int) -> list:
    # 움직일 공간이 없는 내가 지는 경우
    if finished(board, my_y, my_x):
        return [False, 0]
    # 움직일 수 있고 상대방과 같은 곳에 있는 이기는 경우
    if my_y == your_y and my_x == your_x:
        return [True, 1]

    min_benefit = sys.maxsize
    max_benefit = 0
    can_win = False

    # 사방향 이동
    for my, mx in moving:
        ny, nx = my_y + my, my_x + mx
        if not in_range(ny, nx) or board[ny][nx] == 0:
            continue
        board[my_y][my_x] = 0
        result = dfs(board, your_y, your_x, ny, nx)
        board[my_y][my_x] = 1
        # 현재 턴인 사람이 승리함, 상대방의 반환값이 패배여야함
        if not result[0]:
            can_win = True
            # 상대방은 최소의 손해를 얻기 위해 행동
            min_benefit = min(min_benefit, result[1])
        # 현재 턴인 사람이 패배
        else:
            # 상대 턴인 사람은 최대의 이득을 얻기 위해 행동
            max_benefit = max(max_benefit, result[1])
    turn = min_benefit if can_win else max_benefit
    return [can_win, turn + 1]

# 범위 안에 있는지 판단
def in_range(y: int, x: int) -> bool:
    if 0 <= y < VERTICAL and 0 <= x < HORIZONTAL:
        return True
    return False


# 더 이상 움직일 수 있는지 판단
def finished(board: list, y: int, x: int) -> bool:
    for my, mx in moving:
        ny, nx = my + y, mx + x
        # 움직이는 경우가 존재
        if in_range(ny, nx) and board[ny][nx] == 1:
            return False
    return True


def solution(board: list, aloc: list, bloc: list) -> int:
    init(board)
    return dfs(board, aloc[0], aloc[1], bloc[0], bloc[1])[1]
