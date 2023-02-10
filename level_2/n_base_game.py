# n진수 게임
# N : 튜브의 마지막 회차에 나오는 가장 큰 수의 10진수
# 시간복잡도 : O(N log N)

# n 을 base 진수로 바꾸는 함수
def make_n_base_number(n: int, base: int) -> str:
    if n == 0:
        return '0'
    n_base_number = ''
    while n > 0:
        n, mod = divmod(n, base)
        if mod >= 10:
            n_base_number = chr(mod - 10 + ord('A')) + n_base_number
            continue
        n_base_number = str(mod) + n_base_number
    return n_base_number


# 튜브가 마지막으로 말할 때까지의 게임 결과를 반환
def make_max_n_base_lines(n: int, t: int, m: int) -> str:
    max_n_base_lines = ''
    number = 0
    while len(max_n_base_lines) < t * m:
        max_n_base_lines += make_n_base_number(number, n)
        number += 1
    return max_n_base_lines


# 진법 n, 미리 구할 숫자의 갯수 t, 게임에 참가하는 인원 m, 튜브의 순서 p
def solution(n: int, t: int, m: int, p: int) -> str:
    answer = ''
    p -= 1
    max_n_base = make_max_n_base_lines(n, t, m)
    for multiply in range(t):
        answer += max_n_base[p + multiply * m]
    return answer


