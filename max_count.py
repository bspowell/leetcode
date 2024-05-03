def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        # Check if the middle element is the target
        if arr[mid] == target:
            return mid  # Return the index of the target element

        # If the target is smaller, search the left half
        elif arr[mid] > target:
            high = mid - 1

        # If the target is larger, search the right half
        else:
            low = mid + 1

    return -1  # Return -1 if the target is not found
