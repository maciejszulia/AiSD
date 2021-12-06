from typing import Any, Callable, List
from BinaryNode import BinaryNode


class BinaryTree:
    root: BinaryNode

    def __init__(self, value):
        self.root = BinaryNode(value)

    def traverse_in_order(self, visit: Callable[[Any], None]):
        self.root.traverse_in_order(visit)

    def traverse_post_order(self, visit: Callable[[Any], None]):
        self.root.traverse_post_order(visit)

    def traverse_pre_order(self, visit: Callable[[Any], None]):
        self.root.traverse_pre_order(visit)

    def show(self):
        self.root.show(0)

    def traverse_left_line(self) -> list[BinaryNode]:
        output = []

        def append_node(node):
            return output.append(node)

        append_node(self.root)
        if self.root.left_child is not None:
            self.traverse_left_line(append_node(self))

        return output

    def left_line(self) -> List[BinaryNode]:
        output = []

        def _output():
            output.append(self.root)

        self.root.traverse_pre_order(_output())
        return output
