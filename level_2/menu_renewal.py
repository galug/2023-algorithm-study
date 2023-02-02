# 메뉴 리뉴얼 -> combinations 와 dictionary 
# N : orders 의 길이 (len(orders)) , M: 문자열의 길이 (len(order))
# 시간 복잡도 O(NM) 공간 복잡도 O(N 2 ** M)
import collections
import itertools

course_menus = collections.defaultdict(int)
menus = collections.defaultdict(set)


# 초기화
def init(orders: list):
    for order in orders:
        order_length = len(order)
        combination_idx = [i for i in range(order_length)]
        # 모든 2개 이상의 메뉴를 가지는 코스 개수를 센다.
        for number_of_combination in range(2, order_length + 1):
            for cb in itertools.combinations(combination_idx, number_of_combination):
                menu = ''.join(sorted([order[cn] for cn in cb]))
                menus[number_of_combination].add(menu)
                course_menus[menu] += 1

# 조건에 맞는 코스 만들기 함수
def make_course(course: list) -> list:
    answer = []
    for menu_number in course:
        temp_answer = []
        temp_max = 0
        for menu in menus[menu_number]:
            if course_menus[menu] > 1 and course_menus[menu] > temp_max:
                temp_answer.clear()
                temp_max = course_menus[menu]
                temp_answer.append(menu)
            elif course_menus[menu] == temp_max:
                temp_answer.append(menu)
        answer += temp_answer
    return sorted(answer)


def solution(orders: list, course: list) -> list:
    init(orders)
    return make_course(course)
