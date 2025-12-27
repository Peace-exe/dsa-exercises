def canConstruct(ransomNote: str, magazine: str) -> bool:
            lettersInMagazine={}

            for c in magazine:
                    if c in lettersInMagazine:
                            lettersInMagazine[c]+=1
                    else:
                            lettersInMagazine[c]=1
            
            for i in ransomNote:
                    if i not in lettersInMagazine or lettersInMagazine[i]==0:
                            return False
                    lettersInMagazine[i]-=1
            return True            
print(canConstruct("a","b"))