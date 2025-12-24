def productExceptSelf(nums: list[int]) -> list[int]:

    res=[]
    prefix=[]
    suffix = []
    
    leftProd = 1
    rightProd = 1
    if not nums:
        return []
    
    for i in range(len(nums)):

        if(i==0):
            prefix.append(leftProd)
        else:
            leftProd=prefix[i-1]*nums[i-1]
            prefix.append(leftProd)
    
    for j in range(len(nums)-1,-1,-1):
        if(j==len(nums)-1):
            suffix.append(rightProd)
        else:
            rightProd=suffix[len(suffix)-1]*nums[j+1]
            suffix.append(rightProd)
    
    suffix= suffix[::-1]

    for k in range(len(nums)):
        res.append(prefix[k]*suffix[k])
    
    return res

nums=[1,2,3,4]
print(productExceptSelf(nums))

    
        
        