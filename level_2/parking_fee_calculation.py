# 주차 요금 계산
# N : records 의 개수(len(records))
# 시간 복잡도 O(N) 공간 복잡도 O(N)
import collections

base_time, base_fee, unit_time, unit_fee = 0, 0, 0, 0
cars_per_time = collections.defaultdict(int)

# 초기화 과정
def init(fees: list, records: list) -> list:
    global base_time, base_fee, unit_time, unit_fee
    base_time, base_fee, unit_time, unit_fee = fees
    records_account = collections.defaultdict(list)
    # 차량 번호에 따른 입차 출차 시간 초기화
    for record in records:
        time, cars_number, in_or_out = record.split()
        hour, minute = map(int, time.split(':'))
        records_account[cars_number].append(hour * 60 + minute)
    for car_number in records_account:
        in_and_out_length = len(records_account[car_number])
        # 마지막 출차 시간이 없는 경우
        if in_and_out_length % 2 == 1:
            records_account[car_number].append(23 * 60 + 59)
            in_and_out_length += 1
        # 총 주차 시간 계산
        for in_and_out_idx in range(0, in_and_out_length - 1, 2):
            cars_per_time[car_number] += records_account[car_number][in_and_out_idx + 1] - records_account[car_number][
                in_and_out_idx]

# 주차 요금을 계산하는 과정
def calculate() -> dict:
    cars_per_fee = collections.defaultdict(int)
    for car_number, time in cars_per_time.items():
        # 기본 요금에 대한 계산
        calculate_time = time - base_time
        cars_per_fee[car_number] = base_fee
        if calculate_time <= 0:
            continue
        # 추가 요금에 대한 계산
        div, mod, = divmod(calculate_time, unit_time)
        if mod > 0:
            div += 1
        cars_per_fee[car_number] += div * unit_fee
    return cars_per_fee


def solution(fees: list, records: list) -> list:
    init(fees, records)
    cars_per_fee = calculate()
    # 차량 번호순으로 정렬 후 출력
    keys = list(cars_per_fee.keys())
    keys.sort()
    answer = [cars_per_fee[key] for key in keys]
    return answer


