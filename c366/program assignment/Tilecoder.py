import numpy
import math


numTilings = 4
numTiles = 81


    


def tilecode(x,y,tileIndices):

    for i in range (0,tileIndices):
        
        Xindex = int(((x+1.2)+i*0.2125/numTilings)*8/1.7)
        Yindex = int(((y+0.07)+i*0.0175/numTilings)*8/0.14)
        tileIndices[i] = i*numTiles+Xindex+9*Yindex

  
   



def printTileCoderIndices(x,y):
    tileIndices = [-1]*numTilings
    tilecode(x,y,tileIndices)
    print 'Tile indices for input (',x,',',y,') are : ', tileIndices

#printTileCoderIndices(0.1,0.1)
#printTileCoderIndices(4.0,2.0)
#printTileCoderIndices(5.99,5.99)
#printTileCoderIndices(4.0,2.1)

#printTileCoderIndices(6.0,6.0)
    
