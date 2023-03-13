# 기둥과 보 설치
# 시간복잡도: O(N ** 2)

PILLAR, BEAM = 0, 1
INSTALL, UNINSTALL = 1, 0


def is_impossible(build_map: set) -> bool:
    for x, y, kind in build_map:
        if kind == PILLAR:
            if y != 0 and (x, y - 1, PILLAR) not in build_map and (x - 1, y, BEAM) not in build_map and (
            x, y, BEAM) not in build_map:
                return True
        if kind == BEAM:
            if (x, y - 1, PILLAR) not in build_map and (x + 1, y - 1, PILLAR) not in build_map and not (
                    (x - 1, y, BEAM) in build_map and (x + 1, y, BEAM) in build_map):
                return True
    return False


def solution(n: int, build_frame: list) -> list:
    answer = set()
    for x, y, kind, it_ut in build_frame:
        block = (x, y, kind)
        if it_ut == INSTALL:
            answer.add(block)
            if is_impossible(answer):
                answer.remove(block)
        if it_ut == UNINSTALL and block in answer:
            answer.remove(block)
            if is_impossible(answer):
                answer.add(block)
    answer = list(answer)
    return sorted(answer, key=lambda x: (x[0], x[1], x[2]))


'''실패 코드

# 기둥 삭제 
def delete_pillar(build_map: list, x: int, y: int) -> bool:
    # 기둥이 위에 존재할 시 삭제 불가 
    if build_map[PILLAR][DOWN][y + 1][x] == 1:
        return False
    # 보의 왼쪽 부분이 걸쳐 있을 시 
    if build_map[BEAM][LEFT][y + 1][x] == 1 and not can_build_beam(build_map, x, y + 1):
        return False
    # 보의 오른쪽 부분이 걸쳐 있을 시 
    if build_map[BEAM][RIGHT][y + 1][x] == 1 and not can_build_beam(build_map, x - 1, y + 1):
        return False
    return True


# 보 삭제 
def delete_beam(build_map: list, x: int, y: int):
    if build_map[PILLAR][UP][y][x] == 1 and build_map[PILLAR][UP][y][x + 1] == 1:
        return True
    # 왼쪽에 보가 걸쳐 있을 때 
    if build_map[BEAM][RIGHT][y][x] == 1 and not can_build_beam(build_map, x - 1, y):
        return False
    # 오른쪽에 보가 걸쳐 있을 때 
    if build_map[BEAM][LEFT][y][x + 1] == 1 and not can_build_beam(build_map, x + 1, y):
        return False
    # 왼쪽에 기둥이 걸칠때
    if build_map[PILLAR][DOWN][y][x] == 1 and not can_build_pillar(build_map, x, y):
        return False
    # 오른쪽에 기둥이 걸칠때 
    if build_map[PILLAR][DOWN][y][x + 1] == 1 and not can_build_pillar(build_map, x + 1, y):
        return False
    return True


# 기둥 생성 가능
def can_build_pillar(build_map: list, x: int, y: int) -> bool:
    if y == 0:
        return True
    if build_map[BEAM][LEFT][y][x] == 1 or build_map[BEAM][RIGHT][y][x] == 1 or build_map[PILLAR][UP][y][x] == 1:
        return True
    return False


# 보 생성 가능 
def can_build_beam(build_map: list, x: int, y: int) -> bool:
    # 한 쪽 끝 부분이 기둥 위
    if build_map[PILLAR][UP][y][x] == 1 or build_map[PILLAR][UP][y][x + 1] == 1:
        return True
    # 양쪽 끝 부분이 다른 보와 동시 연결 
    if build_map[BEAM][RIGHT][y][x] == 1 and build_map[BEAM][LEFT][y][x + 1] == 1:
        return True
    return False


def solution(n: int, build_frame: list) -> list:
    answer = []
    build_map = [[[[0] * (n + 1) for _ in range(n + 1)] for _ in range(2)] for _ in range(2)]

    for x, y, kind, it_ut in build_frame:
        # 삭제 시
        if it_ut == UNINSTALL:
            # 기둥 삭제 
            if kind == PILLAR:
                build_map[PILLAR][DOWN][y][x] = 0
                build_map[PILLAR][UP][y + 1][x] = 0
                if delete_pillar(build_map, x, y):
                    continue
                build_map[PILLAR][DOWN][y][x] = 1
                build_map[PILLAR][UP][y + 1][x] = 1
                continue
            # 보 삭제 
            if kind == BEAM:
                build_map[BEAM][LEFT][y][x] = 0
                build_map[BEAM][RIGHT][y][x + 1] = 0
                if delete_beam(build_map, x, y):
                    continue
                build_map[BEAM][LEFT][y][x] = 1
                build_map[BEAM][RIGHT][y][x + 1] = 1
                continue
        # 설치시 
        if it_ut == INSTALL:
            if kind == PILLAR and can_build_pillar(build_map, x, y):
                build_map[PILLAR][DOWN][y][x] = 1
                build_map[PILLAR][UP][y + 1][x] = 1
                continue
            if kind == BEAM and can_build_beam(build_map, x, y):
                build_map[BEAM][LEFT][y][x] = 1
                build_map[BEAM][RIGHT][y][x + 1] = 1

    for x in range(n + 1):
        for y in range(n + 1):
            if build_map[PILLAR][DOWN][y][x] == 1:
                answer.append([x, y, PILLAR])
            if build_map[BEAM][LEFT][y][x] == 1:
                answer.append([x, y, BEAM])
    answer.sort()
    return answer
'''