import array

# array(typecode, [elements])
arr = array.array('i', [1, 6, 3, 0 , 4, 5])   # 'i' = integer array

# Selection Sort
for i in range(len(arr)):
    for j in range(i, len(arr)):
        if arr[i] > arr[j]:
            tmp = arr[i]
            arr[i] = arr[j]
            arr[j] = tmp

print(arr)

# Output: array('i', [1, 3, 4, 5, 6])
