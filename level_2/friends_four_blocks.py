# 프렌즈 4블록
# 시간복잡도: O(n * m(

board_stack = []
boom_range = [[0, 1], [1, 0], [1, 1]]

# board 를 리스트 형식으로 재구성
def init(m: int, n: int, board: list):
    global board_stack
    board_stack = [[] for _ in range(n)]
    for i in range(m - 1, -1, -1):
        for j in range(n):
            board_stack[j].append(board[i][j])

# 블록 기준 위쪽으로 터뜨릴 수 있는지 판단
def can_boom(x: int, y: int, n: int):
    block = board_stack[x][y]
    for mx, my in boom_range:
        nx, ny = x + mx, y + my
        if nx < 0 or nx >= n or ny < 0 or ny >= len(board_stack[nx]):
            return False
        if board_stack[nx][ny] != block:
            return False
    return True


def solution(m: int, n: int, board: list) -> int:
    answer = 0
    init(m, n, board)
    while True:
        is_not_change = True
        boom = set()
        # 터뜨릴 수 있는 블록을 찾는다.
        for horizontal in range(n):
            for vertical in range(len(board_stack[horizontal])):
                if can_boom(horizontal, vertical, n):
                    is_not_change = False
                    boom.add((horizontal, vertical))
                    for mx, my in boom_range:
                        boom.add((horizontal + mx, vertical + my))
        # 블록이 한 번도 안터지는 경우
        if is_not_change:
            break
        # 터뜨리는 과정
        boom = list(boom)
        # y 위치가 바뀌는 것을 고려하지 않기 위해 y 가 큰 순으로 정렬
        boom.sort(key=lambda x: x[1], reverse=True)
        for bx, by in boom:
            board_stack[bx].pop(by)
        answer += len(boom)
    return answer

