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
