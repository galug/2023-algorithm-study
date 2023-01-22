# 성격 유형 검사하기
# 구현 문제
# 시간 복잡도 O(n)

def solution(survey, choices):
    answer = ''
    characters = {'R': 0, 'T': 0, 'C': 0, 'F': 0, 'J': 0, 'M': 0, 'A': 0, 'N': 0}
    indicators = ['RT', 'CF', 'JM', 'AN']
    # 성격 유형 점수를 매기는 반복문
    for index in range(len(survey)):
        survey_characters, choice = survey[index], choices[index]
        selected_character = survey_characters[select_character(choice)]
        characters[selected_character] += abs(choice - 4)
    # 성격 유형을 판단하는 반복문
    for indicator in indicators:
        if characters[indicator[0]] >= characters[indicator[1]]:
            answer += indicator[0]
            continue
        answer += indicator[1]
    return answer


# 성격 유형을 고르는 함수
def select_character(choice: int) -> int:
    if choice >= 4:
        return 1
    return 0
