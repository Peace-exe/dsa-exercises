#leetcode 392 : is subsequence

def isSubSequence(self, s :str , t :str)->bool:

    listT = list(t)

    flag=0

    for i in range(len(listT)):

        for j in s:

            if listT[i]==j:
                flag=1
        
        if(flag!=1):
            listT[i]=""
        
        flag=0
    
    if(s=="".join(listT)):
        return True
    else:
        return False

            


print(isSubSequence("abc","ahbgdc"))  

