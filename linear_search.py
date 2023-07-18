def linear_search(list, target):
    """
    Performs a linear search on the list for the target value.

    Args:
      list: The list to search.
      target: The value to search for.

    Returns:
      The index of the target value in the list, or -1 if the target value is not found.
    """
    for i in range(len(list)):
        if list[i] == target:
            return i
    return -1


list = [39, 26, 9, 11, 7, 14, 20]
target = 20
index = linear_search(list, target)

print("The index of the target value is:", index)