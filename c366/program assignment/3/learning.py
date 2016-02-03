import mountaincar as mountaincar
from Tilecoder import numTilings, tilecode, numTiles
from Tilecoder import numTiles as n
from pylab import *  #includes numpy
import numpy

numRuns = 1
numEpisodes = 200
alpha = 0.5/numTilings
gamma = 1
lmbda = 0.9
Epi = Emu = epsilon = 0
n = numTiles * 3 * numTilings
e_para = 4 * 9 * 9  #numTilings x tilesPerTiling x numActions
F = [-1]*numTilings

fout1 = open('value1.csv', 'w')

def newQ(F):
    Q=numpy.zeros(3)
    for action in range(3):
        for i in F:
            Q[action]+= theta[i+action*e_para]
    return Q


for j in range(50):
    runSum = 0.0
    for run in xrange(numRuns):
        theta = -0.01*rand(n*numTilings)
        returnSum = 0.0
        for episodeNum in xrange(numEpisodes):
            G = 0
            #your code goes here (20-30 lines, depending on modularity)
            
            #initialize
            
            Q=numpy.zeros(3)
            St = mountaincar.init()
            et = numpy.zeros(n)
            step = 0
            
            
            while St != None:  
                
                step+=1
                tilecode(St[0],St[1],F)
                Q=newQ(F)
                
                # policy here, if Epi is changed, action may select differently
                action = numpy.argmax(Q)
                if Epi > random_sample():
                    action = randint(0,3)
                    
                r, St1 = mountaincar.sample(St,action)
                G+=r
                delta=r-Q[action]
                for i in F:
                        et[i+action*e_para]=1
                if St1 == None:
                    for i in range(n):
                        theta[i]+=alpha*delta*et[i]
                    break
                tilecode(St1[0],St1[1],F)
                Q=newQ(F)
                delta=delta+numpy.max(Q)
                
                for i in range(n):
                    theta[i]+=alpha*delta*et[i]
                    et[i]=lmbda*et[i]
                St = St1
                
                
            
            print "Episode: ", episodeNum, "Steps:", step, "Return: ", G
            returnSum = returnSum + G
            fout1.write(repr(returnSum/(episodeNum+1)) + ', ')
            
        print "Average return:", returnSum/numEpisodes
        fout1.write('\n')
        runSum += returnSum
    print "Overall performance: Average sum of return per run:", runSum/numRuns
fout1.close()

#Additional code here to write average performance data to files for plotting...
#You will first need to add an array in which to collect the data

def writeF():
    fout = open('value', 'w')
    F = [0]*numTilings
    steps = 50
    for i in range(steps):
        for j in range(steps):
            tilecode(-1.2+i*1.7/steps, -0.07+j*0.14/steps, F)
            height = -max(Qs(F))
            fout.write(repr(height) + ' ')
        fout.write('\n')
    fout.close()

#writeF()
