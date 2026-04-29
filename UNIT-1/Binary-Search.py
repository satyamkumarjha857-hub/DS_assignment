
# RECURSSIvE BINARY SEARCH

# RECURSIVE BINARY SEARCH IS AN ALGORITHM THAT FINDS A TARGET ELEMENT FROM A SORTED
#  ARRAY BY REPEATEDLY DIVIDING THE SEARCH INTERVAL IN HALF USING RECURSSION.

def binarySearch(arr, key, low, high):
    if low > high:
        return -1  # Not found
    mid = (low + high) // 2
    if arr[mid] == key:
        return mid
    elif arr[mid] > key:
        return binarySearch(arr, key, low, mid - 1)
    else:
        return binarySearch(arr, key, mid + 1, high)


# Test
arr = [1, 3, 5, 7, 9, 11, 13]
print("Search 7:", binarySearch(arr, 7, 0, len(arr)-1))   # Expected index 3
print("Search 11:", binarySearch(arr, 11, 0, len(arr)-1))   # Expected -1
