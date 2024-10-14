def largest(arr):
    large = arr[0]
    for i in range(len(arr)):
        if arr[i]>large:
            large = arr[i]
    return large

def second_largest(arr):
    if len(arr)< 2 : return None
    largest = second = float("-inf")
    smallest = second_small = float("inf")
    for i in range(len(arr)):
        if arr[i]>largest:
            second = largest
            largest = arr[i]
        elif arr[i]>second and arr[i]!=largest:
            second = arr[i]
        # Smallest
        if arr[i]<smallest:
            second_small = smallest
            smallest = arr[i]
        elif arr[i]<second_small and arr[i]!=smallest:
            second_small = arr[i]
    return second,second_small

def remove(arr):
    i = -1
    for j in range(0,len(arr)):
        if arr[j]!=arr[i]:
            i+=1
            arr[i],arr[j] = arr[j],arr[i]
    return arr[:i+1]

arr = [1,2,3,2,6,7,4,1,7]
print(largest(arr))
print(second_largest(arr))
arr = [1,1,1,2,2,3,4,6,7]
print(remove(arr))