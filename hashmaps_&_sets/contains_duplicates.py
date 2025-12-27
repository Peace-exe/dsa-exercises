def containsDuplicate( nums: list[int]) -> bool:
                seen = {

                }

                for i in nums:
                        if i in seen:
                                return True
                        else:
                                seen[i]=1
                return False