# 튜플
# 세트의 개수 : N
# 시간복잡도 : O(N log N)  공간 복잡도 : O(N) 

# 초기화
def init(s: str) -> list:
    s = s.replace(',', ' ')[1: -1]
    start = 1
    tuples = []
    # 문자열을 set 의 리스트로 바꾼다.
    for end, ch in enumerate(s):
        if ch == '}':
            tuples.append(set(map(int, s[start:end].split())))
            start = end + 3
    # 길이 순으로 정렬
    tuples.sort(key=lambda x: len(x))
    return tuples

def solution(s: str) -> list:
    answer = []
    tuples = init(s)
    # 차집합을 이용 겹치는 문자열을 제거
    answer.append((tuples[0] - set()).pop())
    for idx in range(1, len(tuples)):
        answer.append((tuples[idx] - tuples[idx - 1]).pop())
    return answer


