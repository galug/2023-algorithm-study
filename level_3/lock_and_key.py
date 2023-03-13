KEY_SIZE, LOCK_SIZE = 0, 0


def init(key_size: int, lock_size: int, lock: list) -> list:
    global KEY_SIZE, LOCK_SIZE
    KEY_SIZE, LOCK_SIZE = key_size, lock_size
    new_line = [0] * ((key_size - 1) * 2 + lock_size)
    new_lock = [new_line for _ in range(key_size - 1)]
    for l in lock:
        new_lock.append(([0] * (key_size - 1) + l + [0] * (key_size - 1)))
    for _ in range(key_size - 1):
        new_lock.append(new_line)
    return new_lock, len(new_line)


def rotate_key(key: list) -> list:
    key_size = len(key)
    new_key = [[0] * key_size for _ in range(key_size)]

    for y in range(key_size):
        for x in range(key_size):
            new_key[x][key_size - 1 - y] = key[y][x]
    return new_key


def make_key(key: list, sy: int, sx: int, lock_size: int) -> list:
    new_key = [[0] * lock_size for _ in range(lock_size)]

    for y in range(KEY_SIZE):
        for x in range(KEY_SIZE):
            new_key[y + sy][x + sx] = key[y][x]
    return new_key


def match(new_lock: list, key: list) -> bool:
    copy_lock = [line.copy() for line in new_lock]
    lock_size = len(new_lock)
    key_size = len(key)
    for ly in range(lock_size - KEY_SIZE + 1):
        for lx in range(lock_size - KEY_SIZE + 1):
            is_matching = True
            big_key = make_key(key, ly, lx, lock_size)
            for i in range(KEY_SIZE - 1, KEY_SIZE + LOCK_SIZE - 1):
                for j in range(KEY_SIZE - 1, KEY_SIZE + LOCK_SIZE - 1):
                    if (copy_lock[i][j] == 1 and big_key[i][j] == 1) or (copy_lock[i][j] == 0 and big_key[i][j] == 0):
                        is_matching = False
                        break
                if is_matching == False:
                    break
            if is_matching:
                return True
    return False


def solution(key: list, lock: list) -> bool:
    answer = True
    key_size = len(key)
    lock_size = len(lock)
    new_lock, new_lock_size = init(key_size, lock_size, lock)
    for i in range(4):
        if i != 0:
            new_key = rotate_key(key)
            key = new_key
        if match(new_lock, key):
            return True
    return False