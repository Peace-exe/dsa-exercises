def numJewelsInStones(jewels: str, stones: str)->int:

                    hashmap = {
                            
                    }
                    count=0
                    for i in jewels:
                            if i in hashmap:
                                    hashmap[i]+=1
                            else:
                                    hashmap[i]=1

                    for j in stones:
                            
                            if j in hashmap:
                                    count+=1


                    return count
print(numJewelsInStones("z","aAAbbbb"))