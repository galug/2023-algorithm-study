# 괄호 변환
# N : 문자열의 길이(len(p))
# 시간 복잡도 : O(N) 공간 복잡도 : O(N)

# 올바른 괄호인지 확인하는 함수
def is_right_bracket(p: str) -> bool:
    stack = 0
    for ch in p:
        if stack == 0 and ch == ')':
            return False
        if stack > 0 and ch == ')':
            stack -= 1
            continue
        stack += 1
    return True

def solution(p: str) -> str:
    # 빈 문자열인지 확인
    if not p:
        return p
    # 균형잡힌 문자열인지 확인
    if is_right_bracket(p):
        return p
    # 균형잡힌 두 문자열 u,v 로 나눠주는 과정
    brackets = {'(': 0, ')': 0}
    split_idx = 0
    for b_idx, bracket in enumerate(p):
        brackets[bracket] += 1
        if brackets['('] == brackets[')']:
            split_idx = b_idx + 1
            break
    # u 가 올바른 괄호 문자열인 경우와 아닌 경우
    if is_right_bracket(p[:split_idx]):
        return p[:split_idx] + solution(p[split_idx:])
    else:
        answer = '(' + solution(p[split_idx:]) + ')'
        other_brackets = {'(': ')', ')': '('}
        for b in p[:split_idx][1:-1]:
            answer += other_brackets[b]
        return answer
