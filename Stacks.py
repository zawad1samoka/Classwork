stack = [] # create an empty list to represent the stack

# add 10, 20 & 30 to the top of the stack respectively
stack.append(10)
stack.append(20)
stack.append(30)

print("Stack after pushes: ", stack) # expected: [10, 20, 30]

# peek at the top element(last element on the list)
top_element = stack[-1] # access last element without removing it
print("Top element is: ", top_element) # expected: 30

# check if stack is empty
if len(stack) == 0:
    print("Stack is empty")
else:
    print("Stack is NOT empty") # expected here

# the second method is via custom classes. Here
# we implement a stack class with all key implementations

class SimpleStack:
    def __init__(self):
        # initialize an empty list to hold stack elements
        self.items = []

    def is_empty(self):
        # return true if the stack has no elements otherwise return false
        return len(self.items) == 0

    # add item to the top of the stack
    def push(self, item):
        self.items.append(item)

    # remove item from the top of the stack
    def pop(self):
        # if stack is empty return an error to avoid an invalid operation
        if self.is_empty():
            raise Exception("Cannot pop an empty stack")
        return self.items.pop()

    # return the top item without removing it
    def peek(self):
        # raise an error if stack is empty
        if self.is_empty():
            raise Exception("Cannot peek an empty stack")
        # the top most element is the last to be pushed
        # since the actual size of the list is greater than
        # position by one, minus one returns the last element
        return self.items[-1]

    # return the number of all items in the stack
    def sixe(self):
        return len(self.items)

    # print all items in the stack from top to bottom
    def print_stack(self):
        print("Stack from bottom to top: ", self.items)
        return

# execute
if __name__ == "__main__":
    # instantiate the stack class by creating an object for it
    stack1 = SimpleStack()

    # push some elements
    stack1.push(1000)
    stack1.push(2000)
    stack1.push(3000)

    # print the elements
    stack1.print_stack()

    # peek top element
    print("Top element: ", stack1.peek()) # expected: 3000

    # pop elements
    print("Popped: ", stack1.pop())
    stack1.print_stack() # expected: [1000, 2000]

    # check if empty
    print("Is stack empty? ", stack1.is_empty()) # expected: False

    # pop all to empty
    stack1.pop()
    stack1.pop()
    print("Is stack empty now? ", stack1.is_empty())
