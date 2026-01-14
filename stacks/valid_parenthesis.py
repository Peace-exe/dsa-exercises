def isValid(s:str):

    brackets = {
        ")":"(",
        "]":"[",
        "}":"{"


    }
    stack =[]

    for b in s:

        if b not in brackets:
            stack.append(b)
        else:

            if not stack:
                return False
            else:
                popped = stack.pop()
                if popped != brackets[b]:
                    return False
    
    return not stack



print(isValid("({}])"))
