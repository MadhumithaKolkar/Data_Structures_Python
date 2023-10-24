import time

# Not that efficient, just to try making an algorithm for sorting. Has O(n*logn) time complexity :P
def madhumitha_sort(arr):
    if len(arr) <= 1:
        return arr

    # Split the input array into two halves
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    # Recursively sort the two halves
    left = madhumitha_sort(left)
    right = madhumitha_sort(right)

    # Interleave the sorted halves
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Append the remaining elements
    result.extend(left[i:])
    result.extend(right[j:])
    return result

if __name__ == '__main__':
    arr = [i for i in range (1000000)]

    start_time = time.time()
    sorted_arr = madhumitha_sort(arr)
    end_time = time.time()
    milliseconds = (end_time - start_time) * 1000

    # print("Sorted array:", sorted_arr)
    print("Time taken {:.6f} milliseconds".format(milliseconds))