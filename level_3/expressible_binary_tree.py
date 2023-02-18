# 표현 가능한 이진식 -> dfs 를 통한 tree 문제 해결
# N: binary_tree_len , M : len(numbers)
# 시간 복잡도 : O( N * log N * M)

# tree_len 을 구하는 함수
def make_max_tree_len(binary_tree_len: int) -> int:
    tree_height = 1
    while tree_height * 2 - 1 < binary_tree_len:
        tree_height *= 2
    max_tree_len = tree_height * 2 - 1
    return max_tree_len


# 문제의 조건에 맞는 이진 트리식을 구하는 함수
def make_binary_tree(number: int) -> str:
    binary_tree = ''
    binary_tree_len = 0
    while number > 0:
        div, mod = divmod(number, 2)
        binary_tree = str(mod) + binary_tree
        number //= 2
        binary_tree_len += 1

    max_tree_len = make_max_tree_len(binary_tree_len)
    return (max_tree_len - binary_tree_len) * '0' + binary_tree

# left ~ right 까지를 하나의 트리로서 본다.
def dfs(binary_tree: list, left: int, right: int):
    global is_binary
    if left == right:
        return
    root = (left + right) // 2
    if binary_tree[root] == '0' and '1' in binary_tree[left: right + 1]:
        is_binary = False
        return
    if binary_tree[root] == '0':
        return
    dfs(binary_tree, left, root - 1)
    dfs(binary_tree, root + 1, right)


is_binary = True


def init():
    global is_binary
    is_binary = True


def solution(numbers: list) -> list:
    global is_binary
    answer = []
    for number in numbers:
        init()
        binary_tree = make_binary_tree(number)
        dfs(binary_tree, 0, len(binary_tree) - 1)
        answer.append(1 if is_binary else 0)
    return answer


