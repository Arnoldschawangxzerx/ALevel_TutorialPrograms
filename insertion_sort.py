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
# Insertion sort
ub=count-1
lb=0
for i in range (lb+1,ub):
    key=array[i]
    place=i-1
    if array[place] > key:
        while place >= lb and array[place] > key:
            temp=array[place+1]
            array[place+1]=array[place]
            array[place]=temp
            place=place-1
        array[place+1]=key

print("The array after sorting is:", array[:count])
