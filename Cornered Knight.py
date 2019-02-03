"""
Cornered Knight Problem

January 30, 2019

Alex Pavlik
"""

import matplotlib.pyplot as plt
#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
#-----------------------------------Functions------------------------------------
#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------


#--------------------------------------------------------------------------------
#Function to generate the 2-D array for all of the board positions
#--------------------------------------------------------------------------------

def Generate(n):
	ar=[]
	val=0
	for i in range(n):
		temp = []
		for j in range(i+1):
			val+=1
			#print(d)
			temp.append(val)
		ar.append(temp)
		
	return ar



#--------------------------------------------------------------------------------
#Function to shift the point from the true grid to the generated grid
#--------------------------------------------------------------------------------

def Shear(point):
    val = point[:]
    val[0] = val[0] + val[1]
    return val


#--------------------------------------------------------------------------------
#Function to identify all possible areas to move and their values
#--------------------------------------------------------------------------------

def Spots(currentPos):
    
    directionOperators = {0: [-1,-1],#                          0   1
                          1: [1,-1], #                           \ /
                          2: [-1,1], #Each diagonal direction:    o
                          3: [1,1]}  #                           / \
                                     #                          2   3
    testPos = []
    order = [0,1,2,5,3,4,7,6]
    #Checking each possible option in each available direction
    for i in range(4):
        operator = directionOperators[i]
        #print("Operator:",operator)
        
        testPos.append([currentPos[0] + operator[0], currentPos[1] + 2 * operator[1]])
        testPos.append([currentPos[0] + 2 * operator[0], currentPos[1] + operator[1]])
    #for j in range(len(testPos)):
            #print(testPos[j])
        
        #This ordering should make sure the lowest number is always chosen
    for i in order:
        if Test(testPos[i]):
            #print(i)
            currentPos = Move(testPos[i])
            return currentPos, False
                            
    #print("Knight is stuck at edge of board")
    return currentPos, True

#--------------------------------------------------------------------------------
#Function to move the Knight to the next available spot
#--------------------------------------------------------------------------------

def Test(tpoint):
    TshearPoint = Shear(tpoint)
    #print('Testing sheared value:', TshearPoint)
    
    #Make sure its in range
    if TshearPoint[0] >= 0 and TshearPoint[1] >= 0:
        if TshearPoint[0] < diags:
            if TshearPoint[1] < len(array[TshearPoint[0]]):
                #Make sure the point has never been visited.
                if array[TshearPoint[0]][TshearPoint[1]] is not 0:
                    return True
        
    return False

#--------------------------------------------------------------------------------
#Function to finalize the move of the Knight
#--------------------------------------------------------------------------------

def Move(mpoint):
    MshearPoint = Shear(mpoint)
    
    #print('Moving to sheared position', MshearPoint, "with a value of:", array[MshearPoint[0]][MshearPoint[1]])

    values.append(array[MshearPoint[0]][MshearPoint[1]])
    array[MshearPoint[0]][MshearPoint[1]] = 0

    return mpoint

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
#-----------------------------------Body-----------------------------------------
#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------



#--------------------------------------------------------------------------------
#Global Variable Definition
#--------------------------------------------------------------------------------

diags = int(input('Number of Collums'))
xpos = int(input('Starting X Position'))
ypos = int(input('Starting Y Position'))
position = [xpos,ypos]

xvals = [xpos]
yvals = [ypos]
values = []

trapped = False

#--------------------------------------------------------------------------------
#Start Up Code
#--------------------------------------------------------------------------------

array = Generate(diags)
values.append(array[xpos+ypos][ypos])
array[xpos+ypos][ypos] = 0

while not trapped:
    #print('Cycle Starting Postion', position)
    position, trapped = Spots(position)
    xvals.append(position[0])
    yvals.append(position[1])
#print(values)
print(position)
plt.title('Path of the Trapped Knight')
plt.plot(yvals,xvals)
#plt.minorticks_on()
#plt.grid(True, 'both', 'both')
plt.show()

