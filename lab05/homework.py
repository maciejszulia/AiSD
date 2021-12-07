from BinaryNode import BinaryNode
from BinaryTree import BinaryTree
from typing import List
from collections import deque


def left_line(tree: BinaryTree) -> List[BinaryNode]:
    output = []
    if tree.root is None:
        return
    queue = deque()
    queue.append(tree.root)
    while queue:
        size_q = len(queue)
        i = 0
        while i < size_q:
            current_node = queue.popleft()
            i += 1
            if i == 1:
                output.append(current_node.value)
            if current_node.left_child:
                queue.append(current_node.left_child)
            if current_node.right_child:
                queue.append(current_node.right_child)
    return output


tree = BinaryTree(10)

assert tree.root.value == 10
tree.root.add_right_child(2)
assert tree.root.right_child.value == 2
tree.root.right_child.add_right_child(1)
assert tree.root.right_child.is_leaf() is False
tree.root.add_left_child(1)
tree.root.left_child.add_left_child(1)
assert tree.root.left_child.left_child.value == 1
assert tree.root.left_child.left_child.is_leaf() is True
tree.root.left_child.left_child.add_right_child(1)

tree.show()
print(left_line(tree))
