def spiralOrder(matrix: list[list[int]])->list[int]:

        res=[]
        n = len(matrix[0])
        m = len(matrix)
        
        upWall = 0 
        rightWall = len(matrix[0])
        downWall = len(matrix)
        leftWall = -1

        UP,RIGHT,DOWN,LEFT=0,1,2,3
        DIRECTION = RIGHT

        i,j=0,0


        while len(res) != m*n:

            if DIRECTION==RIGHT:
                  while j<rightWall:
                        res.append(matrix[i][j])
                        j+=1
                  rightWall-=1
                  i+=1
                  j-=1
                  DIRECTION=DOWN
            elif DIRECTION==DOWN:
                  while i<downWall:
                        res.append(matrix[i][j])
                        i+=1
                  downWall-=1
                  i-=1
                  j-=1
                  DIRECTION=LEFT
            elif DIRECTION==LEFT:
                  while j>leftWall:
                        res.append(matrix[i][j])
                        j-=1
                  leftWall+=1
                  i-=1
                  j+=1
                  DIRECTION=UP
            else:
                  while i> upWall:
                        res.append(matrix[i][j])
                        i-=1
                  upWall+=1
                  i+=1
                  j+=1
                  DIRECTION=RIGHT
        
        return res
        
print(spiralOrder( [[1,2,3,4],[5,6,7,8],[9,10,11,12]]))

'''
  n
m [1,2,3,4]
  [5,6,7,8]
  [5,6,7,8]
  [5,6,7,8]
  [9,10,11,12]

'''