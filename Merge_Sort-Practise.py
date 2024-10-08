def merge_sort(arr):
    if len(arr)<=1:
        return

    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]

    merge_sort(left)
    merge_sort(right)

    merge_two_sorted_arrays(left,right,arr)

def merge_two_sorted_arrays(left,right,arr):

    i=j=k=0

    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            arr[k]=left[i]
            i+=1
        else:
            arr[k]=right[j]
            j+=1
        k+=1

    while i<len(left):
        arr[k]=left[i]
        i+=1
        k+=1

    while j<len(right):
        arr[k]=right[j]
        j+=1
        k+=1

arr = [5,1,76,9,4,1,765,3432,0]
merge_sort(arr)
print(arr)

