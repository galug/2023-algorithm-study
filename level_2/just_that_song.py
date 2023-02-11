# 방금 그 곡
# N: len(musicinfos) M: 시간의 길이의 최대값
# 시간복잡도 : O(N * M)

# 총 음악 시간을 구한다.
def play_time(start_time: str, end_time: str) -> int:
    start_hour, start_minute, = map(int, start_time.split(':'))
    end_hour, end_minute = map(int, end_time.split(':'))
    total_minute = end_minute - start_minute
    if total_minute < 0:
        total_minute = 60 + total_minute
        end_hour -= 1
    return (end_hour - start_hour) * 60 + total_minute


# 시간 동안 연주하는 멜로디
def find_total_melody(time: int, melody: str) -> str:
    melody_len = len(melody)
    if melody_len > time:
        return melody[:time]
    repeat_div, repeat_mod = divmod(time, melody_len)
    return melody * repeat_div + melody[:repeat_mod]


def solution(m: str, musicinfos: list) -> str:
    answer = [0, '']
    # # 이 붙은 음들을 소문자로 변환하여 탐색에 용이하게 한다.
    replace_dic = {'C#': 'c', 'D#': 'd', 'F#': 'f', 'G#': 'g', 'A#': 'a'}
    for k, v in replace_dic.items():
        m = m.replace(k, v)
    for music_info in musicinfos:
        start_time, end_time, title, melody = music_info.split(',')
        music_time = play_time(start_time, end_time)
        for k, v in replace_dic.items():
            melody = melody.replace(k, v)

        total_melody = find_total_melody(music_time, melody)

        if m in total_melody and answer[0] < music_time:
            answer[0], answer[1] = music_time, title
    return answer[1] if answer[1] else '(None)'
