# 셔틀 버스  -> que 를 이용한 문제
# 시간복잡도: O(n * len(timetables))

import collections
import bisect


def time_to_total(time: str) -> int:
    hour, minute = map(int, time.split(':'))
    return 60 * hour + minute


def total_to_time(total_time: int) -> str:
    hour, minute = divmod(total_time, 60)
    return '%02d:%02d' % (hour, minute)


def solution(n: int, t: int, m: int, timetable: list) -> str:
    answer = ''
    # total_time table 생성
    time_tables = list(map(time_to_total, timetable))
    time_tables.sort()
    # 버스 셔틀 시간표 생성
    start_time = time_to_total('09:00')
    bus_time_tables = []
    for bus_count in range(n):
        bus_time_tables.append(start_time + bus_count * t)
    # 버스 시간당 타는 사람들
    time_table_idx = 0
    bus_people = collections.defaultdict(list)
    que = collections.deque(time_tables)

    for bus_time in bus_time_tables:
        # 버스 도착 전에 도착하는 사람들
        bus_people_count = 0
        while que and que[0] <= bus_time and bus_people_count < m:
            bus_people[bus_time].append(que.popleft())
            bus_people_count += 1
    last_time = bus_time_tables[-1]
    #
    if len(bus_people[last_time]) < m:
        return total_to_time(last_time)
    #
    return total_to_time(bus_people[last_time][-1] - 1)