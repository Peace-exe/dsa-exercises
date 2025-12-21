def areAlmostEqual(s1,s2)->bool:
    

    index = []

    if s1==s2:
        return True

    for i in range(len(s1)):
        if s1[i]!= s2[i]:
            index.append(i)
        
    if len(index)==2:
        if s1[index[0]]==s2[index[1]] and s1[index[1]]==s2[index[0]]:
            return True
        else:
            return False
    else:
        return False



#test cases

#case 1 : s1 ="bank" s2 ="kanb"
print(areAlmostEqual("bank","kanb"))
#case 2: s1="attack", s2 = "defend"
print(areAlmostEqual("attack","defend"))
#case 3 : s1 = "kelb", s2 = "kelb"
print(areAlmostEqual("kelb","kelb"))
#case 4 : s1="aa" , s2="ac"
print(areAlmostEqual("aa","ac"))