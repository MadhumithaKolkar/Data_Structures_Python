def quickSort(nums,start,end):
    if end<= start : return

    pivot = helper(nums,start,end)
    quickSort(nums,start,pivot-1)
    quickSort(nums,pivot+1,end)


def helper(nums,start,end):
    pivot = nums[end]
    j = start
    i = start-1

    for j in range(start,end+1):
        if nums[j]<pivot:
            i+=1
            tmp = nums[i]
            nums[i]=nums[j]
            nums[j]=tmp
    i+=1
    tmp = nums[i]
    nums[i]=nums[j]
    nums[j]=tmp
    return i

nums = [8,2,4,7,1,3,9,6,5,3,3,3,3,5,7,2,5,7,2]
quickSort(nums,0,len(nums)-1)
print(nums)

