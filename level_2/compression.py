# 압축
# n : len(msg)
# 시간 복잡도 : O(N)
dic = {}

# 사전 초기화
def init():
    first_order = ord('A')
    for i in range(26):
        dic[chr(first_order + i)] = i + 1


def solution(msg: str) -> list:
    init()
    idx = 0
    answer = []
    dic_size = 27
    while idx < len(msg):
        end = idx + 1
        # 사전에 없는 단어 찾기
        while end < len(msg) + 1 and msg[idx: end] in dic:
            end += 1
        # 사전에 없는 단어일시 사전에 추가
        if msg[idx: end] not in dic:
            dic[msg[idx: end]] = dic_size
        end -= 1

        answer.append(dic[msg[idx: end]])
        idx = end
        dic_size += 1
    return answer
