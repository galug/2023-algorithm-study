# 신고 결과 받기 문제
# 시간 복잡도 : O(n ^^ 2)

import collections


def solution(id_list, report, k):
    answer = [0] * len(id_list)
    matching_idx_id_list = {}
    # idx와 id_list를 매칭한다.
    for idx, id in enumerate(id_list):
        matching_idx_id_list[id] = idx
    # 신고한 사람과 신고 당한 사람을 저장한다.
    reported_list = collections.defaultdict(set)
    for report_contents in report:
        reporter, reported_person = map(str, report_contents.split())
        reported_list[reported_person].add(reporter)
    # 신고 당한 사람들 중 일정 횟수를 넘어간 사람을 찾는 반복문
    for reported_person in reported_list:
        if len(reported_list[reported_person]) >= k:
            # 신고한 유저에게 결과 메일을 보내주는 반복문
            for reporter in reported_list[reported_person]:
                answer[matching_idx_id_list[reporter]] += 1
    return answer


'''
풀이 2 
def solution(id_list, report, k):
    answer = []
    # 신고한 사람과 신고 당한 사람을 저장한다.
    report_list = collections.defaultdict(set)
    reported_list = collections.defaultdict(int)
    ban = set()
    # 신고한 사람, 신고당한 사람을 뽑는 반복문 
    for report_contents in report:
        reporter, reported_person = map(str, report_contents.split())
        # 신고 당한 사람이 신고한 사람의 신고 리스트에 없다면 
        if reported_person not in report_list[reporter]:
            report_list[reporter].add(reported_person)
            reported_list[reported_person] += 1
            # 일정 신고 횟수를 넘어갔을 시 
            if reported_list[reported_person] >= k:
                ban.add(reported_person)
    # 모든 id_list를 돌아보는 반복문 
    for idx, id in enumerate(id_list):
        answer.append(0)
        # 신고를 한적이 없는 경우 continue
        if id not in report_list:
            continue
        # ban 당한 사람이 나의 신고 목록에 있을 경우 메일을 보내줌 
        for ban_person in ban:
            if ban_person in report_list[id]:
                answer[idx] += 1
    return answer
'''
