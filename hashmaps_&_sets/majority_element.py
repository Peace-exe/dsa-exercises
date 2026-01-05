def majorityElement(nums : list[int]):

            numsCount = {
                    
            }
            for num in nums:
                    if num in numsCount:
                            numsCount[int(num)]+=1
                    else:
                            numsCount[int(num)]=1
            print(numsCount)

            for key in numsCount:
                    if numsCount[key] > len(nums)//2:
                            return key
             
            
            
print(majorityElement([1]))