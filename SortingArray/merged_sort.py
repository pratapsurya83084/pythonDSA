def merge_sort(arr):
    # base case
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    leftarr = merge_sort(arr[:mid])
    rightarr = merge_sort(arr[mid:])

    i = j = 0
    mergeArr = []

    # merge step
    while i < len(leftarr) and j < len(rightarr):
        if leftarr[i] < rightarr[j]:
            mergeArr.append(leftarr[i])
            i += 1
        else:
            mergeArr.append(rightarr[j])
            j += 1

    # append any leftover elements
    mergeArr.extend(leftarr[i:])
    mergeArr.extend(rightarr[j:])

    return mergeArr

arr = [9, 4, 3, 2, -3, -1, 0]
print("before sorting array is:", arr)
arr = merge_sort(arr)
print("after sorting array:", arr)
