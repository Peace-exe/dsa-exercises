def dailyTemp(temperatures: list[int]):
    n = len(temperatures)

    answer = [0]*n

    stack =[]

    for i, temp in enumerate(temperatures):
        while stack and stack[-1][1]<temp:
            stack_day, stack_temp = stack.pop()
            answer[stack_day]= i - stack_day
        stack.append((i,temp))
    return answer

print(dailyTemp([73,74,75,71,69,72,76,73]))
