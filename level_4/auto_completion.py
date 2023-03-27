# 자동 완성 -> Trie(트라이) 를 통한 해결
# N : len(words) M: 단어의 최대 길이
# 시간복잡도 : O(N * M)

def insert(root: dict, word: str):
    count = 1
    for ch in word:
        if ch not in root:
            root[ch] = {}
            root = root[ch]
            root['count'] = count
            root['has_words'] = 1
            count += 1
            continue
        root = root[ch]
        root['has_words'] += 1
        count += 1


def search(root: dict, word: str):
    for ch in word:
        root = root[ch]
        if root['has_words'] == 1:
            return root['count']
    return root['count']


def solution(words: list) -> int:
    answer = 0
    root = {}
    root['count'] = 0
    root['has_words'] = 0
    for word in words:
        insert(root, word)
    for word in words:
        answer += search(root, word)
    return answer