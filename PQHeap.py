

def parent(i):
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
    

def insert(priority_q, num):

    priority_q.append(num)

    i = len(priority_q) - 1


    while i > 1 and priority_q[parent(i)] < priority_q[i]:
        temporary_value = priority_q[parent(i)]
        ## swap places


            

    

def createEmptyPQ():
    return []

