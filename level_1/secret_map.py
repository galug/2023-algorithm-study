# 비밀 지도
# n : 비밀 지도의 길이
# 시간 복잡도 : O(n **2) 공간 복잡도 : O(n ** 2)

def solution(n: int, arr1: list, arr2: list):
    answer = []
    for idx in range(n):
        # 2진수 변환 함수 
        binary_line = bin(arr1[idx] | arr2[idx])[2:]
        secret_line = ' ' * (n - len(binary_line)) + binary_line.replace('1', '#').replace('0', ' ')
        answer.append(secret_line)
    return answer
