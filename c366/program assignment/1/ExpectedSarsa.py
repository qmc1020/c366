import blackjack
from pylab import *




numEpisodes = 1000000
e = 1
alpha = 0.001
returnSum = 0.0

Q = [[0,0]]*183
#for i in Q:
 #   i[0],i[1]= uniform(0,1),uniform(0,1)

for episodeNum in range(numEpisodes):
    G = 0
    # my code starts here
    a=0
    
    S =blackjack.init()
    t = Q[S]
    if (e > randint(0, 2)):
        R,S_ =blackjack.sample(S,randint(0,2))
    else:
        if t[0]>t[1]:
            R,S_ = blackjack.sample(S,0)
            a=0
        else:
            R,S_ = blackjack.sample(S,1)
            a=1
    while (S_!=(-1)):
        Q[S][a] = Q[S][a] + alpha*(R + Q[S_][0]+Q[S_][1]-Q[S][a])
        S=S_
        t = Q[S]
        if (e > randint(0, 2)):
            R,S_ = blackjack.sample(S,randint(0,2))
        else:
            if t[0]>t[1]:
                R,S_ = blackjack.sample(S,0)
                a=0
            else:
                R,S_ = blackjack.sample(S,1)
                a=1
        
    Q[S][a] = Q[S][a] + alpha*(R + Q[S_][0]+Q[S_][1]-Q[S][a])
    G = R    
    
            
    
    returnSum = returnSum + G
print "Average return: ", returnSum/numEpisodes



###########################################################
#part2 e = 0.01
numEpisodes = 1000000
e = 0.01
alpha = 0.001
returnSum = 0.0
h=0

Q = [[0,0]]*183
#for i in Q:
 #   i[0],i[1]= uniform(0,1),uniform(0,1)

for episodeNum in range(numEpisodes):
    h+=1
    G = 0
    a=0
    
    S =blackjack.init()
    t = Q[S]
    if (e > uniform(0,1)):
        R,S_ =blackjack.sample(S,randint(0,2))
    else:
        if t[1]>t[0]:
            R,S_ = blackjack.sample(S,1)
            a=1
        else:
            R,S_ = blackjack.sample(S,0)
            a=0
    Q[S][a] = Q[S][a] + alpha*(R + Q[S_][0]+Q[S_][1]-Q[S][a])
    if (S_==(-1)): R=1
    
    while (S_!=(-1)):
        S=S_
        t = Q[S]
        if (e > randint(0, 2)):
            R,S_ = blackjack.sample(S,randint(0,2))
        else:
            if t[0]>t[1]:
                R,S_ = blackjack.sample(S,0)
                a=0
            else:
                R,S_ = blackjack.sample(S,1)
                a=1
        Q[S][a] = Q[S][a] + alpha*(R + Q[S_][0]+Q[S_][1]-Q[S][a])
    Q[S][a] = Q[S][a] + alpha*(R + Q[S_][0] + Q[S_][1] - Q[S][a])
    G = R    
    
            
        
    returnSum = returnSum + G
    if (h==9999 ):
        print "numEpisod",episodeNum, "Average return: ", returnSum/numEpisodes
        h=0
print "numEpisod",episodeNum, "Average return: ", returnSum/numEpisodes

def policy(index):
    a,b = Q[index]
    if (a>b): return 0
    return 1
blackjack.printPolicy(policy)