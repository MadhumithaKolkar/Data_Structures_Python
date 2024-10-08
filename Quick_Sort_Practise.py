def quick_Sort(nums,start,end):
    if start>=end:
        return

    pivot = partition(nums,start,end)

    quick_Sort(nums,start,pivot-1)
    quick_Sort(nums,pivot+1,end)


def partition(nums,start,end):
    pivot = nums[end]
    j = start
    i = j-1

    for j in range(start,end+1):
        if nums[j]<pivot:
            i+=1
            temp = nums[i]
            nums[i]=nums[j]
            nums[j] = temp
    i+=1
    temp = nums[i]
    nums[i]= nums[j]
    nums[j] = temp

    return i

nums = [5,1,4,9,6,2,0,1]
quick_Sort(nums,0,len(nums)-1)
print(nums)