# 파일명 정렬
# n : len(files) m : len(file)
# 시간 복잡도: O(n log n + n*m)

# HEAD 구분자와 숫자를 찾아내는 함수
def find_number(file: str):
    number_start_idx, number = 0, 0
    for idx, ch in enumerate(file):
        if ch.isnumeric():
            number_start_idx = idx
            end_idx = number_start_idx

            while end_idx < len(file) and file[end_idx].isnumeric():
                end_idx += 1
            number = int(file[number_start_idx: end_idx])
            break
    return number_start_idx, number

# files 를 정렬할 수 있게 list 로 다시 초기화
def init(files: list) -> list:
    temp = []
    for file in files:
        number_start_idx, number = find_number(file)
        temp.append([file[:number_start_idx].lower(), number, file])
    return temp


def solution(files: list) -> list:
    answer = init(files)
    answer.sort(key=lambda x: (x[0], x[1]))
    return list(map(lambda x: x[2], answer))
