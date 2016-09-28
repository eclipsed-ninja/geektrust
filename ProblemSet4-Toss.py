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
import random, sys

'''
Default Values goes here
'''
teams = ['Lengaburu', 'Enchai']
# 1 = Bats, 0 = Bowls
decision = ["Bowls", "Bats"]
tossdecision = [{"Clear":1, "Cloudy":0, "Day":1, "Night":0},{"Clear":0, "Cloudy":1, "Day":0, "Night":1}]



'''
All code goes here
'''

def toss():
	'''
	Trying to be "more" random by utlizing os.urandom()
	'''
	ranobj = random.SystemRandom()
	return ((ranobj.randint(0, sys.maxint))%2)
	
def winner(team, weather, timeofday):
	'''
	Winner trying to choose what they will pick, Bat or Bowl
	Because of dict inside list, we are free of respective input ie., Cloudy Day and Day Cloudy are both acceptable inputs
	'''
	# DELETE ME : Lengaburu wins toss and bats
	return teams[team]+" wins the toss and bats" if ((tossdecision[team][weather]) | (tossdecision[team][timeofday])) else teams[team]+" wins the toss and bowls"


def main(argv):
	tosswinner = toss()
	print winner(tosswinner, sys.argv[1], sys.argv[2])
	

if __name__ == "__main__":
   main(sys.argv[1:])