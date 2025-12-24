def maxTwoEvents(events : list[list[int]])->int:

    if not events:
        return 0
    events.sort(key= lambda interval:interval[0] )
    for i in range(len(events)):
        print(events[i])
        

maxTwoEvents([[1,3,2],[4,5,2],[2,4,3]])