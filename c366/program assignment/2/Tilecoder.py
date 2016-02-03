import numpy
import math


numTilings = 8 
tileMove = -0.6/8


    


def tilecode(x,y,tileIndices):
    spaceY = 0.6
    spaceX = 0.6
     
    movement = 0  # movement of the tilings.


    for i in range (0,8):
        
        index = 121*i
        movement = i * tileMove

        coordX= math.floor((x- movement)/spaceX)
        coordY= math.floor((y- movement)/spaceY)

        index = index + ( coordY * 11 + coordX)
        tileIndices[i] = index

  
   



def printTileCoderIndices(x,y):
    tileIndices = [-1]*numTilings
    tilecode(x,y,tileIndices)
    print 'Tile indices for input (',x,',',y,') are : ', tileIndices

printTileCoderIndices(0.1,0.1)
printTileCoderIndices(4.0,2.0)
printTileCoderIndices(5.99,5.99)
printTileCoderIndices(4.0,2.1)

printTileCoderIndices(6.0,6.0)
    
