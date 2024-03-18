"""
This module functions as a program that implements the data structure priority queue.

Requirements
------------
Python 3.7 or higher.

Notes
-----
Module is created as part of the group project for the final exam of DSXXX Algoritmer og datastrukturer.
"""

def parent(i:int) -> int:
    """Return the index of the parent node of i from a heap like data structure


    """
    return (i-1)//2
    
def left(i):
    return (2 * i) + 1
    
def right(i):
    return (2 * i) + 2


def extractMin(priority_q):
    # Chris udkast til denne TODO.
    # test
    pass

def swap(p1, p2):
    pass

def insert(priority_q, num):

    priority_q.append(num)

    i = len(priority_q) - 1


    while i > 1 and priority_q[parent(i)] < priority_q[i]:
        temporary_value = priority_q[parent(i)]
        ## swap places


            

    

def createEmptyPQ():
    return []

