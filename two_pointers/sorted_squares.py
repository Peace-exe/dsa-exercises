def sortedSquares(nums:list[int])->list[int]:
            #brute force method
            '''
            squared = [num**2 for num in nums]

            return sorted(squared)
            '''
            # optimal way

            left = 0 
            right = len(nums)-1
            res=[]
            while left<= right:
                    if abs(nums[left])> abs(nums[right]):
                            res.append(nums[left]**2)
                            left+=1
                    else:
                            res.append(nums[right]**2)
                            right-=1
            return res[::-1]
            