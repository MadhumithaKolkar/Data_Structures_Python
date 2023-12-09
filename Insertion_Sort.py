def insertion_Sort(nums):

    for i in range(len(nums)):
        temp = nums[i]
        j = i-1
        while j>=0 and nums[j]>temp:
            nums[j+1]=nums[j]
            j-=1
        nums[j+1]=temp
    return nums


nums = [9,8,2,4,7,1,5,0]
print(insertion_Sort(nums))