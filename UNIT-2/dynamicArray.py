
# DYNAMIC ARRAY SIMULATION (RESIZE + POP)

# UNDERSTANDING HOW DYNAMIC ARRAYS GROW AND WHY APPEND IS AMORTIZED O(1).

# DYNAMIC ARRAY : Array that automatically resizes (usually doubles) when full, allowing variable
#                 size unlike fixed arrays. Append is amortized O(1) due to rare resizes.

class DynamicArray:
    def __init__(self):
        self.size = 0              # Number of elements in array
        self.capacity = 1          # Initial capacity
        self.array = [None] * self.capacity

    def append(self, item):
        # Resize if array is full
        if self.size == self.capacity:
            self._resize(2 * self.capacity)

        self.array[self.size] = item
        self.size += 1
        print(f"Appended {item} -> Size: {self.size}, Capacity: {self.capacity}")

    def pop(self):
        if self.size == 0:
            print("Array is empty, nothing to pop.")
            return None

        popped_item = self.array[self.size - 1]
        self.array[self.size - 1] = None
        self.size -= 1
        print(f"Popped {popped_item} -> Size: {self.size}, Capacity: {self.capacity}")
        return popped_item

    def _resize(self, new_capacity):
        new_array = [None] * new_capacity
        for i in range(self.size):
            new_array[i] = self.array[i]
        self.array = new_array
        self.capacity = new_capacity

    def __str__(self):
        return str([self.array[i] for i in range(self.size)])


# Example usage
if __name__ == "__main__":
    dyn_arr = DynamicArray()

    # Append elements
    for i in range(6):
        dyn_arr.append(i)

    # Pop elements
    dyn_arr.pop()
    dyn_arr.pop()

    print("Final Array:", dyn_arr)
