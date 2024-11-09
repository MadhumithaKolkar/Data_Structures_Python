def left(arr):
    temp = arr[0]
    for i in range(1, len(arr)):
        arr[i - 1] = arr[i]
    arr[i] = temp
    return arr

def rotate(nums,k):
    k = k%len(nums)
    def helper(l,r):
        while l<r:
            nums[l] , nums[r] = nums[r] , nums[l]
            l += 1
            r -= 1

    helper(0,k-1)
    helper(k,len(arr)-1)
    helper(0,len(arr)-1)

    return arr

def move(nums):
    i = 0

    for j in range(len(nums)):
        if nums[j] != 0:
            if i!=j:
                nums[i] , nums[j] = nums[j] , nums[i]
            i += 1

    return nums

def union(n1,n2):
    res = []
    i,j = 0,0

    while i<len(n1) and j<len(n2):
        if n1[i]<n2[j]:
            if not res or n1[i] != res[-1]:
                res.append(n1[i])
            i += 1
        elif n2[j] < n1[i]:
            if not res or n2[j] != res[-1]:
                res.append(n2[j])
            j += 1
        else:
            if not res or n1[i] != res[-1]:
                res.append(n1[i])
            i += 1
            j += 1

    while i<len(n1):
        if n1[i] != res[-1]:
            res.append(n1[i])
        i += 1

    while j<len(n2):
        if n2[j] != res[-1]:
            res.append(n2[j])
        j += 1

    return res

def inter(n1,n2):
    ans = []
    visit = [0 for i in range(len(n2))]

    for i in range(len(n1)):
        for j in range(len(n2)):
            if n1[i]==n2[j] and visit[j]==0:
                ans.append(n1[i])
                visit[j] = 1
            if n2[j]>n1[i]:
                break
    return ans

def intersection(n1,n2):
    ans = []
    i,j = 0,0

    while i<len(n1) and j<len(n2):
        if n1[i] < n2[j]:
            i += 1
        elif n2[j] < n1[i]:
            j += 1
        else:
            ans.append(n1[i])
            i += 1
            j += 1

    return ans

def missing(nums,n):
    xor1 = 0
    xor2 = 0
    for i in range(len(nums)):
        xor1 = xor1^(i+1)
        xor2 = xor2^(nums[i])
    return xor1^xor2^n

def once_element(nums):
    # count_map = {}
    #
    # for num in nums:
    #     count_map[num] = 1+count_map.get(num,0)
    #
    # for num,count in count_map.items():
    #     if count == 1:
    #         return num
    #
    # return -1
    xor = 0
    for num in nums:
        xor = xor^num
    return xor

def longest_subarray(nums,k):
    # maxL = 0
    # length = 0
    # i = 0
    # sum = 0
    #
    # for j in range(len(nums)):
    #     sum += nums[j]
    #     while sum>k and i<j:
    #         sum -= nums[i]
    #         i += 1
    #     if sum == k:
    #         length = j-i+1
    #         maxL = max(maxL,length)
    # return maxL

    maxL = 0
    hMap = {}
    hMap[0] = -1
    sum = 0

    for i in range(len(nums)):
        sum += nums[i]
        if sum-k in hMap:
            maxL = max(maxL,i-hMap[sum-k])
        if sum not in hMap:
            hMap[sum] = i
    return maxL

def zeros(arr):
    k = 0
    for i in range(3):
        for j in range(k,len(nums)):
            while nums[j]==i and k<j:
                k += 1
                nums[k],nums[j] = nums[j],nums[k]
    return nums


# arr = [1, 2, 3, 4, 5, 6, 7]
# # print(left(arr))
# print(rotate(arr,2))
# nums = [0,1,0,2,3,2,0,0,4,5,1]
# print(move(nums))
arr1 = [1, 2, 4, 4, 5, 6, 6, 7, 8]
arr2 = [2, 4, 6]
print(union(arr1,arr2))
print(inter(arr1,arr2))
print(intersection(arr1,arr2))
nums = [1,2,4,5]
n = 5
print(missing(nums,n))

nums = [1,2,2,4,5,4,1,3,5]
print(f"The number appearing only once is : {once_element(nums)}")

nums = [1,2,-3,1,2]
k = 4
print(f"Long : {longest_subarray(nums,3)}")

print(zeros([0,1,2,0,1,2,1,2,0,0,0,1]))