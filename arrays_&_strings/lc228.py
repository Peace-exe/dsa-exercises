
def summaryRanges(nums:list[int]) -> list[int] :
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if(len(nums)==0):
                return []
        
        start = nums[0]
        end = nums[0]
        res=[]
        
        for i in range(len(nums)):
                if i != len(nums)-1:
                        if end +1 == nums[i+1]:
                                end+=1
                        else:
                                if(start==end):
                                        
                                        res.append(f"{end}")
                                        end=nums[i+1]
                                        start=end
                                else:
                                        res.append(f"{start}->{end}")
                                        end=nums[i+1]
                                        start=end
                                        
                else:   
                        if(start==end):
                                res.append(f"{end}")
                        else:
                                res.append(f"{start}->{end}")
        return res

nums1 = [0,2,3,4,6,8,9]
print(summaryRanges(nums1))
