#roman to integer

def romanToInt(s:str)->int:

    hashmap = {
    "I":1,
    "V":5,
    "X":10,
    "L":50,
    "C":100,
    "D":500,
    "M":1000
    }

    stack=[]

    i= 0 
    j= 1
    
    while(i<len(s)):

        if(len(s)>1):

            if (hashmap[s[i]] < hashmap[s[j]]):

                stack.append(-hashmap[s[i]])
            else:

                stack.append(hashmap[s[i]])
        else:
            stack.append(hashmap[s[i]])
        i+=1

        if(i<len(s)-1):
            j+=1
        else:
            continue


    sum = 0 

    for k in stack:

        sum +=k
    
    return sum 

print(romanToInt("M"))



        

    


