def binarySearch(nums):
    n = len(nums)
    for i in range(n):
        for j in range(n-i-1):
            if nums[j]>nums[j+1]:
                temp = nums[j]
                nums[j]=nums[j+1]
                nums[j+1]=temp

    return nums

arr = [3,7,2,9,23,8,1,5,0]
print(binarySearch(arr))