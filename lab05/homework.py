from BinaryNode import BinaryNode
from BinaryTree import BinaryTree
from typing import List
from lab02.Queue import Queue


def left_line(tree: BinaryTree) -> List[BinaryNode]:
    # output to Lista ktora ma przechowywac binary nody
    output: List[BinaryNode] = []
    # zrob kolejke
    queue = Queue()
    # zakolejkuj korzeń
    queue.enqueue(tree.root)

    # gdy queue ma elementy:
    while queue:
        # dlugosc queue
        queue_size = len(queue)
        i = 0

        # gdy dlugosc kolejki jest wieksza od i
        # kod się wykonuje gdy w kolejce jest element
        while i < queue_size:
            # current node = zwróc pierwszy element z kolejki
            current_node = queue.dequeue()
            i += 1

            # gdy tylko jeden element w kolejce:
            if i == 1:
                # wrzuć do outputa
                output.append(current_node)
            # gdy element ma dzieci:
            if current_node.left_child:
                # zakolejkuj dziecko
                queue.enqueue(current_node.left_child)
            # same
            if current_node.right_child:
                queue.enqueue(current_node.right_child)

    return output


tree = BinaryTree(10)

tree.root.add_right_child(2)
tree.root.right_child.add_right_child(1)

tree.root.add_left_child(1)
tree.root.left_child.add_left_child(1)
tree.root.left_child.left_child.add_right_child(1)

tree.root.right_child.right_child.add_right_child(1)
tree.root.right_child.right_child.right_child.add_right_child(1)

tree.show()
print(left_line(tree))
