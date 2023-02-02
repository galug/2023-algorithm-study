# k 진수에서 소수 개수 구하기
# 최대 소수 : p
# 시간 복잡도 : O(n log n) 공간 복잡도 : O(n)
import math

prime = set()
# 소수 확인 함수
def is_prime(n: int) -> int:
    if n == 1:
        return 0

    if n in prime:
        return 1

    limit_sqrt = int(math.sqrt(n)) + 1
    for div in range(2, limit_sqrt):
        if n % div == 0:
            return 0
    prime.add(n)
    return 1

# 진수로 변환하는 함수
def convert(n: int, k: int) -> str:
    convert_number = ''
    while n > 0:
        div, mod = divmod(n, k)
        convert_number = str(mod) + convert_number
        n = div
    return convert_number


def solution(n: int, k: int) -> int:
    convert_number = convert(n, k)
    convert_numbers = list(map(lambda x: int(x) if x else 1, convert_number.split('0')))

    answer = 0
    for cn in convert_numbers:
        answer += is_prime(cn)
    return answer

