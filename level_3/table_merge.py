# 표 병합 -> 완전 탐색
# K : 상수(2500), N: len(commands)
# 시간 복잡도 : O(K * N )
import collections

MAX_LENGTH = 51

table = [[None] * MAX_LENGTH for _ in range(MAX_LENGTH)]
groups = []


def update(command: list):
    if len(command) == 3:
        for i in range(1, MAX_LENGTH):
            for j in range(1, MAX_LENGTH):
                if table[i][j] == command[1]:
                    table[i][j] = command[2]
    if len(command) == 4:
        r, c = map(int, [command[1], command[2]])
        is_in_group = False
        for group in groups:
            if (r, c) in group:
                is_in_group = True
                for gr, gc in group:
                    table[gr][gc] = command[3]
        if not is_in_group:
            table[r][c] = command[3]


def merge(command: list):
    r1, c1, r2, c2 = map(int, [command[1], command[2], command[3], command[4]])
    if r1 == r2 and c1 == c2:
        return
    include_group_idx = []
    for group_idx, group in enumerate(groups):
        if (r1, c1) in group or (r2, c2) in group:
            include_group_idx.append(group_idx)
    if len(include_group_idx) == 2:
        g1 = groups.pop(include_group_idx.pop())
        g2 = groups.pop(include_group_idx.pop())
        merge_group = g1 | g2
    elif len(include_group_idx) == 1:
        if (r1, c1) in groups[include_group_idx[0]]:
            group = groups.pop(include_group_idx.pop())
            merge_group = group | {(r2, c2)}
        else:
            group = groups.pop(include_group_idx.pop())
            merge_group = group | {(r1, c1)}
    else:
        merge_group = {(r1, c1), (r2, c2)}
    groups.append(merge_group)
    value = table[r1][c1] if table[r1][c1] is not None else table[r2][c2]
    for r, c in merge_group:
        table[r][c] = value


def unmerge(command: list):
    r, c = map(int, [command[1], command[2]])
    for group_idx, group in enumerate(groups):
        if (r, c) in group:
            unmerge_group = groups.pop(group_idx)
            for r_, c_ in unmerge_group:
                if r_ == r and c_ == c:
                    continue
                table[r_][c_] = None
            break


def solution(commands: list) -> list:
    answer = []
    for command in commands:
        split_command = command.split()
        if split_command[0] == 'UPDATE':
            update(split_command)
        if split_command[0] == 'MERGE':
            merge(split_command)
        if split_command[0] == 'UNMERGE':
            unmerge(split_command)
        if split_command[0] == 'PRINT':
            r, c = map(int, [split_command[1], split_command[2]])
            answer.append(table[r][c] if table[r][c] is not None else 'EMPTY')
    return answer
