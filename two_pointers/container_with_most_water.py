def maxArea(height):
        n = len(height)
        i = 0
        j = n-1
        
        maxAr = 0
        baseVal = 0
        heightVal = 0
        area = 0
        
        while i < j :

                baseVal = abs(j-i)
                heightVal = min(height[i], height[j])
                area = baseVal * heightVal
                if maxAr < area:
                        maxAr=area

                if height[i]<height[j]:
                        i+=1
                else:
                        j-=1
                        

        return maxAr

print(maxArea([1,8,6,2,5,4,8,3,7]))