# 블록 이동하기
# N: board 의 한쪽 변 크기
# 시간복잡도: O(N ** 2)

import collections

Y, X = 0, 1


def can_move(cur1: tuple, cur2: tuple, new_board: list) -> list:
    cand = []
    # 직선으로 이동
    moving = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    for my, mx in moving:
        ncy1, ncx1, ncy2, ncx2 = cur1[Y] + my, cur1[X] + mx, cur2[Y] + my, cur2[X] + mx
        if new_board[ncy1][ncx1] == 0 and new_board[ncy2][ncx2] == 0:
            cand.append(((ncy1, ncx1), (ncy2, ncx2)))
    # 세로에서 가로로 이동
    if cur1[X] == cur2[X]:
        for lrx in [-1, 1]:
            if new_board[cur1[Y]][cur1[X] + lrx] == 0 and new_board[cur2[Y]][cur2[X] + lrx] == 0:
                cand.append(((cur1[Y], cur1[X]), (cur1[Y], cur1[X] + lrx)))
                cand.append(((cur2[Y], cur2[X]), (cur2[Y], cur2[X] + lrx)))
    # 가로에서 세로로 이동
    if cur1[Y] == cur2[Y]:
        for udy in [-1, 1]:
            if new_board[cur1[Y] + udy][cur1[X]] == 0 and new_board[cur2[Y] + udy][cur2[X]] == 0:
                cand.append(((cur1[Y], cur1[X]), (cur1[Y] + udy, cur1[X])))
                cand.append(((cur2[Y], cur2[X]), (cur2[Y] + udy, cur2[X])))
    return cand


def solution(board: list) -> int:
    board_size = len(board)
    # 외벽에 둘러쌓인 새로운 보드 생성
    new_board = [[1] * (board_size + 2) for _ in range(board_size + 2)]
    for y in range(board_size):
        for x in range(board_size):
            new_board[y + 1][x + 1] = board[y][x]
    # 보드 위치, count 를 넣은 que
    que = collections.deque([[[1, 1], [1, 2], 0]])
    visited = {((1, 1), (1, 2))}
    while que:
        cur1, cur2, count = que.popleft()
        if cur1 == (board_size, board_size) or cur2 == (board_size, board_size):
            return count
        for new_cur1, new_cur2 in can_move(cur1, cur2, new_board):
            if (new_cur1, new_cur2) not in visited:
                visited.add((new_cur1, new_cur2))
                que.append([new_cur1, new_cur2, count + 1])