# 블록 게임
import collections

BOARD_SIZE = 0


def is_regtangle(y: int, x: int) -> bool:
    pass


def is_in_range(y: int, x: int) -> bool:
    if x < 0 or x >= BOARD_SIZE or y < 0 or y >= BOARD_SIZE:
        return False
    return True


def find_block(y: int, x: int, board: list, blocks_set: set) -> list:
    kind = board[y][x]
    blocks = [[y, x]]
    blocks_set.add((y, x))
    que = collections.deque([[y, x]])
    while que:
        y, x = que.popleft()
        for my, mx in [[-1, 0], [1, 0], [0, 1], [0, -1]]:
            ny, nx = y + my, x + mx
            if (ny, nx) in blocks_set:
                continue
            if not is_in_range(ny, nx):
                continue
            if board[ny][nx] != kind:
                continue
            blocks.append([ny, nx])
            que.append([ny, nx])
            blocks_set.add((ny, nx))
    return blocks


def solution(board: list) -> int:
    global BOARD_SIZE
    answer = 0
    BOARD_SIZE = len(board)
    blocks_set = set()
    blocks = []
    # 최상단 블록 찾기
    for x in range(BOARD_SIZE):
        for y in range(BOARD_SIZE):
            if board[y][x] != 0:
                if (y, x) not in blocks_set:
                    blocks.append(find_block(y, x, board, blocks_set))
                break
    print(blocks)
    # while True:
    #     is_boom = False

    return answer