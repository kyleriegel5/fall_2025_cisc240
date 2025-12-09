#!/usr/bin/env python3
from typing import Any, override


class Node:
    def __init__(self, data: Any) -> None:
        self.data: Any = data
        self.next: int | None = None
        self.prev: int | None = None

    @override
    def __str__(self) -> str:
        return f"Node data: {self.data} Next node: {self.next} Previous node: {self.prev}"


class LinkedList:
    def __init__(self) -> None:
        self.head: int | None = None
        self.tail: int | None = None
        self.linked_list: list[Node] = []

    @override
    def __str__(self) -> str:
        if self.head is None:
            return ""

        out_str = ""
        index = self.head
        visited = set()

        while index is not None:

            if index in visited:
                break
            visited.add(index)

            node = self.linked_list[index]
            out_str += f"{node}\n"
            index = node.next

        return out_str.rstrip("\n")

    def zero_list(self) -> None:
        self.head: int | None = None
        self.tail: int | None = None
        self.linked_list: list[int | Node] = [0] * len(self.linked_list)

    def append(self, data: Any) -> None:
        new_node: Node = Node(data)

        if self.head is None:
            self.head = 0
            self.tail = 0

        if len(self.linked_list):
            for index, value in enumerate(self.linked_list):
                if value == 0:
                    new_node.prev = self.tail
                    self.linked_list[index] = new_node
                    if self.tail != index:
                        self.linked_list[self.tail].next = index
                        self.tail = index
                    self.__make_circular()
                    return

            new_node.prev = self.tail
            self.linked_list[self.tail].next = len(self.linked_list)
            self.tail = len(self.linked_list)

        self.linked_list.append(new_node)
        self.__make_circular()

    def remove_node(self, index: int) -> None:
        node = self.linked_list[index]

        if node.prev is not None:
            self.linked_list[node.prev].next = node.next
        else:
            self.head = node.next

        if node.next is not None:
            self.linked_list[node.next].prev = node.prev
        else:
            self.tail = node.prev

        self.linked_list[index] = 0
        self.__make_circular()

    def __make_circular(self) -> None:
        self.linked_list[self.head].prev = self.tail
        self.linked_list[self.tail].next = self.head


def print_by_index(linked_list: LinkedList) -> None:
    for index, node in enumerate(linked_list.linked_list):
        if node:
            print(f"Index: {index} {node}")

def to_list(ll: LinkedList) -> list[int]:
    values = []
    index = ll.head
    visited = set()

    while index is not None and index not in visited:
        visited.add(index)
        node = ll.linked_list[index]
        if node != 0:
            values.append(node.data)
        index = node.next

    return values

def radix_sort(list_in: list[int]) -> list[int]:

    list_out: list[int] = list_in.copy()
    max_val: int = max(list_out)

    temp_array: list[list[int]] = [[] for _ in range(10)]
    exponent: int = 1

    while max_val // exponent > 0:
        while len(list_out) > 0:
            val = list_out.pop()
            index = (val // exponent) % 10
            temp_array[index].append(val)

        for bucket in temp_array:
            while len(bucket) > 0:
                val = bucket.pop()
                list_out.append(val)

        exponent *= 10

    return list_out

def main():
    # Instantiate a LinkedList
    ll: LinkedList = LinkedList()
    
    print(ll)

    # Add ten values in order
    for number in range(1, 11):
        ll.append(number)
    print(ll)

    # zero out our list and add values
    ll.zero_list()

    # appending on a zeroed out list
    ll.append(128)

    # adding an out of order node to simulate a list with gaps
    ll.tail = 9
    ll.linked_list[ll.tail] = Node(444)
    ll.linked_list[ll.tail].prev = ll.head
    ll.linked_list[ll.tail].next = ll.head
    ll.linked_list[ll.head].prev = ll.tail
    ll.linked_list[ll.head].next = ll.tail

    # Appnding 5 entries to see if they are placed correctly
    ll.append(212)
    ll.append(687)
    ll.append(555)
    ll.append(777)
    ll.append(999)

    print("\nDoubly/Circularly linked list in array order:")
    print_by_index(ll)

    print("\nDoubly/Circularly linked list in list order:")
    print(ll)
    
    print("\nThe node at the 3rd index has been removed:")
    ll.remove_node(3)
    print_by_index(ll)
    
    print("\nDoubly/Circularly linked list data sorted in a list:")
    ll_list = to_list(ll)
    print(radix_sort(ll_list))

if __name__ == "__main__":
    main()
