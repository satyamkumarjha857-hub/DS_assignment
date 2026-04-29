def counting_sort(arr):
    if not arr:
        return arr

    # Find the maximum element in arr.
    max_value = max(arr)

    # Create a count array to store the count of each unique object in the input array.
    count = [0] * (max_value + 1)

    # Count the occurrence of each element in the input array and store it in the count array.
    for number in arr:
        count[number] += 1

    # Update the input array with sorted numbers based on the count array.
    for i in range(1, len(count)):
            count[i] += count[i - 1]
    output = [0] * len(arr)

    for i in range(len(arr) - 1, -1, -1):
        output[count[arr[i]] - 1] = arr[i]
        count[arr[i]] -= 1

    return output

# Example usage
arr = [4, 2, 2, 8, 3, 3, 1]
sorted_arr = counting_sort(arr) 
print("Sorted array:", sorted_arr)