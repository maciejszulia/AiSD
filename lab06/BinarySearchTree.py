from BinaryNode import BinaryNode
from typing import Any


class BinarySearchTree:
    root: BinaryNode

    def __init__(self, root_val):
        self.root = BinaryNode(root_val)

    def insert(self, value: Any) -> None:
        pass

    def _insert(self, node: BinaryNode, value: Any) -> BinaryNode