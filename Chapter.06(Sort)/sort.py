def selection_sort(arr):
    print('selection_sort')
    print('Before : ',arr)
    for i in range(len(arr)):
        min_index = i
        for j in range(i+1,len(arr)):
            if arr[min_index] > arr[j]:
                min_index = j
        arr[min_index], arr[i] = arr[i], arr[min_index]
    print('After : ',arr)

def insertion_sort(arr):
    print('insertion_sort')
    print('Before : ',arr)
    for i in range(1,len(arr)):
        for j in range(i,0,-1):
            if arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
            else:
                break
    print('After : ',arr)
    
def quick_sort(arr, start, end):
    if start >= end:
        return 
    pivot = start
    left = start+1
    right = end
    while left <= right:
        while left <= end and arr[left] <= arr[pivot]: left+=1
        while right > start and arr[right] >= arr[pivot]: right-=1
        if left <= right:
            arr[left], arr[right] = arr[right], arr[left]
        else:
            arr[pivot], arr[right] = arr[right], arr[pivot]
    quick_sort(arr, start, right-1)
    quick_sort(arr, left, end) 
        
arr1 = [5,7,9,0,3,1,6,2,4,8]
arr2 = [5,7,9,0,3,1,6,2,4,8]
arr3 = [5,7,9,0,3,1,6,2,4,8]

selection_sort(arr1)
insertion_sort(arr2)
quick_sort(arr3,0,len(arr3)-1)
print(arr3)