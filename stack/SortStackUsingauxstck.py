def sort_stack(input_stack):
    auxiliary_stack = []

    # Process all elements in the input stack
    while input_stack:
        temp = input_stack.pop()   # Pop the top element

        # Move elements from auxiliary_stack back to input_stack
        # if they are larger than temp
        while auxiliary_stack and auxiliary_stack[-1] > temp:
            input_stack.append(auxiliary_stack.pop())

        # Place temp in correct position
        auxiliary_stack.append(temp)

    # Move all sorted elements back to input_stack - after sorting
    while auxiliary_stack:
        input_stack.append(auxiliary_stack.pop())

    return input_stack


# Example
stack = [34, 3, 31, 98, 92, 23]
print("Original Stack:", stack)

sorted_stack = sort_stack(stack)
print("Sorted Stack:  ", sorted_stack)
