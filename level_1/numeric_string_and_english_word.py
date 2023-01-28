# 숫자 문자열과 영단어 문제
# n : 문자열의 길이
# 시간 복잡도: O(n), 공간 복잡도: O(n)

# 문자열에 따른 숫자를 저장
matching_number = {'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4',
                   'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}

# 영단어와 숫자 문자열이 섞인 문자열을 숫자로 바꿔주는 함수
def solution(s: str) -> int:
    for english, value in matching_number.items():
        s = s.replace(english, value)
    return int(s)
