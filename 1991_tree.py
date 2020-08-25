n = int(input())
node_list = {}


def preorder(root, node_list):
    if root != '.':
        left = node_list[root][0]
        right = node_list[root][1]

        print(root, end="")
        preorder(left, node_list)  # left preorder
        preorder(right, node_list)  # right preorder


def inorder(root, node_list):
    if root != '.':
        left = node_list[root][0]
        right = node_list[root][1]

        preorder(left, node_list)  # left preorder
        print(root, end="")
        preorder(right, node_list)  # right preorder


def postorder(root, node_list):
    if root != '.':
        left = node_list[root][0]
        right = node_list[root][1]

        preorder(left, node_list)  # left preorder
        print(root, end="")
        preorder(right, node_list)  # right preorder


for _ in range(n):
    root, left, right = input().split()
    node_list[root] = [left, right]

preorder("A", node_list)
inorder("A", node_list)
postorder("A", node_list)
