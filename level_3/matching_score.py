# 매칭점수 -> 정규 표현식
# N: 가장 긴 page 길이, M : len(pages)
# 시간복잡도 : O(N M)

import re
import sys
import collections

out_pages = collections.defaultdict(list)


def analyze_page(page: str, word: str) -> list:
    page_infos = {}
    page = page.lower()
    # 페이지 링크 찾기
    page_link = re.search('<meta property="og:url" content="https://(\S+)"', page).group(1)
    # 외부 링크 찾기
    out_links = re.findall('<a href="https://(\S+)">', page)
    out_link_pages = 0
    for out_link in out_links:
        out_link_pages += 1
        out_pages[out_link].append(page_link)

    # 기본 점수 찾기
    base_score = 0
    page = re.sub('[^a-z]', ' ', page).split()
    for w in page:
        if word == w:
            base_score += 1
    return page_link, base_score, out_link_pages


def solution(word: str, pages: list) -> int:
    answer = [sys.maxsize, 0]
    word = word.lower()
    page_infos = {}
    for index, page in enumerate(pages):
        page_link, base_score, out_links = analyze_page(page, word)
        page_infos[page_link] = [index, base_score, out_links]

    for page_link in page_infos:
        index, base_score, out_links = page_infos[page_link]
        total_score = base_score

        for out_page in out_pages[page_link]:
            if out_page in page_infos:
                total_score += (page_infos[out_page][1] / page_infos[out_page][2])
        if total_score > answer[1]:
            answer = [index, total_score]
            continue
        if total_score == answer[1] and index < answer[0]:
            answer = [index, total_score]
    # 점수 계산
    return answer[0]