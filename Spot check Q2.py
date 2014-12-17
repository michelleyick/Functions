#Michelle Yick
#17-12-2014
#Functions spot check Q2

#Define functions
def GetGridSize():
    vaildGrid = " "
    thisGridsize =  0
    validGrid = False
    while validGrid == False:
        thisGridsize = int(input("Please enter the size of the grid (max 20): "))
       if thisGridsize <= 20:
            validGrid = True
        if thisGridsize <= 0:
            validGrid = False
   
    
    return thisGridsize
def GetGridRow(aRowLength):
    # draws a single row using |_ for each square
    thisRow = '|_' * (thisGridsize)
    # add closing | to row
    thisRow = thisRow + '|'
    return thisRow
 
def DisplayGrid(thisGridsize, aRow):
    # display top of grid using _ as top of each square
    print(' _' *thisGridsize )
    # display rows of |_| for each row
    for rowCount in range(thisGridsize):
        print(aRow)
 
# main program
thisGridsize = GetGridSize()
rowToDraw = GetGridRow(5)
DisplayGrid(thisGridsize, rowToDraw)
