# 경주로 건설
# N : board_size
# 시간복잡도 : O(N ** 2)

import collections
import sys


def solution(board: list) -> int:
    board_size = len(board)

    moving = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    que = collections.deque()
    visited = [[[sys.maxsize] * board_size for _ in range(board_size)] for _ in range(2)]

    visited[0][0][0] = 0
    visited[1][0][0] = 0

    if board[1][0] == 0:
        visited[0][1][0] = 100
        que.append([1, 0, 0, 100])
    if board[0][1] == 0:
        visited[1][0][1] = 100
        que.append([0, 1, 1, 100])

    while que:
        y, x, d, cost = que.popleft()
        # 4 방향 탐색
        for md, move in enumerate(moving):
            my, mx = move[0], move[1]
            ny, nx = y + my, x + mx
            # 범위를 벗어나거나 벽일 경우
            if ny < 0 or ny >= board_size or nx < 0 or nx >= board_size or board[ny][nx] == 1:
                continue
            # 직선도로로 나아가는 경우
            if d % 2 == md % 2:
                # 세로로 직선 도로를 세우는 경우
                if md % 2 == 0 and visited[0][ny][nx] > cost + 100:
                    visited[0][ny][nx] = cost + 100
                    que.append([ny, nx, md, cost + 100])
                # 가로로 직선 도로를 세우는 경우
                if md % 2 == 1 and visited[1][ny][nx] > cost + 100:
                    visited[1][ny][nx] = cost + 100
                    que.append([ny, nx, md, cost + 100])
            # 코너를 만드는 경우
            if d % 2 != md % 2:
                # 세로로 코너로 꺾는 경우
                if md % 2 == 0 and visited[0][ny][nx] > cost + 600:
                    visited[0][ny][nx] = cost + 600
                    que.append([ny, nx, md, cost + 600])
                if md % 2 == 1 and visited[1][ny][nx] > cost + 600:
                    visited[1][ny][nx] = cost + 600
                    que.append([ny, nx, md, cost + 600])
    return min(visited[0][-1][-1], visited[1][-1][-1])