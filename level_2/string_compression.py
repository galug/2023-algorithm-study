# 문자열 압축 문제 -> 완전 탐색
# N: len(s)
# 시간 복잡도 : O(N ** 2) 공간 복잡도 : O(1)
import sys

def decimal(n: int) -> int:
    answer = 0
    while n > 0:
        n //= 10
        answer += 1
    return answer

# 최소 값만을 구하는 풀이
def solution(s: str) -> int:
    # 문자열이 한 개인 경우 고려
    if len(s) == 1:
        return 1

    answer = sys.maxsize
    length = len(s)
    # compression_length 최대 length // 2 까지 이다.
    for compression_length in range(1, length // 2 + 1):
        start, end = 0, compression_length
        temp_answer = 0
        # prev 와 s[시작:끝] 이 같은지 계속해서 확인
        while start < length:
            # 자르고 남는 문자열을 처리한다.
            if end > length:
                temp_answer += len(s[end - compression_length:])
                break
            prev = s[start:end]
            # 압축할 수 범위를 구한다.
            while end < length and prev == s[end:end + compression_length]:
                end += compression_length
            # 문자열 압축 과정
            if (end - start) // compression_length != 1:
                temp_answer += decimal((end - start) // compression_length)
            temp_answer += compression_length
            start, end = end, end + compression_length
        answer = min(answer, temp_answer)
    return answer

'''
최소값일시 문자열을 구하는 풀이 
def solution(s: str) -> int:
    if len(s) == 1:
        return 1
    answer = 'a' * 1001
    length = len(s)
    # compression_length 최대 length // 2 까지 이다.
    for compression_length in range(1, length // 2 + 1):
        start, end = 0, compression_length
        temp_answer = ''
        # prev 와 s[시작:끝] 이 같은지 계속해서 확인
        while start < length:
            # 자르고 남는 문자열을 처리한다.
            if end > length:
                temp_answer += s[end - compression_length:]
                break
            prev = s[start:end]
            # 압축할 수 범위를 구한다.
            while end < length and prev == s[end:end + compression_length]:
                end += compression_length
            # 문자열 압축 과정
            if (end - start) // compression_length != 1:
                temp_answer += str((end - start) // compression_length)
            temp_answer += prev
            start, end = end, end + compression_length

        if len(temp_answer) < len(answer):
            answer = temp_answer
    return len(answer)
'''