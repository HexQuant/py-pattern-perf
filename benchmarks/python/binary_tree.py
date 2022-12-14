import random
from dataclasses import dataclass

class Node:
    __slots__ = ('data', 'leftChild', 'rightChild')

    def __init__(self, data) -> None:
        self.data = data
        self.leftChild:Node = None
        self.rightChild:Node = None

    def insert(self, data) -> None:
        if data < self.data:
            if self.leftChild:
                self.leftChild.insert(data)
            else:
                self.leftChild = Node(data)
                return
        else:
            if self.rightChild:
                self.rightChild.insert(data)
            else:
                self.rightChild = Node(data)
                return

    def search(self, val):
        if val == self.data:
            return self.data
        elif val < self.data:
            if self.leftChild:
                return self.leftChild.search(val)
            else:
                return None
        else:
            if self.rightChild:
                return self.rightChild.search(val)
            else:
                return None


randomlist = random.sample(range(0, 9000), 1000)



def func_a():
    root = Node(4500)
    for val in randomlist:
        root.insert(val)

    root.search(9000)


if __name__ == '__main__':

    from myprofiler.myprofiler import do_profile
    do_profile(
        'Binary tree', (
            ('naive class', 'func_a'),
        ),
        number=100
    )
