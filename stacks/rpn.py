def eval(tokens):

    stack =[]

    for i in tokens:

        if i == "+":
            popped = stack.pop()
            stack[-1]= stack[-1]+popped
            print(f" stack at i = {i}, stack: {stack}\n")
        elif i == "-":
            popped = stack.pop()
            stack[-1]= stack[-1]-popped
            print(f" stack at i = {i}, stack: {stack}\n")
        elif i =="*":
            popped = stack.pop()
            stack[-1]= stack[-1]*popped
            print(f" stack at i = {i}, stack: {stack}\n")
        elif i == "/":
            popped = stack.pop()
            stack[-1]= int(stack[-1]/popped)
            print(f" stack at i = {i}, stack: {stack}\n")
        else:
            stack.append(int(i))
            print(f" stack at i = {i}, stack: {stack}\n")
        
    return stack[0]

print(eval(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))