import heapq

class PriorityQueue:
    def __init__(self):
        self.queue = []

    def push(self, item, priority):
        # heapq is a min-heap, so we use priority as the first element
        heapq.heappush(self.queue, (priority, item))

    def pop(self):
        # Returns item with smallest priority value
        if self.queue:
            return heapq.heappop(self.queue)[1]
        return None

    def peek(self):
        # Look at the highest priority item without removing
        if self.queue:
            return self.queue[0][1]
        return None

    def is_empty(self):
        return len(self.queue) == 0


# Example usage
pq = PriorityQueue()
pq.push("Task A", 3)   # Lower number = higher priority
pq.push("Task B", 1)
pq.push("Task C", 2)

print("Next task:", pq.pop())   # Task B (priority 1)
print("Next task:", pq.pop())   # Task C (priority 2)
print("Next task:", pq.pop())   # Task A (priority 3)
