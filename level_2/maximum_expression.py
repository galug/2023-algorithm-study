# 수식 최대화
# N : len(expression)
# 시간 복잡도 : O(N) 공간 복잡도 : O(N)
import itertools
# op 들의 모음
operations = []

# 초기화
def init(expression: str):
    for op in '*+-':
        if op in expression:
            operations.append(op)

# 연산을 해주는 함수
def operation(operator1: int, operator2: int, op: str) -> int:
    if op == '*':
        return operator1 * operator2
    if op == '+':
        return operator1 + operator2
    if op == '-':
        return operator1 - operator2

#
def calculate_expression(expression: str, op_priority: dict):
    start = 0
    expression_list = []
    # op 와 operator 를 기준으로 list 로 쪼개 준다.
    for end, ex in enumerate(expression):
        if end == len(expression) - 1:
            expression_list.append(int(expression[start:end + 1]))
        if ex in '*+-':
            expression_list.append(int(expression[start:end]))
            expression_list.append(ex)
            start = end + 1
    # 우선 순위에 우위가 있는 op 부터 계산해준다.
    for op in op_priority:
        new_expression = []
        ex_idx = 0
        while ex_idx < len(expression_list):
            if type(expression_list[ex_idx]) == str and expression_list[ex_idx] == op:
                operator1 = new_expression.pop()
                operator2 = expression_list[ex_idx + 1]
                new_expression.append(operation(operator1, operator2, op))
                ex_idx += 2
                continue
            new_expression.append(expression_list[ex_idx])
            ex_idx += 1
        expression_list = new_expression
    return abs(expression_list[0])


def solution(expression: str) -> int:
    answer = 0
    init(expression)
    # op의 우선순위를 정해서 전해준다.
    for p in itertools.permutations(operations, len(operations)):
        answer = max(answer, calculate_expression(expression, p))
    return answer


