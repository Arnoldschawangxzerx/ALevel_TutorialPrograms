def insertion_sort(arr):
    """
    Sorts a list in ascending order using insertion sort algorithm.
    Returns the sorted list.
    """
    # Start from second element (index 1)
    for i in range(1, len(arr)):
        key = arr[i]  # Element to be inserted
        j = i - 1
        
        # Move elements greater than key one position ahead
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]  # Shift element right
            j -= 1
        
        arr[j + 1] = key  # Insert key in correct position
    
    return arr


# Example usage
my_list = [12, 11, 13, 5, 6]

sorted_list = insertion_sort(my_list)

print("Sorted list:", sorted_list)
