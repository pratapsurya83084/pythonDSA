# bubble sort

def bubble_sort(arr):
    if len(arr) > 1:
        n = len(arr)
        for i in range(n):
            for j in range(0 , n-1):
                if arr[j] > arr[j+1]:
                    # swap j and j+1
                    temp = arr[j]
                    arr[j] = arr[j+1]
                    arr[j+1] = temp





arr = [9,3,3,2,7,0,-1]
print("before sorted array is:",arr)
bubble_sort(arr);
print("after sorted array : " , arr)










