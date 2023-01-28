# 신규 아이디 추천 문제
# n : 문자열의 길이(length(new_id))
# 시간복잡도 : O(n), 공간 복잡도: O(n)
import re


def step_four(new_id: str) -> str:
    start, end = 0, len(new_id)
    # 문자열이 . 만 남았을 시 빈 문자열을 반환
    if new_id == '.':
        return ''
    # 문자열 맨 앞의 .을 제거
    if new_id[0] == '.':
        start += 1
    # 문자열 맨 끝의 .을 제거
    if new_id[-1] == '.':
        end -= 1
    return new_id[start: end]


def step_five(new_id: str) -> str:
    # new_id 가 빈 문자열일 경우 a 반환
    if new_id == '':
        return 'a'
    return new_id


def step_six(new_id: str) -> str:
    # 문자열의 길이가 15개 이하일 경우 통과
    if len(new_id) <= 15:
        return new_id
    # 문자열의 길이가 16개 이상이고 15번째가 . 일 경우 제거
    if new_id[14] == '.':
        return new_id[:14]
    # 문자열의 길이가 16개 이상이고 15번쩨가 . 이 아닐 경우 15개의 문자열을 반환
    return new_id[:15]


def step_seven(new_id: str) -> str:
    # 문자열의 길이가 3개 이상일 경우 그대로 반환
    if len(new_id) > 2:
        return new_id
    # 문자열의 길이가 2개 이하일 경우 맨 끝의 문자열을 길이가
    return new_id + new_id[-1] * (3 - len(new_id))

def solution(new_id: str) -> str:
    # 모든 문자를 소문자로 변환
    new_id = new_id.lower()
    # 조건에 맞는 문자가 아닌 문자는 모두 제거
    new_id = re.sub('[^a-z0-9-_.]', '', new_id)
    # .이 2개 이상 연속될 경우 . 한개로 변환
    new_id = re.sub('[.]{2,}', '.', new_id)
    # 문자열 맨 앞이나 끝에 . 이 있을 경우 제거
    new_id = step_four(new_id)
    # 빈 문자열일 경우 a 반환
    new_id = step_five(new_id)
    # 문자열 길이가 16개 이상일 경우 15개로 줄이기 단 . 은 항상 맨 뒤에 있어서는 안됨
    new_id = step_six(new_id)
    # 문자열 길이가 2개 이하일 경우 맨끝의 문자를 반복해서 길이를 3으로 만들기
    new_id = step_seven(new_id)
    return new_id


