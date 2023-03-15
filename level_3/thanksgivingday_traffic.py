# 추석 트래픽
# O(N) 

def convert(end_time: str, duration: str) -> list:
    duration_time = int(float(duration[:-1]) * 1000)
    # 끝 시간 정리
    end_time = end_time.split(':')
    end = int(end_time[0]) * 60 * 60 * 1000 + int(end_time[1]) * 60 * 1000 + int(float(end_time[2]) * 1000)
    return [end - duration_time + 1, end]


def solution(lines: list) -> int:
    answer = 0
    start_end = []
    # 최소시간과 최대시간 그리고 처리량들 찾기
    min_time, max_time = float('inf'), 0
    for line in lines:
        split_line = line.split()
        start, end = convert(split_line[1], split_line[2])
        min_time, max_time = min(min_time, start), max(max_time, end)
        start_end.append([start, end])
    # 최대 처리량 구하기
    for i in range(len(lines)):
        cur_end = start_end[i][1]
        count = 0
        for j in range(i, len(lines)):
            if cur_end > start_end[j][0] - 1000:
                count += 1
        answer = max(answer, count)
    return answer