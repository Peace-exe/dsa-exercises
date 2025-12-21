#valid parenthesis

def isValid(s:str)->bool:

    stack = []

    hashMap = {")" : "(" ,
               "}" : "{" ,
               "]" : "["}
    
    for c in s:

        if c not in hashMap:#opening bracket case
            stack.append(c)
        else:# closing bracket case

            if not stack:
                return False
            else:
                popped = stack.pop()

                if popped != hashMap[c]:
                    return False
        
    
    return not stack #returns true if stack is empty in the end.


print(isValid(")"))


        
    



    