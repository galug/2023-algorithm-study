# 호텔 방 배정 -> union-find

import sys

sys.setrecursionlimit(100000)


# union - find 이용 찾기
def find(cur_pos: int, parent: list):
    # 방에 손님이 없는 경우
    if cur_pos not in parent:
        parent[cur_pos] = cur_pos + 1
        return cur_pos
    parent[cur_pos] = find(parent[cur_pos], parent)
    return parent[cur_pos]


def solution(k: int, room_number: list) -> list:
    answer = []
    parent = dict()
    for rn in room_number:
        answer.append(find(rn, parent))
    return answer


'''
import sys

sys.setrecursionlimit(100000)


# union - find 이용 찾기  
def find(cur_pos: int, parent: list):
    if cur_pos == parent[cur_pos]:
        return cur_pos
    new_pos = find(parent[cur_pos], parent)
    parent[cur_pos] = new_pos 
    return new_pos

def solution(k: int, room_number: list) -> list:
    answer = []
    parent = [i for i in range(k + 1)]
    visited = set()
    for rn in room_number:
        # 원하는 방이 배정되어 있다면 
        if rn in visited:
            rn = find(rn, parent)
        visited.add(rn)
        answer.append(rn)
        parent[rn] += 1
    return answer
'''