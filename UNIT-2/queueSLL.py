
# QUEUE USING SLL (O(1) OPERATIONS)

# IMPLEMENTING QUEUE WITH HEAD + TAIL POINTERS AND CONNECT TO BFS USAGE.

# QUEUE USING SLL :  Queue implemented on SLL with front (dequeue) and rear (enqueue) pointers. 
#                    FIFO order. Enqueue at tail O(1), dequeue at head O(1)

class Node:
    def __init__(self, data):
        self.data = data      # Value stored in the node


# Queue implemented using singly linked list
class Queue:
    def __init__(self):
        self.head = None     
        self.tail = None      

    # Enqueue operation (insert)
    def enqueue(self, data):
        new_node = Node(data)
        if self.tail is None:         # If queue is empty
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node # Link old node to new node
            self.tail = new_node      # Update node pointer
        print(f"Enqueued {data}")

    # Dequeue operation (remove)
    def dequeue(self):
        if self.head is None:         # If queue is empty
            print("Queue Underflow")
            return None
        dequeued = self.head.data    
        self.head = self.head.next    # Move head to next node
        if self.head is None:         # If queue becomes empty
            self.tail = None          # Reset
        print(f"Dequeued {dequeued}")
        return dequeued

    # Front operation (peek at front)
    def front(self):
        if self.head is None:
            print("Queue is empty")
            return None
        return self.head.data         # Return front value


    # Traverse for debugging
    def traverse(self):
        temp = self.head
        print("Queue:", end=" ")
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")


# Example usage
if __name__ == "__main__":
    q = Queue()
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)
    q.traverse()

    print("Front element:", q.front())
    q.dequeue()
    q.traverse()
    q.dequeue()
    q.dequeue()
    q.dequeue()  # Underflow case