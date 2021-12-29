from typing import Any
from lab05.BinaryNode import BinaryNode


class BinaryNode:
    value: Any
    left_child: 'BinaryNode'
    right_child: 'BinaryNode'

    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None

    def __repr__(self):
        return str(self.value)

    def min(self) -> BinaryNode:
