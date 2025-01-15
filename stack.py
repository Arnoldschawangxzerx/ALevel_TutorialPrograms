stack = [None] * 10  # Initialize the stack with size stack_size
basepointer = 0              # Bottom pointer
toppointer = -1             # Top pointer (indicating the stack is empty)
stack_size = 10             # Stack size (maximum capacity)
item = None         # Variable to hold the popped value

def pop():
    global toppointer, item
    if toppointer == basepointer - 1:
        print("!!UNDERFLOW!! Stack is empty, cannot pop")
    else:
        item = stack[toppointer]
        stack[toppointer] = None  # Clear the value from the stack
        toppointer -= 1
        print(f"Popped: {item}")

def push(new_item):
    global toppointer
    if toppointer < stack_size - 1:
        toppointer += 1
        stack[toppointer] = new_item
        print(f"Pushed: {new_item}")
    else:
        print("!!OVERFLOW!! Stack is full, cannot push")

def peek():
    a=stack[toppointer]
    print("The top element is ", a)

# Example Usage
push(5)  # Push an item onto the stack
push(10) # Push another item
push(20) # Push another item
push(10) # Push another item
push(10) # Push another item
push(10) # Push another item
push(10) # Push another item
push(10) # Push another item
push(10) # Push another item
push(10) # Push another item
push(10) # Attempt to push on a full stack
peek()      # Returns the ltop element without removing it
pop()    # Pop the last item
pop()    # Pop the next item
pop()    # Pop the next item
pop()    # Pop the next item
pop()    # Pop the next item
pop()    # Pop the next item
pop()    # Pop the next item
pop()    # Pop the next item
pop()    # Pop the next item
pop()    # Pop the next item
pop()    # Attempt to pop from an empty stack
