'''

/*
 * (C) Ashish Saxena <ashish@reak.in>
 * (C) 2016 REAK INFOTECH LLP
 *
 * The LICENSE file included with the project would govern the use policy for this code,
 * In case of missing LICENSE file the code will be treated as an Intellectual Property of the creator mentioned above,
 * All rights related to distribution, modifcation, reselling, use for commercial or private use of this code is terminated.
 *
 */

'''
import random

'''
Player Probability
(Kirat Boli, N.S Nodhi, R Rumrah, Shashi Henra)

Initialization Vars
'''
players = ["Kirat Boli", "N.S Nodhi", "R Rumrah", "Shashi Henra"]
playerRunProb=[[5,30,25,10,15,1,9,5],[10,40,20,5,10,1,4,10],[20,30,15,5,5,1,4,20],[30,25,5,0,5,1,4,30]]
runfinder=[0,1,2,3,4,5,6,"OUT!"]
cacheplayerRunProb = []
personalPlayerTotals = [0,0,0,0]
teamtotal = 0


def cumulate(array):
    total = 0
    for x in array:
        total += x
        yield total

def buildprep():
	# Nothing but simply caching a cumulative list to avoid doing it again and again for the length of the program
	for player in playerRunProb:
		cacheplayerRunProb.append(list(cumulate(player)))
	

def playball(player,over,ball):
	ranobj = random.SystemRandom()
	weight = ranobj.randint(0, 100)
	for index, meh in enumerate(cacheplayerRunProb[player]):
		if (weight < meh) :
			print str(over)+"."+str(ball)+" "+players[player]+" scores "+str(runfinder[index]) if "OUT!" !=str(runfinder[index]) else str(over)+"."+str(ball)+" "+players[player]+" is OUT!, What a blow to Lengaburu!"
			break
	# Get the score back, for computing total
	return runfinder[index]
	
def addtotal(value):
	global teamtotal
	teamtotal += int(value)
	
def addtopersonal(player, value):
	global personalPlayerTotals
	personalPlayerTotals[player] += int(value)
	
def changestrike(array):
	array[0], array[1] = array[1], array[0]
	
def main():
	# Build the cumulative cache
	buildprep()
	
	playerplaying = [0,1]
	wickets = 0
	
	for over in range(0,4):
		for ball in range(1,7):
			run = playball(playerplaying[0],over,ball)
			if run != "OUT!":
				addtotal(run)
				addtopersonal(playerplaying[0], run)
				if (run%2):
					# Not even, Need to change strike
					changestrike(playerplaying)
			else:
				# Player is out
				pass
		print teamtotal
		print personalPlayerTotals
	
if __name__ == "__main__":
   main()