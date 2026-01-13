def trap(height):

        n = len(height)
        leftWall= rightWall = 0
        leftMax=[0]*n
        rightMax = [0]*n
        totalWater = 0
        bucket = 0

        j=0
        for i in range(n):
                j=-1-i

                leftMax[i]=leftWall
                rightMax[j]= rightWall

                leftWall = max(leftWall,height[i])
                rightWall = max(rightWall,height[j])

        for k in range(n):
                
                bucket = min(leftMax[k],rightMax[k])
                totalWater+= max(0, bucket-height[k])
        
        return totalWater

'''
#Bug to remember 
 
leftMax = rightMax = [0]*n 
    # does not create two saperate lists, it creates one and assigns two names to it.
    # writing rightMax will also overwrite leftMax

so why this doesn't happen with variables?? a=b=1
    # Because numbers are immutable objects and lists are not
    # when we do this both are stored at saperate addresses

'''        


        
