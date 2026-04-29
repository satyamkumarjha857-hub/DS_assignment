
# SINGLY LINKED LIST (CORE OPERATIONS)

# IMPLEMENTING DYNAMIC INSERTION AND DELETION WITHOUT SHIFTING

# SINGLY LINKED LIST : Linear data structure of nodes where each node contains data 
#                      + next pointer to the next node. One-way traversal from head to tail (last node's next = null).
 
class Node:
    def __init__(self, data):
        self.data = data   # Stores the value
        self.next = None   # Points to the next node


class SinglyLinkedList:
    def __init__(self):
        self.head = None   # Start of the list

    # Insert at the beginning
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head   # New node points to old head
        self.head = new_node        # Head now becomes new node
        print(f"Inserted {data} at beginning")

    # Insert at the end
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:       # If list is empty
            self.head = new_node
            print(f"Inserted {data} at end (first node)")
            return
        temp = self.head
        while temp.next:            # Traverse till last node
            temp = temp.next
        temp.next = new_node        # Link last node to new node
        print(f"Inserted {data} at end")

    # Delete by value
    def delete_by_value(self, value):
        if self.head is None:
            print("List is empty")
            return

        # If head itself holds the value
        if self.head.data == value:
            self.head = self.head.next
            print(f"Deleted {value} from list")
            return

        # Search for the node to delete
        temp = self.head
        while temp.next and temp.next.data != value:
            temp = temp.next

        if temp.next is None:
            print(f"Value {value} not found")
        else:
            temp.next = temp.next.next
            print(f"Deleted {value} from list")

    # Traverse and print list
    def traverse(self):
        if self.head is None:
            print("List is empty")
            return
        temp = self.head
        print("Linked List:", end=" ")
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")


# Example usage
if __name__ == "__main__":
    sll = SinglyLinkedList()
    sll.insert_at_beginning(10)
    sll.insert_at_beginning(5)
    sll.insert_at_end(20)
    sll.insert_at_end(30)
    sll.traverse()

    sll.delete_by_value(20)
    sll.traverse()

    sll.delete_by_value(100)  # Value not present
    sll.traverse()