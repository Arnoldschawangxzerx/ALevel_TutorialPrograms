def binary_search(arr, target):
    """
    Performs binary search on a sorted list to find the target value.
    Returns the index of the target if found, otherwise -1.
    """
    left = 0
    right = len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2  # Calculate middle index
        
        if arr[mid] == target:
            return mid  # Target found at middle index
        elif arr[mid] < target:
            left = mid + 1  # Search right half
        else:
            right = mid - 1  # Search left half
    
    return -1  # Target not found


# Example usage (list must be sorted)
my_list = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
target_value = 23

result = binary_search(my_list, target_value)

if result != -1:
    print(f"Target {target_value} found at index {result}")
else:
    print(f"Target {target_value} not found in the list")
