import random
import time


# Implementation of the binary search algorithm
# Illustrate the effeciency of the algorithm compared  to naive search.

def naive_search(l, target):
    """
    Perform naive search to find the target element.

    Parameters:
    l (list): A list of elements
    target (int): The element to search for

    Returns:
    int: The index of the target element if found, else -1
    """
    for i in range(len(l)):
        if l[i] == target:
            return i
    return -1


# binary search uses divide and conquer
# we will leverage the fact that our list is SORTED


def binary_search(l, target, low=None, high=None):
    """
    Perform binary search on a sorted list to find the target element.

    Parameters:
    l (list): A sorted list of elements
    target (int): The element to search for
    low (int): The lower index of the search range
    high (int): The upper index of the search range

    Returns:
    int: The index of the target element if found, else -1
    """
    if low is None:
        low = 0
    if high is None:
        high = len(l) - 1
    if high < low:
        return -1

    midpoint = (low + high) // 2

    if l[midpoint] == target:
        return midpoint
    elif target < l[midpoint]:
        return binary_search(l, target, low, midpoint - 1)
    else:
        return binary_search(l, target, midpoint + 1, high)


if __name__ == "__main__":
    length = 10000
    # build a sorted list of 10000
    sorted_list = set()
    while len(sorted_list) < length:
        sorted_list.add(random.randint(-3 * length, 3 * length))

    sorted_list = sorted(list(sorted_list))

    start = time.time()

    for target in sorted_list:
        naive_search(sorted_list, target)
    end = time.time()
    print("Naive search time: ", (end - start) / length, "seconds")

    start = time.time()

    for target in sorted_list:
        binary_search(sorted_list, target)
    end = time.time()
    print("Binary search time: ", (end - start) / length, "seconds")
