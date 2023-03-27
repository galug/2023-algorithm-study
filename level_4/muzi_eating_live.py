# 무지의 먹방 라이브 -> heap 과 그리드 알고리즘 사용

import collections
import heapq


def solution(food_times: list, k: int) -> int:
    answer = 0
    heap = []
    for food_idx, food_time in enumerate(food_times):
        heapq.heappush(heap, [food_time, food_idx + 1])

    prev_time = 0
    food_length = len(food_times)

    while heap:
        food_time, food_idx = heapq.heappop(heap)
        if (food_time - prev_time) * food_length <= k:
            k -= (food_time - prev_time) * food_length
            food_length -= 1
            prev_time = food_time
        else:
            heap.append([food_time, food_idx])
            heap.sort(key=lambda x: x[1])
            return heap[k % food_length][1]
    return -1


'''
def solution(food_times: list, k: int) -> int:
    answer = 0

    que = collections.deque()
    for idx, time in enumerate(food_times):
        que.append([time, idx + 1])
    # k == 0 일 때 까지 돌린다. 
    for _ in range(k):
        time, food_num = que.popleft()
        if time - 1 > 0:
            que.append([time - 1, food_num])
        if len(que) == 0:
            return - 1
    return que[0][1]
'''