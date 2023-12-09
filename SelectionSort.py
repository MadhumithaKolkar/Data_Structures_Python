def selection_sort(arr):
    size = len(arr)

    # We are keeping it as size-1 because we need a value j which will be an index value after i
    for i in range (size-1):
        min_index = i
        for j in range(min_index+1,size):
            if arr[j] < arr[min_index]:
                min_index = j

        if i != min_index: # It is already sorted, so no need to swap arr[i] with arr[min_index] when i==min_index
            arr[i], arr[min_index] = arr[min_index], arr[i]

if __name__ == '__main__':
    e = [22,6,8,2,12,656,12]
    d = [99]
    selection_sort(e)
    print(e)