# 이모티콘 할인율 -> 완전 탐색
# N: 이모티콘의 개수(len(emoticons)) M: 유저의 수 (len(users))
# 시간 복잡도 : O(4 ** N  * N * M) 공간 복잡도 : O()
from itertools import product


def solution(users: list, emoticons: list) -> list:
    answer = [0, 0]
    number_of_users = len(users)
    # 이모티콘에 대해 나올 수 있는 할인율의 경우를 반복
    for pro in product((10, 20, 30, 40), repeat=len(emoticons)):
        # 이모티콘의 할인율에 따른 유저의 구매 금액을 저장한다.
        users_purchase_amount = [0] * len(users)
        for d_idx, discount in enumerate(pro):
            for user_idx in range(number_of_users):
                if users[user_idx][0] <= discount:
                    users_purchase_amount[user_idx] += (emoticons[d_idx] * (100 - discount) // 100)
        # 유저의 구매 금액으로 이 유저가 구독을 할지 이모티콘을 구매할지 판단한다.
        total_subscribe, total_purchase_amount = 0, 0
        for user_idx in range(number_of_users):
            if users[user_idx][1] <= users_purchase_amount[user_idx]:
                total_subscribe += 1
                continue
            total_purchase_amount += users_purchase_amount[user_idx]
        # 구독 개수와 구매 금액의 순차적인 최대 개수를 구한다.
        if [total_subscribe, total_purchase_amount] > answer:
            answer[0], answer[1] = total_subscribe, total_purchase_amount
    return answer
