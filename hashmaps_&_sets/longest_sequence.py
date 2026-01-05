from collections import defaultdict
def longestConsecutive( nums: list[int]) -> int:

                numSet = set(nums)

                longest = 0
                length = 0
                nextNum = 0

                for num in numSet:
                        if num - 1 not in numSet:
                                nextNum= num+1
                                length = 1
                                while nextNum in numSet:
                                        nextNum+=1
                                        length+=1
                                longest = max(longest,length)
                return longest

                                



longestConsecutive([100,4,200,1,3,2])
