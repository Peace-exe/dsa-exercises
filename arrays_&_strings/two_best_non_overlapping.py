def maxTwoEvents(events : list[list[int]])->int:

        if not events:
            return 0
        events.sort(key= lambda interval:interval[0] )
        maxSum = 0
        validInterval=-1

        suffixMax = [0]*len(events)
        suffixMax[-1]=events[-1][2]

        for i in range(len(events)-2,-1,-1):
              suffixMax[i]=max(events[i][2], suffixMax[i+1])

        for i in range(len(events)):
            
            validInterval=-1

            if(maxSum<events[i][2]):
                    maxSum=events[i][2]


            low= i+1
            high = len(events)-1
            while low<=high:
                    mid = (low+high)//2

                    #going left
                    if events[mid][0]> events[i][1]:
                          validInterval=mid
                          high = mid-1
                    #going right 
                    if events[mid][0]<=events[i][1]:
                          low = mid+1
            
            if validInterval>-1:
                  maxSum = max(maxSum, events[i][2] + suffixMax[validInterval])
            
            
                      
        return maxSum                 
        
        
        

print(maxTwoEvents([[1,5,3],[1,5,1],[6,6,5]]))