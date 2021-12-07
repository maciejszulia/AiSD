from BinaryNode import BinaryNode
from BinaryTree import BinaryTree
from typing import List
from lab02.Queue import Queue


def left_line(tree: BinaryTree) -> List[BinaryNode]:
    output: List[BinaryNode] = []
    # if tree.root is None:
    #     return
    queue = Queue()
    queue.enqueue(tree.root)
    while queue:
        queue_size = len(queue)
        i = 0
        while i < queue_size:
            current_node = queue.dequeue()
            i += 1

            if i == 1:
                output.append(current_node.value)
            if current_node.left_child:
                queue.enqueue(current_node.left_child)
            if current_node.right_child:
                queue.enqueue(current_node.right_child)

    return output


tree = BinaryTree(10)

tree.root.add_right_child(2)
tree.root.right_child.add_right_child(1)

tree.root.add_left_child(1)
tree.root.left_child.add_left_child(1)
tree.root.left_child.left_child.add_right_child(1)

tree.show()
print(left_line(tree))
