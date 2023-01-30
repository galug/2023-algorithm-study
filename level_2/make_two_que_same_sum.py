# 두큐 합 같게 만들기 문제
# N : que 의 길이(len(queue1))
# 시간 복잡도 : O(N) 공간 복잡도 : O(N)
import collections


def solution(queue1: list, queue2: list) -> int:
    answer = 0
    # queue1 의 합과 queue2 의 합을 구한다.
    sum_of_que1 = sum(queue1)
    sum_of_que2 = sum(queue2)
    # 두 수의 합이 홀수 인 경우 같은 큐의 합을 내는 것은 불가능
    if (sum_of_que1 + sum_of_que2) % 2 == 1:
        return -1
    # que 두 개를 2번은 섞을 생각을 해야한다.
    limit = len(queue1) * 4
    # 큐 두 개를 queue 자료형으로 만든다.
    que1 = collections.deque(queue1)
    que2 = collections.deque(queue2)

    # 각 que 의 길이가 0이 아니거나 limit 를
    while sum_of_que1 and sum_of_que2 and answer <= limit:
        # que1의 합이 que2 의 합과 같을 때
        if sum_of_que1 == sum_of_que2:
            return answer
        # que1의 합이 que2의 합보다 작을 때
        if sum_of_que1 < sum_of_que2:
            pop_num = que2.popleft()
            que1.append(pop_num)
            sum_of_que2 -= pop_num
            sum_of_que1 += pop_num
        # que2 의 합이 que1의 합보다 작을 때
        else:
            pop_num = que1.popleft()
            que2.append(pop_num)
            sum_of_que1 -= pop_num
            sum_of_que2 += pop_num

        answer += 1
    # 조건에 맞는 결과를 내는 것이 불가능하므로 -1 반환
    return -1
