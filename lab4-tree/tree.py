from typing import Any, List, Callable, Union


class TreeNode:
    value: Any
    children: List['TreeNode']

    def __init__(self, value):
        self.value = value
        self.children = []

    def __str__(self):
        return str(self.value)

    def is_leaf(self) -> bool:
        if len(self.children) == 0:
            return True
        return False

    def add(self, child: 'TreeNode') -> None:
        self.children.append(child)

    # def for_each_deep_first(self, visit: Callable[['TreeNode'], None]) -> None:
    #     visit(self)
    #     for i in self.children:
    #         i.for_each_deep_first(visit)


class Tree:
    root: TreeNode
