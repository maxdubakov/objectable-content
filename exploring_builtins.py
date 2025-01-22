from copy import copy
from typing import List


class Hollow:
    def __init__(self, habitat: str):
        self.habitat = habitat


class Tree:
    # its good practice to make constructor to only assign values
    # and maybe init something quickly, but no heavy sync operations like reading from a file

    # types assigned to args (int, str) are never checked by Python's compiler,
    # so they don't affect efficiency -- only readability
    def __init__(
        self,
        age: int,
        tree_type: str,
    ):
        self.age = age
        self.tree_type = tree_type
        self.hollows: List[Hollow] = []

    # __len__ is useful if there is ONE meaning of it that can be easily interpreted
    def __len__(self):
        return len(self.hollows)

    # __repr__ should return a string which can be copy-pasted to the REPL and reproduce the same object
    # if it's not possible due to any constraints (like, file buffer initialization), it must be covered with <>
    def __repr__(self):
        return f"Tree({self.age}, '{self.tree_type}')"

    def __eq__(self, other):
        return self.age == other.age and self.tree_type == other.tree_type

    def __copy__(self):
        return Tree(self.age, self.tree_type)


if __name__ == "__main__":
    tree1 = Tree(10, "oak")

    # check __len__ which returns number of hollows
    print(len(tree1))

    # check __repr__, should print readable/viable object
    print(tree1)

    # check __copy__ and __eq__
    tree1_copy = copy(tree1)
    print(tree1 == tree1_copy)
