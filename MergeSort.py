def merge_sort(arr):
    if len(arr)<=1:
        return

    mid = len(arr)//2

    left = arr[:mid]
    right = arr[mid:]

    merge_sort(left)
    merge_sort(right)

    merge_two_sorted_lists(left,right,arr)

def merge_two_sorted_lists(a,b,arr):
    print("This is a",a)
    print("This is b", b)
    len_a = len(a)
    len_b = len(b)

    i = j = k = 0

    while i<len_a and j <len_b:
        if a[i] <= b[j]:
            arr[k] = a[i]
            i+=1
        else:
            arr[k] = b[j]
            j += 1
        k +=1
    while i<len_a:
        arr[k] = a[i]
        i+=1
        k+=1
    while j<len_b:
        arr[k] = b[j]
        j+=1
        k+=1


arr = [5,1,76,9,4,1,765,3432]
merge_sort(arr)
print(arr)
