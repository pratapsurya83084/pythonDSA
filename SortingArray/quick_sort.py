def quick_sort(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)
        quick_sort(arr, low, pivot_index - 1)
        quick_sort(arr, pivot_index + 1, high)

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    # iterate from low to high-1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]   # swap
    # place pivot after the last smaller element
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i + 1

# example
arr = [9, 4, 9, 0, -2, 5, -1]
print("before sorting:", arr)
quick_sort(arr, 0, len(arr) - 1)
print("after sorting: ", arr)
