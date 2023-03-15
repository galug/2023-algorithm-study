# 길찾기 문제 -> 트리 문제
# N :len(nodeinfos)
# O(N log N)

import sys

sys.setrecursionlimit(1000000)


class Tree():
    def __init__(self, key, value, left, right):
        self.key = key
        self.value = value
        self.left = None
        self.right = None


def insert(root: Tree, new_node: Tree):
    parent = root
    while True:
        if parent.value < new_node.value:
            if parent.right:
                parent = parent.right
                continue
            parent.right = new_node
            return
        if parent.value > new_node.value:
            if parent.left:
                parent = parent.left
                continue
            parent.left = new_node
            return


def preorder(root: Tree, path: list):
    if not root:
        return
    path.append(root.key)
    if root.left:
        preorder(root.left, path)
    if root.right:
        preorder(root.right, path)


def postorder(root: Tree, path: list):
    if not root:
        return
    if root.left:
        postorder(root.left, path)
    if root.right:
        postorder(root.right, path)
    path.append(root.key)


def solution(nodeinfo: list) -> list:
    for idx, node in enumerate(nodeinfo):
        nodeinfo[idx].append(idx + 1)
    # 트리를 생성
    nodeinfo.sort(key=lambda x: (-x[1], x[0]))
    root = Tree(nodeinfo[0][2], nodeinfo[0][0], None, None)
    for node in nodeinfo[1:]:
        insert(root, Tree(node[2], node[0], None, None))
    # 전위 순회
    preorders = []
    preorder(root, preorders)
    # 후위 순회
    postorders = []
    postorder(root, postorders)

    return [preorders, postorders]