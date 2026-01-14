def isValid(s:str):

    brackets = {
        "(":")",
        "[":"]",
        "{":"}"

    }

    stack =[]

    
    
    for i in range(len(stack)):
        stack.append(s[i])

        if s[i-1] s[i]==brackets[s[i-1]]:
            stack.pop()
            stack.pop()


print(isValid("([])"))
