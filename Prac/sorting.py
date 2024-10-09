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


arr = [13, 46, 24, 52, 20, 9]
print(selection_sort(arr))
a = [3,5,7,8,90]
print(bubble_sort(a))
