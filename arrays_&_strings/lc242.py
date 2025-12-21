def isAnagram(s,t):
    list1=[]
    list2=[]
    
    for i in s:
        list1.append(i)
    for j in t:
        list2.append(j)

    list1.sort()
    list2.sort()

    return list1==list2

#case 1 : s = "anagram", t = "nagaram"
print(isAnagram("anagram","nagaram"))
#case 2 : s = "rat", t = "car"
#print(isAnagram("rat","car"))