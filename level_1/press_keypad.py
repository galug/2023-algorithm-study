# 키패드 누르기 문제
# n: numbers 의 길이
# 시간복잡도 : O(n), 공간 복잡도 : O()

# destination 과의 거리를 비교해주는 함수
def compare_distance(left_hand: int, right_hand: int, destination: int, hand: str) -> int:
    ly, lx = keypad[left_hand]
    ry, rx = keypad[right_hand]
    dy, dx = keypad[destination]
    if abs(dy - ly) + abs(dx - lx) < abs(dy - ry) + abs(dx - rx):
        return -1
    elif abs(dy - ly) + abs(dx - lx) > abs(dy - ry) + abs(dx - rx):
        return 1
    if hand == 'left':
        return -1
    return 1


# 키페드의 위치를 저장하는 dictionary
keypad = {10: (3, 0), 0: (3, 1), 11: (3, 2)}
_key = 1
for y in range(3):
    for x in range(3):
        keypad[_key] = (y, x)
        _key += 1


def solution(numbers: list, hand: str) -> str:
    answer = ''
    left, right = 10, 11
    for number in numbers:
        # 1,4,7 의 경우 왼손으로 친다.
        if number in (1, 4, 7):
            left = number
            answer += 'L'
            continue
        # 3,6,9 의 경우 오른손으로 친다.
        if number in (3, 6, 9):
            right = number
            answer += 'R'
            continue
        # 왼손과 오른손 중 더 가까운 곳 혹은 주손에 따른 타자를 칠 손을 결정
        if compare_distance(left, right, number, hand) < 0:
            left = number
            answer += 'L'
        else:
            right = number
            answer += 'R'

    return answer
