"""
This module provides PQHeap, which creates an instance of the min-heap priority queue data structure

Requirements
------------
Python 3.7 or higher.

Notes
-----
Module is created as part of the group project for the final exam of DSXXX Algoritmer og datastrukturer.
"""
from typing import List


class CreateHeap():
    """

    """


def parent(i: int) -> int:
    """Return the index of the parent node of i from a heap like data structure

    i
        index of a node in heap like priority queue data structure, default is None.
    :return: int
    """
    return (i - 1) // 2


def left(i: int) -> int:
    """Return the index of the left child node of i from a heap like data structure

    i
        index of a node in heap like priority queue data structure, default is None.
    :return: int
    """
    return (2 * i) + 1


def right(i: int) -> int:
    """Return the index of the right child node of i from a heap like data structure

    i
        index of a node in heap like priority queue data structure, default is None.
    :return: int
    """
    return (2 * i) + 2


def extract_min(priority_q: List[int]) -> int:
    """
    Return the key of the element with the least priority from a heap like priority queue data structure

    priority_q
        A non-empty list of elements in a heap like data structure, Default is None
    :return: int
    """
    # TODO
    pass


def swap(p1, p2):
    pass


def insert(priority_q: List[int], num: int) -> None:
    """
    Insert key into priority_q.

    priority_q
        A non-empty list of elements in a heap like data structure, Default is None
    num
        An integer value that will be inserted into priority_q, Default is None
    :return: None:
    """
    priority_q.append(num)

    i = len(priority_q) - 1

    while i > 1 and priority_q[parent(i)] < priority_q[i]:
        temporary_value = priority_q[parent(i)]
        # swap places


def create_emptyPQ():
    """
    Return an empty heap like priority queue data structure

    :return: Empty priority queue
    """

    return []
