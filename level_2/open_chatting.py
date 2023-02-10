# 오픈 채팅방 문제 -> 완전 탐색
# N : 레코드의 길이(len(record))
# 시간 복잡도 : O()

state_dic = {'Enter': '님이 들어왔습니다.', 'Leave': '님이 나갔습니다.'}


def solution(record: list) -> list:
    answer = []
    uid_nickname = {}
    # uid 와 들어왔습니다 나갔습니다만 저장
    for r in record:
        state, uid_and_nickname = r.split(' ', 1)
        if state == 'Enter':
            uid, nickname = uid_and_nickname.split()
            uid_nickname[uid] = nickname
            answer.append([uid, state_dic[state]])
        if state == 'Leave':
            answer.append([uid_and_nickname, state_dic[state]])
        if state == 'Change':
            uid, nickname = uid_and_nickname.split()
            uid_nickname[uid] = nickname
    # 최종 uid-nickname 쌍 기준으로 result 생성 
    return list(map(lambda x: uid_nickname[x[0]] + x[1], answer))
