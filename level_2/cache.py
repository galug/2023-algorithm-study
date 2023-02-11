# 캐시
# N: len(cities) M: cacheSize
# 시간 복잡도: O(N * M)
import collections


def solution(cacheSize: int, cities: list) -> int:
    # 모든 DB가 miss 인 경우
    if cacheSize == 0:
        return len(cities) * 5
    answer = 0
    cache = collections.deque()
    cur_cache_size = 0
    for city in cities:
        city = city.lower()
        if city in cache:
            answer += 1
            cache.remove(city)
            cache.append(city)
            continue
        if cur_cache_size < cacheSize:
            answer += 5
            cache.append(city)
            cur_cache_size += 1
            continue
        # cache 가 꽉 찬 상황에서 city 가 cache 안에 없는 경우
        answer += 5
        cache.popleft()
        cache.append(city)
    return answer
