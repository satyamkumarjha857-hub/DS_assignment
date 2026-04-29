
# STACK USING SLL + PARENTHESES CHECKER

# BUILDING STACK USING LINKED LIST AND APPLY TO BRACKET VALIDATIONS.

# STACK USING SLL : Stack implemented on top of SLL where top pointer = stack top. 
#                   Push/pop at head (O(1)). LIFO order using SLL nodes.

class Node:
    def __init__(self, data):
        self.data = data      # Value stored in the node
        self.next = None      # Pointer to the next node


# Stack implemented using singly linked list
class Stack:
    def __init__(self):
        self.top = None       # Points to the top of the stack

    # Push operation
    def push(self, data):
        new_node = Node(data)     # Create a new node
        new_node.next = self.top  # Link new node to current top
        self.top = new_node       # Update top to new node
        print(f"Pushed {data}")

    # Pop operation
    def pop(self):
        if self.top is None:      # If stack is empty
            print("Stack Underflow")
            return None
        popped = self.top.data    # Get value at top
        self.top = self.top.next  # Move top to next node
        print(f"Popped {popped}")
        return popped

    # Peek operation
    def peek(self):
        if self.top is None:
            print("Stack is empty")
            return None
        return self.top.data      # Return value at top without removing


# Function to validate parentheses and brackets
def parentheses(string):
    stack = Stack()
    opening = "([{"
    closing = ")]}"
    mapping = {')': '(', ']': '[', '}': '{'}

    for char in string:
        if char in opening:
            stack.push(char)      # Push opening bracket
        elif char in closing:
            if stack.top is None: # No matching opening
                return False
            top_char = stack.pop()
            if mapping[char] != top_char:  # Check match
                return False

    return stack.top is None      # Valid if stack is empty at end


# Example usage
if __name__ == "__main__":
    expr1 = "([{}])"
    expr2 = "([)]"
    expr3 = "([]{})"

    print(expr1, "->", parentheses(expr1))
    print(expr2, "->", parentheses(expr2))
    print(expr3, "->", parentheses(expr3))