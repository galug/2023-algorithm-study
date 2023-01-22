# 개인정보 수집 유효 기간 문제
# 구현 문제
# 시간 복잡도 : O(n)
import re


def solution(today: str, terms: list, privacies: list) -> list:
    answer = []
    terms_valid = make_terms_dictionary(terms)
    for privacy_index, privacy in enumerate(privacies):
        valid_privacy = make_valid_privacy(privacy, terms_valid)
        if is_destroy(today, valid_privacy):
            answer.append(privacy_index + 1)
    return answer


# 약관과 유효기간을 dictionary 형태로 만든다.
def make_terms_dictionary(terms: list) -> dict:
    term_valid = {}
    for term in terms:
        tos = term.split()
        term_valid[tos[0]] = int(tos[1])
    return term_valid


# 개인 정보 수집 일자로 만료 기간을 만들어주는 함수
def make_valid_privacy(privacy: str, term_valid: dict):
    year, month, day, term = map(str, re.split('[ .]', privacy))
    year, month, day, term = int(year), int(month), int(day), term_valid[term]

    month, day = month + term, day - 1
    if day == 0:
        day = 28
        month -= 1
    if month > 12:
        if month % 12 == 0:
            year += month // 12 - 1
            month = 12
        else:
            year += month // 12
            month %= 12
    elif month <= 0:
        month = 12
        year -= 1
    return str(year) + '.{0:02d}.'.format(month) + '{0:02d}'.format(day)


# 파기 해야할 개인정보인지 판단하는 함수
def is_destroy(today: str, valid: str):
    if today > valid:
        return True
    return False
