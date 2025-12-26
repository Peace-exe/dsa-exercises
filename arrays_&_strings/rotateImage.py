def rotate(matrix:list[list[int]])->list[list[int]]:

            #transpose of the matrix

            n=len(matrix)
            i,j=0,0

            while i <len(matrix):
                
                while j < len(matrix):
                        matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
                        j+=1
                j=0
                i+=1
                j+=i

            #horizontal flip of the matrix
            i=0
            j=n-1
            k=0
            while k<n:
                    
                    while i<j:
                            matrix[k][i] ,matrix[k][j] = matrix[k][j] ,matrix[k][i]
                            i+=1
                            j-=1
                    i=0
                    j=n-1
                    k+=1
            return matrix


print(rotate([[1,2,3],[4,5,6],[7,8,9]]))