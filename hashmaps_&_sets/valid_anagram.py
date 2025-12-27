def isAnagram(s: str, t: str) -> bool:

        hashmap={

        }

        for i in s:
                if i in hashmap:
                        hashmap[i]+=1
                else:
                        hashmap[i]=1
        print(hashmap)
        for c in t:
                if c not in hashmap or hashmap[c]==0:
                        return False
                elif hashmap[c]>1:
                        hashmap[c]-=1
                else:
                        hashmap[c]-=1
        print(hashmap)
        if all(v==0 for v in hashmap.values()):
                return True
        else:
                return False

print(isAnagram("anagram","nagaram"))