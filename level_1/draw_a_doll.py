# 크레인 인형 뽑기 게임 -> 스택 자료 구조를 이용한 풀이
# n : 크레인의 한 변 크기, m : move 의 크기
# 시간 복잡도 : O(nm) 공간 복잡도 : O(n ^^ 2 + m)

# 불필요한 연산을 줄이기 위한 전역 변수
length = 0


# 크레인에서 뽑은 결과를 반환하는 함수, 뽑을 수 없을 시 -1 을 반환
def draw(board: list, move: int) -> int:
    global length
    move -= 1
    for y in range(length):
        if board[y][move] != 0:
            element = board[y][move]
            board[y][move] = 0
            return element
    return -1


def solution(board: list, moves: list) -> int:
    global length
    length = len(board)
    answer = 0
    stack = []

    for move in moves:
        element = draw(board, move)
        # 뽑을 인형이 없을 시 넘어간다.
        if element == -1:
            continue
        # 바구니에 있는 인형이 터지는 경우
        if stack and stack[-1] == element:
            answer += 2
            stack.pop()
        # 바구니에 있는 인형이 터지지 않는 경우
        else:
            stack.append(element)

    return answer


