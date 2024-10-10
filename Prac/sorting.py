def selection_sort(arr):
    for i in range(len(arr) - 1):
        smallest = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[smallest]:
                smallest = j
        arr[i], arr[smallest] = arr[smallest], arr[i]
    return arr

def bubble_sort(arr):
    for i in range(len(arr)):
        print("running")  # This is to show the optimized code , when sorted , only runs once
        swap = 0
        for j in range(len(arr)-i-1):
            if arr[j]>arr[j+1]:
                swap = 1
                arr[j],arr[j+1] = arr[j+1],arr[j]
        if swap == 0:
            break
    return arr

def merge_sort(arr):
    def divide(arr):
        if len(arr) == 1:
            return arr
        n = len(arr)//2
        left = divide(arr[:n])
        right = divide(arr[n:])

        return merge(left,right)

    def merge(l,r):
        merged_array = []
        i = 0
        j = 0

        while i<len(l) and j<len(r):
            if l[i]<r[j]:
                merged_array.append(l[i])
                i += 1
            else:
                merged_array.append(r[j])
                j+=1

        if i<len(l):
            merged_array.extend(l[i:])

        if j<len(r):
            merged_array.extend(r[j:])

        return merged_array

    sorted = divide(arr)
    return sorted

def binary_search(arr,target):
    l = 0
    r = len(arr)-1

    while l<r:
        mid = (l+r)//2
        if arr[mid]==target:
            return mid+1
        elif arr[mid]>target:
            r = mid-1
        else :
            l = mid + 1

    return -1

# arr = [13, 46, 24, 52, 20, 9]
# print(selection_sort(arr))
# a = [3,5,7,8,90]
# print(bubble_sort(a))
arr = [3,4,5,6,7,8,9]
arr.sort()
res = binary_search(arr,6)
print(f"6 is at index : {res}")
arr = [3,1,2,4,1,5,2,6,4]
print(merge_sort(arr))
