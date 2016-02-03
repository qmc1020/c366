import blackjack
from pylab import *

numEpisodes = 2000

returnSum = 0.0
for episodeNum in range(numEpisodes):
    G = 0
    # my code starts here
    
    
    R,S = blackjack.sample(blackjack.init(),(randint(0, 2)))
    if (S==(-1)): R=1
    while (S!=(-1)):
        R,S = blackjack.sample(S,(randint(0, 2)))    
    G = R    
    
            
    print "Episode: ", episodeNum, "Return: ", G 
    returnSum = returnSum + G
print "Average return: ", returnSum/numEpisodes
