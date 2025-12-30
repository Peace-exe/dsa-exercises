def isValidSudoku(board:list[list[int]])->bool:

            hashmap={

            }
            m=9
            n=9
            indices =[]
            for i in range(m):
                for j in range(n):
                    if board[i][j] != "." and int(board[i][j]) not in hashmap:
                        hashmap[int(board[i][j])] = [[i,j]]
                    elif board[i][j]!= ".":
                        hashmap[int(board[i][j])].append([i,j])
                    else:
                        continue
            print(hashmap)
            for i in range(1,10):
                if i in hashmap:
                    indices = hashmap[i]
                    #print(indices)
                    if len(indices)>1:
                            
                        for j in range(len(indices)):
                            for k in range(j+1,len(indices)):
                                if( indices[j][0] == indices[k][0] )or( indices[j][1]== indices[k][1]):
                                    return False 
                        
            

            grids = {}
            #gridNum : int = 0
            row : int = 0
            col : int = 0
            value : int =0
            
            for gridNum in range(0,9):

                if gridNum == 0:
                    
                    for row in range(0,3):
                        for col in range(0,3):
                            value = board[row][col]
                            if value != "." and int(gridNum) not in grids:
                                grids[int(gridNum)]=[value]
                            elif value!=".":
                                grids[int(gridNum)].append(value)
                            else:
                                continue
                    row = 0
                    col = 0
                
                elif gridNum == 1:
                    
                    for row in range(0,3):
                        for col in range(3,6):
                            value = board[row][col]
                            if value != "." and int(gridNum) not in grids:
                                grids[int(gridNum)]=[value]
                            elif value!=".":
                                grids[int(gridNum)].append(value)
                            else:
                                continue
                elif gridNum == 2:
                    
                    for row in range(0,3):
                        for col in range(6,9):
                            value = board[row][col]
                            if value != "." and int(gridNum) not in grids:
                                grids[int(gridNum)]=[value]
                            elif value!=".":
                                grids[int(gridNum)].append(value)
                            else:
                                continue
                elif gridNum == 3:
                    
                    for row in range(3,6):
                        for col in range(0,3):
                            value = board[row][col]
                            if value != "." and int(gridNum) not in grids:
                                grids[int(gridNum)]=[value]
                            elif value!=".":
                                grids[int(gridNum)].append(value)
                            else:
                                continue
                elif gridNum == 4:
                    
                    for row in range(3,6):
                        for col in range(3,6):
                            value = board[row][col]
                            if value != "." and int(gridNum) not in grids:
                                grids[int(gridNum)]=[value]
                            elif value!=".":
                                grids[int(gridNum)].append(value)
                            else:
                                continue
                elif gridNum == 5:
                    
                    for row in range(3,6):
                        for col in range(6,9):
                            value = board[row][col]
                            if value != "." and int(gridNum) not in grids:
                                grids[int(gridNum)]=[value]
                            elif value!=".":
                                grids[int(gridNum)].append(value)
                            else:
                                continue
                elif gridNum == 6:
                    
                    for row in range(6,9):
                        for col in range(0,3):
                            value = board[row][col]
                            if value != "." and int(gridNum) not in grids:
                                grids[int(gridNum)]=[value]
                            elif value!=".":
                                grids[int(gridNum)].append(value)
                            else:
                                continue
                elif gridNum == 7:
                    
                    for row in range(6,9):
                        for col in range(3,6):
                            value = board[row][col]
                            if value != "." and int(gridNum) not in grids:
                                grids[int(gridNum)]=[value]
                            elif value!=".":
                                grids[int(gridNum)].append(value)
                            else:
                                continue
                elif gridNum == 8:
                    
                    for row in range(6,9):
                        for col in range(6,9):
                            value = board[row][col]
                            if value != "." and int(gridNum) not in grids:
                                grids[int(gridNum)]=[value]
                            elif value!=".":
                                grids[int(gridNum)].append(value)
                            else:
                                continue
            
            print(grids)
            values = []

            for gridNum in range(0,9):
                if gridNum in grids:
                    values= grids[gridNum]
                    for i in range(len(values)):
                        for j in range(i+1,len(values)):
                            if values[i]==values[j]:
                                return False
                    #print(values)
            
            return True


board = [[".",".",".",".",".",".","5",".","."],
         [".",".",".",".",".",".",".",".","."],
         [".",".",".",".",".",".",".",".","."],
         ["9","3",".",".","2",".","4",".","."],
         [".",".","7",".",".",".","3",".","."],
         [".",".",".",".",".",".",".",".","."],
         [".",".",".","3","4",".",".",".","."],
         [".",".",".",".",".","3",".",".","."],
         [".",".",".",".",".","5","2",".","."]]

print(isValidSudoku(board))