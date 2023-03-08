# 표 편집 -> linked_list 를 이용한 풀이
# m : len(cmd)
# 시간복잡도 : O( n * m )

def solution(n: int, k: int, cmd: list) -> str:
    table = ['O' for _ in range(n)]
    delete_stack = []
    linked_list = {i: [i - 1, i + 1] for i in range(n)}
    # linked_list[i] = [prev,next]
    for i in range(n):
        linked_list[i] = [i - 1, i + 1]

    for command in cmd:
        if command[0] in 'UD':
            UD = {'U': 0, 'D': 1}
            c, ud = command.split()
            ud = int(ud)
            for _ in range(ud):
                k = linked_list[k][UD[c]]
        # 삭제
        if command[0] == 'C':
            delete_stack.append(k)
            table[k] = 'X'
            prev_, next_ = linked_list[k][0], linked_list[k][1]
            # 맨 끝의 노드를 삭제했을 때
            if next_ == n:
                linked_list[prev_][1] = next_
                k = prev_
            else:
                # 맨 첫 노드를 삭제한 경우
                if prev_ != -1:
                    linked_list[prev_][1] = next_
                linked_list[next_][0] = prev_
                k = next_
        # 복구
        if command[0] == 'Z':
            pop = delete_stack.pop()
            prev_, next_ = linked_list[pop][0], linked_list[pop][1]
            # 맨 앞의 노드를 복구할 경우
            if prev_ != -1:
                linked_list[prev_][1] = pop
            # 맨 뒤의 노드를 복구할 경우
            if next_ != n:
                linked_list[next_][0] = pop
            table[pop] = 'O'
    return ''.join(table)
