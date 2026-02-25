# Preallocate an array with a fixed size
size = int(input("Enter the maximum size of the array: "))
array = [None] * size  # Initialize an array with `None`
count = 0              # Counter to track the number of elements added

# Adding elements to the array manually
while count < size:
    value = input(f"Enter value for position {count}: ")
    array[count] = int(value)  # Insert value at the current position (converted to int for sorting)
    count += 1                 # Move to the next position

# Print the final array before sorting
print("The array before sorting is:", array[:count])

# Bubble Sort Implementation
for top in range(count - 1, 0, -1):  # Start from the last element and decrease the range
    for i in range(top):  # Compare up to the current top index
        if array[i] > array[i + 1]:  # Compare adjacent elements
            # Swap the elements
            temp = array[i]
            array[i] = array[i + 1]
            array[i + 1] = temp

# Print the sorted array
print("The sorted array is:", array[:count])
