def merge_sort(arr):
    if len(arr)<=1:
        return arr

    mid = len(arr)//2

    left = arr[:mid]
    right = arr[mid:]

    merge_sort(left)
    merge_sort(right)

    print(f"Left : {left}, right : {right}")

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

def max_product_sub_array(nums):
    maxP = float("-inf")
    for i in range(len(nums)):
        product = 1
        for j in range(i,len(nums)):
            product *= nums[j]
            maxP = max(maxP,product)

    return maxP

def recursive_binary_search(nums,left,right,k):
    if right < left:
        return -1

    mid = (left + right) // 2

    if nums[mid] == k:
        return mid
    elif nums[mid] > k:
        return recursive_binary_search(nums,left, mid - 1,k)
    else:
        return recursive_binary_search(nums,mid + 1, right,k)

def lower_bound(nums,x):
    left,right = 0,len(nums)-1

    while left<right:
        mid = (left+right)//2

        if nums[mid]>=x:
            right = mid
        else:
            left = mid+1

    return left

def upper_bound(nums,x):
    left,right = 0,len(nums)-1

    while left<right:
        mid = (left+right)//2

        if nums[mid]<=x:
            left = mid+1
        else:
            right = mid

    return left


# arr = [5,1,76,9,4,1,765,3432]
# merge_sort(arr)
# print(arr)
# print(max_product_sub_array([2,3,-2,4,0,10]))
nums = [3,5,8,15,19,19,19,20]
print(recursive_binary_search(nums,0,len(nums)-1,43))
print(lower_bound(nums,19))
print(upper_bound(nums,19))
