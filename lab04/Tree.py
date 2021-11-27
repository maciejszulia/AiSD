from typing import Any, List, Callable
from TreeNode import TreeNode


class Tree:
    root: TreeNode

    def __init__(self, value):
        self.root = TreeNode(value)

    def __len__(self):
        pass

    def add(self, value: Any, parent_name: Any) -> None:
        pass

    def for_each_level_order(self, visit: Callable[['TreeNode'], None]) -> None:
        pass

    def for_each_deep_first(self, visit: Callable[['TreeNode'], None]) -> None:
        pass

    def show(self):
        pass

