from collections import defaultdict
def groupAnagrams( strs: list[str]):

        anagrams = defaultdict(list)
        count = []
        for s in strs:
                count = [0]*26
                for c in s:
                        count[ord(c)-ord("a")]+=1
                key = tuple(count)

                anagrams[key].append(s)
        #print(anagrams)
        return list(anagrams.values())

strs = ["eat","tea","tan","ate","nat","bat"]
print(groupAnagrams(strs))
                