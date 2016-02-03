#---------------------------------------------------------------
# Course:           CMPUT 366
# Assignment:       Project1
# Due Date:         Nov 5, 2015
# Names:            Mujda Abbasi - Zainab Alsharif
# Student ID:         1298314         1223455
#---------------------------------------------------------------

import blackjack as bj
import numpy as np
from pylab import *

numEpisodes = 2000
returnSum = 0.0

for episodeNum in range(numEpisodes):
    G = 0
    s = bj.init()
    while s != -1:
        r, s = bj.sample(s,np.random.randint(2))
        G+=r
    
    print "Episode: ", episodeNum, "Return: ", G
    returnSum = returnSum + G
print "Average return: ", returnSum/numEpisodes
