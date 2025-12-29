def twoSum(nums:list[int], target : int)->list[int]:

            
        n = len(nums)
        hashmap={}
        for i in range(n):
                hashmap[nums[i]]=i
        
        for i in range(n):
                y = target - nums[i]
                if y in hashmap and hashmap[y]!=i:
                    return [i, hashmap[y]]
                

        

print(twoSum([2,7,11,15],9))


    
