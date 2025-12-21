def longestCommonPrefix(strings):

    shortestStringLength = len( min(strings , key=len) )

    letters=[]
    equal = True
    prefix=[]
    for index in range(shortestStringLength):

        for string in strings:

            letters.append(string[index])

            
        equal = len( set(letters) ) <= 1

        if index==0 and not equal :
            return ""
        elif not equal:
            break
        else:
            prefix.append(string[index])


        letters=[]

    return "".join(prefix)

#test 1:
strs = ["dog","racecar","car"]
print(longestCommonPrefix(strs))
        



