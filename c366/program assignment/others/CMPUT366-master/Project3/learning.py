import mountaincar as mc
import numpy
from Tilecoder import numTilings, tilecode, numTiles
from Tilecoder import numTiles as n
from pylab import *  #includes numpy

numRuns = 1
numEpisodes = 20
numActions = 3
alpha = 0.5/numTilings
gamma = 1
lmbda = 0.9
Epi = Emu = epsilon = 0
n = numTilings * numTiles * numActions
F = [-1]*numpy.ones(numTilings)

def Qs(F):
    Q=numpy.zeros(numActions)
    for a in range(3):
        for i in F:
            Q[a]+= theta[i+a*324]
    return Q

runSum = 0.0
for run in xrange(numRuns):
    theta = -0.01*numpy.random.rand(n)
    returnSum = 0.0
    for episodeNum in xrange(numEpisodes):
        G = 0
        #your code goes here (20-30 lines, depending on modularity)
        step=0
        e=numpy.zeros(n)
        s = mc.init()
        Q=numpy.zeros(numActions)
        while s != None:
            #print Q
            step+=1
            tilecode(s[0],s[1],F)
            Q=Qs(F)
            a = numpy.argmax(Q)
            r, s1 = mc.sample(s,a)
            G+=r
            delta=r-Q[a]
            for i in F:
                    e[i+a*324]=1
            if s1 == None:
                for i in range(n):
                    theta[i]+=alpha*delta*e[i]
                break
            tilecode(s1[0],s1[1],F)
            Q=Qs(F)
            delta=delta+numpy.max(Q)
            for i in range(n):
                theta[i]+=alpha*delta*e[i]
                e[i]=lmbda*e[i]
            s = s1
        
        print "Episode: ", episodeNum, "Steps:", step, "Return: ", G
        returnSum = returnSum + G
    print "Average return:", returnSum/numEpisodes
    runSum += returnSum
print "Overall performance: Average sum of return per run:", runSum/numRuns


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

writeF()
