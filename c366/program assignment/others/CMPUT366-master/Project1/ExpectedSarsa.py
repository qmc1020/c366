#---------------------------------------------------------------
# Assignment:       Project1
# Due Date:         Nov 5, 2015
# Names:            Mujda Abbasi - Zainab Alsharif
# Student ID:         1298314         1223455
#---------------------------------------------------------------

import blackjack as bj
import numpy as np
from pylab import *

numEpisodes = 200000
returnSum = 0.0

num_states = 181
num_actions = 2

alpha = 0.00005

emu = 1.0
epi= 0.00001

#Function to find the probability of a given action given the policy
def actionProb(e,a,s):
    if np.argmax(Q[s]) == a:
        return 1 - e + e/num_actions
    else:
        return e/num_actions


#Learning the policy through the Expected Sarsa algorithm
Q =  0.00001*np.random.rand(num_states,num_actions)

for episodeNum in range(numEpisodes):
    G = 0

    s = bj.init()
    while s != -1:
        a = np.random.choice(2, p=[actionProb(emu,0,s),actionProb(emu,1,s)])
        r, s1 = bj.sample(s,a)
        Q[s,a] = Q[s,a] + alpha*(r + actionProb(epi,0,s1)*Q[s1,0] + actionProb(epi,1,s1)*Q[s1,1] - Q[s,a])
        s = s1
        G+=r

    returnSum = returnSum + G

    if episodeNum%10000 == 0:
        print "Episode: ", episodeNum
        print "Average return: ", returnSum/(episodeNum+1)

#Function for the learned policy
def learnedPolicy(s):
    return np.argmax(Q[s])

#Printing out the learned policy
bj.printPolicy(learnedPolicy)


#Following the learned policy deterministically
returnSum = 0.0

for episodeNum in range(numEpisodes):
    G = 0

    s = bj.init()
    while s != -1:
        r, s = bj.sample(s,learnedPolicy(s))
        G+=r

    returnSum = returnSum + G

    if episodeNum%10000 == 0:
        print "Episode: ", episodeNum
        print "Average return: ", returnSum/(episodeNum+1)

#Printing out the learned policy
bj.printPolicy(learnedPolicy)


#Following the learned policy deterministically
returnSum = 0.0
