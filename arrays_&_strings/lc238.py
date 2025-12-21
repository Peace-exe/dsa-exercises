def productExceptSelf(self, nums: list[int]) -> list[int]:

    start=1
    end=0
    res=[]

    while end<len(nums):
        
        if(start==end):
            end+=1
        
        