def calPoints(operations):

    stack = []
    

    for i in range(len(operations)):

        #print(f"{stack}\n")
        if operations[i] == "+":
            stack.append(stack[-1]+stack[-2])
        elif operations[i] == "D":
            stack.append(stack[-1]*2)
        elif operations[i]=="C":
            stack.pop()
        else:
            stack.append(int(operations[i]))

    return sum(stack) 


print(calPoints(["5","2","C","D","+"]))

