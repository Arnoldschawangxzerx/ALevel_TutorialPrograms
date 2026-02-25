def linear_search(arr, target):
    """
    Performs linear search on a list to find the target value.
    Returns the index of the target if found, otherwise -1.
    """
    for index in range(len(arr)):
        if arr[index] == target:
            return index  # Target found, return current index
    return -1  # Target not found after checking all elements


# Example usage
my_list = [5, 2, 8, 1, 9]
target_value = 8

result = linear_search(my_list, target_value)

if result != -1:
    print(f"Target {target_value} found at index {result}")
else:
    print(f"Target {target_value} not found in the list")
