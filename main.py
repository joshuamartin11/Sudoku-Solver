def checkSquare(coord, solPuzzle):
    xSquare = coord[0]//3
    ySquare = coord[1]//3
    for x in range(xSquare*3,xSquare*3+3):
        for y in range(ySquare*3,ySquare*3+3):
            if solPuzzle[x][y] == solPuzzle[coord[0]][coord[1]] and (x != coord[0] and y != coord[1]):
                return False
    return True

def checkCol(coord, solPuzzle):
    for y in range(0,9):
        if solPuzzle[coord[0]][y] == solPuzzle[coord[0]][coord[1]] and y != coord[1]:
            return False
    return True

def checkRow(coord, solPuzzle):
    for x in range(0,9):
        if solPuzzle[x][coord[1]] == solPuzzle[coord[0]][coord[1]] and x != coord[0]:
            return False
    return True

def checkValid(solPuzzle):
    for x in range(0,9):
        for y in range(0,9):
           if(not(checkCol((x,y),solPuzzle) and checkRow((x,y),solPuzzle) and checkSquare((x,y),solPuzzle))):
               return False
    return True

def solve(solPuzzle,curC):


    #Searches for the first blank square.
    while solPuzzle[curC[0]][curC[1]] != 0:
        curC = (curC[0], curC[1] + 1)
        if curC[1] == 9:
            curC = (curC[0] + 1, 0)
            if curC[0] == 9:
                return True
    solved = False

    while not solved:
        solPuzzle[curC[0]][curC[1]] += 1
        if(solPuzzle[curC[0]][curC[1]] > 9):
            solPuzzle[curC[0]][curC[1]] = 0
            return False

        if(checkCol(curC,solPuzzle) and checkRow(curC,solPuzzle) and checkSquare(curC,solPuzzle)):
            if(curC[0] == 8 and curC[1] == 8):
                # for r in solPuzzle:
                #     print(r)
                # exit()
                return True
            # for r in solPuzzle:
            #     print(r)
            # print()

            solved = solve(solPuzzle, curC)
    return True
            
        

def main():
    puzzle =    ["530070000",
                 "600195000",
                 "098000060",
                 "800060003",
                 "400803001",
                 "700020006",
                 "060000280",
                 "000419005",
                 "000080079"]

    solPuzzle = list()
    for r in puzzle:
        solPuzzle.append([int(num) for num in r])

    for r in solPuzzle:
        print(r)
    print()
    solve(solPuzzle, (0,0))
    if checkValid(solPuzzle):

        for r in solPuzzle:
            print(r)
    else:
        print("Invalid")
        
if __name__ == '__main__':
    main()