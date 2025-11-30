# selection sort

def selection_sort(arr):
    if len(arr) > 1:
        n = len(arr);
        for i in range(n):
            smallest = i;
            for j in range(i+1,n):
                if arr[smallest] > arr[j]:
                    smallest = j
                    #swapp i and j
                    # temp = arr[i]
                    # arr[i]=arr[smallest]
                    # arr[smallest]=temp
            # swap 
            tmp = arr[i];
            arr[i]=arr[smallest];
            arr[smallest]=tmp;




arr = [9,3,3,2,7,0,-1]
print("before sorted array is:",arr)
selection_sort(arr);
print("after sorted array : " , arr)










