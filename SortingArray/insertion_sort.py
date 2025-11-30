

# insertion sort
def insertion_sort(arr):
    if len(arr)>=1:
        n=len(arr)
        for i in range(1,n):
            curr = arr[i];
            prev = i-1;
            while prev>=0 and curr < arr[prev]:
                arr[prev+1] = arr[prev]
                prev-=1
                
            arr[prev+1] = curr
            
            
arr=[9,4,9,0,-2,5,-1]
print("before sorting array : ", arr)
insertion_sort(arr)  
print("after sorting array is :",arr)












