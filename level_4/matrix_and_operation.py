# 행렬과 연산 -> que
# 시간복잡도: O(N)

import collections


def solution(rc: list, operations: list):
    VERTICAL, HORIZONTAL = len(rc), len(rc[0])

    def rotate(n: int):
        n = n % (VERTICAL * 2 + (HORIZONTAL - 2) * 2)
        if n == 0:
            return
        for _ in range(n):
            rows[VERTICAL - 1].append(cols[1].pop())
            cols[0].append(rows[VERTICAL - 1].popleft())
            rows[0].appendleft(cols[0].popleft())
            cols[1].appendleft(rows[0].pop())

    def shiftrow(n: int):
        n = n % VERTICAL
        if n == 0:
            return
        for _ in range(n):
            rows.appendleft(rows.pop())
            cols[0].appendleft(cols[0].pop())
            cols[1].appendleft(cols[1].pop())

    # rows 와 col 로 분리
    rows = collections.deque(collections.deque(r[1:-1]) for r in rc)
    cols = [collections.deque(rc[i][0] for i in range(VERTICAL))
        , collections.deque(rc[i][HORIZONTAL - 1] for i in range(VERTICAL))]

    # operations 수행 과정
    op_idx = 0
    while op_idx < len(operations):
        op = operations[op_idx]
        start_op_idx = op_idx
        while op_idx < len(operations) and op == operations[op_idx]:
            op_idx += 1
        if op == "Rotate":
            rotate(op_idx - start_op_idx)
        if op == "ShiftRow":
            shiftrow(op_idx - start_op_idx)

    # 재조립 과정
    for i in range(VERTICAL):
        for j in range(1, HORIZONTAL - 1):
            rc[i][j] = rows[i][j - 1]
    for j in range(VERTICAL):
        rc[j][0] = cols[0][j]
        rc[j][HORIZONTAL - 1] = cols[1][j]
    return rc


'''
def solution(rc: list, operations: list):
    def rotate(n: int, rc: list):
        n = n % (VERTICAL * 2 + (HORIZONTAL - 2) * 2)
        if n == 0:
            return
        que = collections.deque(rc[0])
        for i in range(1, VERTICAL):
            que.append(rc[i][HORIZONTAL - 1])
        for i in range(HORIZONTAL - 2, -1, -1):
            que.append(rc[VERTICAL -1][i])
        for i in range(VERTICAL - 2, 0, -1):
            que.append(rc[i][0])
        # 돌리는 과정 
        for _ in range(n):
            pop = que.pop()
            que.appendleft(pop)
        # 다시 rc 에 집어넣는 과정 
        for i in range(HORIZONTAL):
            rc[0][i] = que.popleft()
        for i in range(1, VERTICAL):
            rc[i][HORIZONTAL - 1] = que.popleft()
        for i in range(HORIZONTAL - 2, -1, -1):
            rc[VERTICAL -1][i] = que.popleft()
        for i in range(VERTICAL - 2, 0, -1):
            rc[i][0] = que.popleft()


    def shiftrow(n: int, rc: list):
        n = n % VERTICAL
        if n == 0:
            return rc
        que = collections.deque(rc)
        # 돌리는 과정 
        for _ in range(n):
            pop = que.pop()
            que.appendleft(pop)
        return list(que)

    VERTICAL, HORIZONTAL = len(rc), len(rc[0])
    # 
    op_idx = 0
    while op_idx < len(operations):
        op = operations[op_idx]
        start_op_idx = op_idx
        while op_idx < len(operations) and op == operations[op_idx]:
            op_idx += 1
        if op == "Rotate":
            rotate(op_idx - start_op_idx, rc)
        if op == "ShiftRow":
            rc = shiftrow(op_idx - start_op_idx, rc)
    return rc 
'''