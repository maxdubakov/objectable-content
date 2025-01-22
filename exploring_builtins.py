from copy import copy
from typing import List


class Hollow:
    def __init__(self, habitat: str):
        self.habitat = habitat

    def __repr__(self):
        return f"Hollow('{self.habitat}')"


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
        self._age = age
        self.tree_type = tree_type
        self.hollows: List[Hollow] = []

    # __len__ is useful if there is ONE meaning of it that can be easily interpreted
    def __len__(self):
        return len(self.hollows)

    # __repr__ should return a string which can be copy-pasted to the REPL and reproduce the same object
    # if it's not possible due to any constraints (like, file buffer initialization), it must be covered with <>
    def __repr__(self):
        return f"Tree({self.age}, '{self.tree_type}')"

    def __str__(self):
        return f"Tree {self.tree_type.title()} {self.age} years old with {len(self.hollows)} hollows in it."

    # not particularly correct as it does not look at hollows
    def __eq__(self, other: "Tree"):
        return self.age == other.age and self.tree_type == other.tree_type

    # also does not copy hollows of a tree
    def __copy__(self):
        return Tree(self.age, self.tree_type)

    def __iter__(self):
        return iter(self.hollows)

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        if age < 0:
            raise ValueError("Age cannot be negative")

        self._age = age

    def add_hollow(self, hollow: Hollow) -> "Tree":
        self.hollows.append(hollow)
        return self


if __name__ == "__main__":
    tree1 = Tree(10, "oak")

    # check __len__ which returns number of hollows
    print(f"Tree's Length : {len(tree1)}")

    # check __repr__, should print readable/viable object
    print(f"Tree's repr   : {repr(tree1)}")

    # if __str__ is implemented, python will use this to print out the object
    print(f"Tree's str    : {tree1}")

    # check __copy__ and __eq__
    tree1_copy = copy(tree1)
    print(f"Copies equal  : {tree1 == tree1_copy}")

    # check age getter/setter
    print(f"Age           : {tree1.age}")

    # set it to the good value
    tree1.age = 11
    print(f"Age           : {tree1.age} (set successfully)")

    try:
        print("\nTrying to set age to value that is not allowed... ", end="")
        tree1.age = -1
    except ValueError as e:
        print(e)

    # add hollows using add_hollow
    tree1.add_hollow(Hollow("owl")).add_hollow(Hollow("squirrel"))

    # iterate over tree's hollows
    print("Hollows       :")
    for hollow in tree1:
        print(f"Hollow        : {hollow}")
