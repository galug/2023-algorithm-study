# 가사 검색 -> Trie 이용해서 해결

import collections


def insert_start(word: str, root: dict):
    new_root = root
    len_word = len(word)
    root['num'][len_word] += 1
    for ch in word:
        if ch not in new_root:
            new_root[ch] = {}
        new_root = new_root[ch]
        if 'num' not in new_root:
            new_root['num'] = collections.defaultdict(int)
        new_root['num'][len_word] += 1


def insert_end(word: str, root: dict):
    new_root = root
    len_word = len(word)
    word = reversed(word)
    for ch in word:
        if ch not in new_root:
            new_root[ch] = {}
        new_root = new_root[ch]
        if 'num' not in new_root:
            new_root['num'] = collections.defaultdict(int)
        new_root['num'][len_word] += 1


def convert(query: str):
    new_word = ''
    if query[0] == '?':
        query = reversed(query)
    for q in query:
        if q != '?':
            new_word += q
    return new_word


def search(query: str, query_len: int, root: dict) -> int:
    for q in query:
        if q in root:
            root = root[q]
            continue
        return 0
    return root['num'][query_len]


def solution(words, queries):
    answer = []
    start_root = {'num': collections.defaultdict(int)}
    end_root = {}
    for word in words:
        insert_start(word, start_root)
        insert_end(word, end_root)

    for query in queries:
        len_query = len(query)
        if query[0] == '?' and query[-1] == '?':
            if len_query in start_root['num']:
                answer.append(start_root['num'][len_query])
                continue
            answer.append(0)
            continue
        # 끝부분에 진짜 찾는 단어 있는 경우
        if query[0] == '?':
            query = convert(query)
            answer.append(search(query, len_query, end_root))
        # 첫 부분에 진짜 찾는 단어 있는 경우
        else:
            query = convert(query)
            answer.append(search(query, len_query, start_root))
    return answer