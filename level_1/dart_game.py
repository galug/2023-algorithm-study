# 다트 게임 -> stack 자료구조 + 구현 문제
# N 은 dartResult의 길이 (len(dartResult))
# 시간 복잡도 : O(N) 공간 복잡도 : O(N)
import re

# 문자열을 점수로 변환해주는 함수
def convert_score(score: str) -> int:
    real_score = int(score[:-1])
    if score[-1] == 'S':
        return real_score
    elif score[-1] == 'D':
        return real_score ** 2
    else:
        return real_score ** 3

def solution(dartResult: str) -> int:
    stack = []
    start = 0
    for idx in range(len(dartResult)):
        # 순수한 점수에 대한 처리를 한다.
        if dartResult[idx] in 'SDT':
            stack.append(convert_score(dartResult[start: idx + 1]))
            start = idx + 1
        # '*' 이 올 경우 제일 최근 2개의 점수에 2 를 곱해준다.
        if dartResult[idx] == '*':
            # 바로 전에 얻은 점수가 존재할 시 2를 곱해준다.
            if len(stack) >= 2:
                stack[-2] *= 2
            stack[-1] *= 2
            start = idx + 1
        # '#' 이 올 경우 제일 최근 점수에 -1 을 곱해준다.
        if dartResult[idx] == '#':
            stack[-1] *= -1
            start = idx + 1
    return sum(stack)

