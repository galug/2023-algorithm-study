# 파괴되지 않은 건물 -> 누적합을 이용한 풀이
# n 은 가로 길이 m 은 세로 길이 
# 시간복잡도 : O(n * m)
import sys


def solution(board: list, skill: list) -> int:
    answer = 0
    vertical, horizontal = len(board), len(board[0])
    # 누적합을 위한 세팅
    sum_array = [[0] * horizontal for _ in range(vertical)]
    for selection, r1, c1, r2, c2, degree in skill:
        calculated_degree = degree * (-1 if selection == 1 else 1)
        sum_array[r1][c1] += calculated_degree
        if r2 + 1 < vertical:
            sum_array[r2 + 1][c1] += calculated_degree * -1
        if c2 + 1 < horizontal:
            sum_array[r1][c2 + 1] += calculated_degree * -1
        if r2 + 1 < vertical and c2 + 1 < horizontal:
            sum_array[r2 + 1][c2 + 1] += calculated_degree
    # 누적합을 구하는 과정
    for y in range(vertical):
        for x in range(horizontal):
            if x > 0:
                sum_array[y][x] += sum_array[y][x - 1]
    for y in range(vertical):
        for x in range(horizontal):
            if y > 0:
                sum_array[y][x] += sum_array[y - 1][x]
    # 정답과 누적합을 더해서 정답의 개수를 센다.
    for y in range(vertical):
        for x in range(horizontal):
            if board[y][x] + sum_array[y][x] > 0:
                answer += 1
    return answer
