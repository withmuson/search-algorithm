def binary_search(list, target):
    """
    Performs a binary search on the list for the target value.

    Args:
      list: The list to search.
      target: The value to search for.

    Returns:
      The index of the target value in the list, or -1 if the target value is not found.
    """
    low = 0
    high = len(list) - 1
    while low <= high:
        mid = (low + high) // 2
        if list[mid] == target:
            return mid
        elif list[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


list = [3, 4, 5, 6, 7, 8, 9]
target = 8
index = binary_search(list, target)

print("The index of the target value is:", index)