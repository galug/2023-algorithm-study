# 카드 짝 맞추기
# 시간복잡도 : O(s ** )
import collections
import sys

BOARD_SIZE = 4

moving = [(0, 1), (0, -1), (1, 0), (-1, 0)]
card_positions = collections.defaultdict(list)
going_order = []


def init(board: list):
    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
            if board[i][j] != 0:
                card_positions[board[i][j]].append((i, j))


def is_in_range(r: int, c: int) -> bool:
    if 0 <= r < BOARD_SIZE and 0 <= c < BOARD_SIZE:
        return True
    return False


def bfs(s_r: int, s_c: int, d_r: int, d_c: int, board: list, visited: set) -> list:
    if s_r == d_r and s_c == d_c:
        return [d_r, d_c, 0]
    que = collections.deque([(s_r, s_c, 0)])
    visited_board = set()
    while que:
        r, c, number_of_moving = que.popleft()
        if (r, c) in visited_board:
            continue
        visited_board.add((r, c))
        for mr, mc in moving:
            for i in range(1, BOARD_SIZE + 1):
                nr, nc = r + mr * i, c + mc * i
                # board 안에 포함 안될시 넘어감
                if not is_in_range(nr, nc):
                    if i != 1:
                        if nr - mr == d_r and nc - mc == d_c:
                            return [d_r, d_c, number_of_moving + 1]
                        que.append([nr - mr, nc - mc, number_of_moving + 1])
                    break
                # 아직 페어를 못맞춘 카드를 찾은 최소 거리일때 반환
                if board[nr][nc] != 0 and board[nr][nc] not in visited:
                    if nr == d_r and nc == d_c:
                        return [d_r, d_c, number_of_moving + 1]
                    que.append([nr, nc, number_of_moving + 1])
                    break
                if i == 1:
                    if nr == d_r and nc == d_c:
                        return [d_r, d_c, number_of_moving + 1]
                    que.append([nr, nc, number_of_moving + 1])


# 카드를 고르는 과정
def select_card(visited: set, visited_positions: list):
    if len(visited_positions) == len(card_positions) * 2:
        going_order.append(visited_positions)
    for k in card_positions:
        # k 에 방문한 적이 없으면
        if k not in visited:
            select_card(visited | {k}, visited_positions + [card_positions[k][0], card_positions[k][1]])
            select_card(visited | {k}, visited_positions + [card_positions[k][1], card_positions[k][0]])


def solution(board: list, r: int, c: int) -> int:
    init(board)
    select_card(set(), [])
    total_element = len(card_positions)
    answer = sys.maxsize
    for orders in going_order:
        visited = set()
        current_r, current_c = r, c
        total_moving = total_element * 2
        for i in range(total_element):
            s_card, d_card = orders[2 * i], orders[2 * i + 1]
            # 카드 위치로 이동
            current_r, current_c, number_of_moving_to_s = bfs(current_r, current_c, s_card[0], s_card[1], board,
                                                              visited)
            # 도착 카드 위치로 이동
            current_r, current_c, number_of_moving_to_d = bfs(current_r, current_c, d_card[0], d_card[1], board,
                                                              visited)
            # 방문한 카드 목록으로 추가
            visited.add(visited.add(board[current_r][current_c]))
            total_moving += (number_of_moving_to_s + number_of_moving_to_d)
        answer = min(answer, total_moving)
    return answer


'''
# 카드 짝 맞추기
# 시간복잡도 : O(s ** )
import collections
import sys

BOARD_SIZE = 4

moving = [(0, 1), (0, -1), (1, 0), (-1, 0)]
card_positions = collections.defaultdict(list)
going_order = []


def init(board: list):
    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
            if board[i][j] != 0:
                card_positions[board[i][j]].append((i, j))


def is_in_range(r: int, c: int) -> bool:
    if 0 <= r < BOARD_SIZE and 0 <= c < BOARD_SIZE:
        return True
    return False


def bfs(s_r: int, s_c: int, d_r: int, d_c: int, board: list, visited: set) -> list:
    if s_r == d_r and s_c == d_c:
        return [d_r, d_c, 0]
    que = collections.deque([(s_r, s_c, 0)])
    visited_board = set()
    while que:
        r, c, number_of_moving = que.popleft()
        if (r, c) in visited_board:
            continue
        visited_board.add((r, c))
        for mr, mc in moving:
            for i in range(1, BOARD_SIZE + 1):
                nr, nc = r + mr * i, c + mc * i
                # board 안에 포함 안될시 넘어감
                if not is_in_range(nr, nc):
                    if i != 1:
                        if nr - mr == d_r and nc - mc == d_c:
                            return [d_r, d_c, number_of_moving + 1]
                        que.append([nr - mr, nc - mc, number_of_moving + 1])
                    break
                # 아직 페어를 못맞춘 카드를 찾은 최소 거리일때 반환
                if board[nr][nc] != 0 and board[nr][nc] not in visited:
                    if nr == d_r and nc == d_c:
                        return [d_r, d_c, number_of_moving + 1]
                    que.append([nr, nc, number_of_moving + 1])
                    break
                if i == 1:
                    if nr == d_r and nc == d_c:
                        return [d_r, d_c, number_of_moving + 1]
                    que.append([nr, nc, number_of_moving + 1])


# 카드를 고르는 과정
def select_card(visited: set, visited_positions: list):
    if len(visited_positions) == len(card_positions) * 2:
        going_order.append(visited_positions)
    for k in card_positions:
        # k 에 방문한 적이 없으면
        if k not in visited:
            select_card(visited | {k}, visited_positions + [card_positions[k][0], card_positions[k][1]])
            select_card(visited | {k}, visited_positions + [card_positions[k][1], card_positions[k][0]])


def solution(board: list, r: int, c: int) -> int:
    init(board)
    select_card(set(), [])
    total_element = len(card_positions)
    answer = sys.maxsize
    for orders in going_order:
        visited = set()
        current_r, current_c = r, c
        total_moving = total_element * 2
        for i in range(total_element):
            s_card, d_card = orders[2 * i], orders[2 * i + 1]
            # 카드 위치로 이동
            current_r, current_c, number_of_moving_to_s = bfs(current_r, current_c, s_card[0], s_card[1], board,
                                                              visited)
            # 도착 카드 위치로 이동
            current_r, current_c, number_of_moving_to_d = bfs(current_r, current_c, d_card[0], d_card[1], board,
                                                              visited)
            # 방문한 카드 목록으로 추가
            visited.add(visited.add(board[current_r][current_c]))
            total_moving += (number_of_moving_to_s + number_of_moving_to_d)
        answer = min(answer, total_moving)
    return answer
'''
