def threeSum(nums):

                nums.sort()
                low = 1
                high = len(nums)-1
                res=[]

                for i in range(len(nums)):
                        
                        low= i+1
                        high= len(nums)-1
                        
                        if nums[i]>0:
                                break
                        elif i>0 and nums[i]==nums[i-1]:
                                continue
                        
                        while low < high :
                                if nums[i]+nums[low]+nums[high]==0:
                                        res.append([nums[i],nums[low],nums[high]])
                                        low+=1
                                        high-=1

                                        while low<high and nums[low]==nums[low-1]:
                                                low+=1
                                        while low<high and nums[high]==nums[high+1]:
                                                high-=1
                                        
                                        
                                elif nums[i]+nums[low]+nums[high]<0:
                                        '''
                                        if nums[low]!=nums[low+1]:
                                                low+=1
                                        else:
                                                low+=2
                                        '''
                                        low+=1
                                elif nums[i]+nums[low]+nums[high]>0:
                                        '''
                                        if nums[high]!=nums[high-1]:
                                                high-=1
                                        else:
                                                high-=2
                                        '''
                                        high-=1
                        

                return res

                    
                    

print(threeSum([-1,0,1,2,-1,-4]))